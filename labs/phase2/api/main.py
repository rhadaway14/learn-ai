from __future__ import annotations

import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .contract import artifact_filename, build_artifact, validate_phase1_artifact
from .model import FEATURE_ORDER, NeuralRiskModel, TrainingConfig, TrainedModel, predict, train_model
from .store import MemoryStore, PostgresStore


class TrainRequest(BaseModel):
    prediction: str = Field(min_length=20, max_length=2_000)
    seed: int = 17
    epochs: int = Field(default=300, ge=2, le=2_000)
    learning_rate: float = Field(default=0.05, gt=0, le=1_000_000)
    hidden_width: int = Field(default=12, ge=2, le=128)
    patience: int = Field(default=30, ge=1, le=500)


class PredictionRequest(BaseModel):
    planned_integrations: float
    document_count: float
    deadline_days: float
    customer_tier: float
    prior_projects: float


class ArtifactRequest(BaseModel):
    observation: str = Field(min_length=20, max_length=4_000)
    failure_diagnosis: str = Field(min_length=20, max_length=4_000)
    recovery: str = Field(min_length=20, max_length=4_000)
    promotion_rationale: str = Field(min_length=20, max_length=4_000)
    limitation: str = Field(min_length=20, max_length=4_000)


class Phase2Service:
    def __init__(self, store: Any, artifact_dir: str | Path) -> None:
        self.store = store
        self.artifact_dir = Path(artifact_dir)
        self.trained: TrainedModel | None = None
        self.last_prediction = ""
        self.failure_observed = False
        self.recovered_after_failure = False
        self.prediction_made = False

    @property
    def checkpoint_path(self) -> Path:
        return self.artifact_dir / "best-checkpoint.pt"

    def restore_checkpoint(self) -> bool:
        if not self.checkpoint_path.exists():
            return False
        checkpoint = torch.load(
            self.checkpoint_path, map_location="cpu", weights_only=True
        )
        evidence = checkpoint["evidence"]
        model = NeuralRiskModel(evidence["configuration"]["hidden_width"])
        model.load_state_dict(checkpoint["model_state"])
        model.eval()
        self.trained = TrainedModel(
            model=model,
            means=checkpoint["means"],
            scales=checkpoint["scales"],
            evidence=evidence,
        )
        return True

    def train(self, request: TrainRequest) -> dict[str, Any]:
        if self.store.latest_phase1() is None:
            raise ValueError("Import passed Phase 1 evidence before training")
        config = TrainingConfig(
            seed=request.seed,
            epochs=request.epochs,
            learning_rate=request.learning_rate,
            hidden_width=request.hidden_width,
            patience=request.patience,
        )
        try:
            trained = train_model(config)
        except RuntimeError:
            self.failure_observed = True
            self.recovered_after_failure = False
            raise
        self.artifact_dir.mkdir(parents=True, exist_ok=True)
        checkpoint = self.checkpoint_path
        torch.save(
            {
                "model_state": trained.model.state_dict(),
                "means": trained.means,
                "scales": trained.scales,
                "evidence": trained.evidence,
            },
            checkpoint,
        )
        self.trained = trained
        if self.failure_observed:
            self.recovered_after_failure = True
        self.prediction_made = False
        self.last_prediction = request.prediction
        run_id = self.store.save_run(trained.evidence)
        return {"run_id": run_id, "checkpoint": str(checkpoint), **trained.evidence}


def create_app(store: Any | None = None, artifact_dir: str | Path | None = None) -> FastAPI:
    selected_store = store or PostgresStore()
    selected_artifact_dir = artifact_dir or os.environ.get(
        "PHASE2_ARTIFACT_DIR", "/artifacts/phase2"
    )
    service = Phase2Service(selected_store, selected_artifact_dir)

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        selected_store.initialize()
        service.restore_checkpoint()
        yield

    app = FastAPI(title="Learn AI Phase 2 Lab", version="1.0", lifespan=lifespan)
    app.state.phase2 = service

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "phase2-api"}

    @app.get("/api/phase2/status")
    def status() -> dict[str, Any]:
        imported = selected_store.latest_phase1()
        return {
            "schema_version": "1.0",
            "phase1_imported": imported is not None,
            "phase1_evidence_id": imported["id"] if imported else None,
            "model_ready": service.trained is not None,
            "failure_observed": service.failure_observed,
            "recovered_after_failure": service.recovered_after_failure,
            "prediction_made": service.prediction_made,
            "feature_order": list(FEATURE_ORDER),
            "current_model": service.trained.evidence if service.trained else None,
            "runs": selected_store.list_runs(),
        }

    @app.post("/api/phase2/phase1")
    def import_phase1(artifact: dict[str, Any]) -> dict[str, Any]:
        try:
            validated = validate_phase1_artifact(artifact)
            identifier = selected_store.save_phase1(validated)
        except ValueError as error:
            raise HTTPException(status_code=422, detail=str(error)) from error
        return {"imported": True, "phase1_evidence_id": identifier}

    @app.post("/api/phase2/train")
    def train(request: TrainRequest) -> dict[str, Any]:
        try:
            return service.train(request)
        except (ValueError, RuntimeError) as error:
            raise HTTPException(
                status_code=422,
                detail={"failure_signal": str(error), "checkpoint_promoted": False},
            ) from error

    @app.post("/api/phase2/predict")
    def score(request: PredictionRequest) -> dict[str, Any]:
        if service.trained is None:
            raise HTTPException(status_code=409, detail="Train and promote a model first")
        result = predict(service.trained, request.model_dump())
        service.prediction_made = True
        return result

    @app.post("/api/phase2/artifact")
    def artifact(request: ArtifactRequest) -> dict[str, Any]:
        if service.trained is None:
            raise HTTPException(status_code=409, detail="Train and promote a model first")
        if not service.trained.evidence["acceptance"]["passed"]:
            raise HTTPException(status_code=409, detail="The model has not passed every numeric gate")
        if not service.failure_observed:
            raise HTTPException(status_code=409, detail="Observe the controlled failure before creating the artifact")
        if not service.recovered_after_failure:
            raise HTTPException(status_code=409, detail="Recover with a passing run after the controlled failure")
        if not service.prediction_made:
            raise HTTPException(status_code=409, detail="Score a new project before creating the artifact")
        phase1 = selected_store.latest_phase1()
        attempt = selected_store.next_attempt()
        try:
            value = build_artifact(
                attempt_number=attempt,
                phase1_evidence_id=phase1["id"],
                prediction=service.last_prediction,
                configuration=service.trained.evidence["configuration"],
                result=service.trained.evidence,
                reasoning=request.model_dump(),
            )
        except ValueError as error:
            raise HTTPException(status_code=422, detail=str(error)) from error
        selected_store.save_artifact(value)
        return {"filename": artifact_filename(attempt), "artifact": value}

    return app


app = create_app()
