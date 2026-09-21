from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from labs.phase2.api.main import create_app
from labs.phase2.api.store import MemoryStore


ROOT = Path(__file__).parents[3]


def passed_phase1() -> dict:
    return {
        "schema_version": "1.0",
        "project_id": "phase1-model-investigation",
        "attempt_number": 2,
        "evaluation": {"passed": True},
    }


def valid_reasoning() -> dict[str, str]:
    return {
        "observation": "Northstar validation loss reached its minimum before the final epoch because the selected checkpoint preserved stronger evidence. Test recall and accuracy also exceeded the recorded majority baseline gate.",
        "failure_diagnosis": "Northstar training became unstable because the excessive learning rate made loss explode before a safe checkpoint could be promoted. The visible failure signal stopped the run and protected the previous model.",
        "recovery": "Northstar recovered because I restored the learning rate while holding the seed and architecture constant. The stable controlled run reproduced the selected checkpoint and passed every acceptance gate.",
        "promotion_rationale": "I would promote the Northstar checkpoint because recall and accuracy passed their release gates against the majority baseline. Validation selected an earlier epoch while sealed test evidence remained protected.",
        "limitation": "Northstar uses synthetic samples, so these metrics may not generalize to real customer populations or shifted subgroups. We should collect representative projects, validate calibration and fairness, then monitor drift.",
    }


def test_health_status_and_phase1_import(tmp_path):
    app = create_app(MemoryStore(), tmp_path)
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok", "service": "phase2-api"}
        assert client.get("/api/phase2/status").json()["phase1_imported"] is False
        imported = client.post("/api/phase2/phase1", json=passed_phase1())
        assert imported.status_code == 200
        status = client.get("/api/phase2/status").json()
        assert status["phase1_imported"] is True
        assert status["phase1_evidence_id"] == "phase1-attempt-2"


def test_phase1_import_rejects_incompatible_or_failed_evidence(tmp_path):
    app = create_app(MemoryStore(), tmp_path)
    with TestClient(app) as client:
        stale = client.post("/api/phase2/phase1", json={**passed_phase1(), "schema_version": "0.9"})
        failed = client.post("/api/phase2/phase1", json={**passed_phase1(), "evaluation": {"passed": False}})
    assert stale.status_code == 422
    assert failed.status_code == 422


def test_full_walkthrough_requires_failure_and_emits_a_valid_artifact(tmp_path):
    store = MemoryStore()
    app = create_app(store, tmp_path)
    reasoning = valid_reasoning()
    with TestClient(app) as client:
        assert client.post("/api/phase2/phase1", json=passed_phase1()).status_code == 200
        trained = client.post(
            "/api/phase2/train",
            json={
                "prediction": "I expect validation to select a checkpoint before epoch 300.",
                "seed": 17,
                "epochs": 300,
                "learning_rate": 0.05,
                "hidden_width": 12,
                "patience": 30,
            },
        )
        assert trained.status_code == 200
        assert trained.json()["acceptance"]["passed"] is True
        assert client.post("/api/phase2/artifact", json=reasoning).status_code == 409

        failed = client.post(
            "/api/phase2/train",
            json={
                "prediction": "I expect the explosive learning rate to fail closed immediately.",
                "seed": 17,
                "epochs": 40,
                "learning_rate": 1_000_000,
                "hidden_width": 12,
                "patience": 10,
            },
        )
        assert failed.status_code == 422
        assert client.post("/api/phase2/artifact", json=reasoning).status_code == 409
        recovered = client.post(
            "/api/phase2/train",
            json={
                "prediction": "I expect the recovered model to reproduce the known-good evidence.",
                "seed": 17,
                "epochs": 300,
                "learning_rate": 0.05,
                "hidden_width": 12,
                "patience": 30,
            },
        )
        assert recovered.status_code == 200
        assert client.post("/api/phase2/artifact", json=reasoning).status_code == 409
        prediction = client.post(
            "/api/phase2/predict",
            json={
                "planned_integrations": 7,
                "document_count": 4_500,
                "deadline_days": 45,
                "customer_tier": 2,
                "prior_projects": 4,
            },
        )
        assert prediction.status_code == 200
        artifact_response = client.post("/api/phase2/artifact", json=reasoning)

    assert artifact_response.status_code == 200
    body = artifact_response.json()
    assert body["filename"] == "phase2-neural-risk-attempt-01.json"
    schema = json.loads(
        (ROOT / "schemas/phase2-lab-artifact.schema.json").read_text(encoding="utf-8")
    )
    jsonschema.Draft202012Validator(schema).validate(body["artifact"])


def test_reasoning_gate_rejects_repeated_or_semantically_empty_text():
    from labs.phase2.api.contract import validate_reasoning

    repeated = {field: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" for field in valid_reasoning()}
    with pytest.raises(ValueError, match="distinct words"):
        validate_reasoning(repeated)

    filler = {
        field: "Northstar alpha beta gamma delta epsilon because zeta eta theta iota. Kappa lambda mu nu xi omicron pi rho sigma tau upsilon."
        for field in valid_reasoning()
    }
    with pytest.raises(ValueError, match="concepts for"):
        validate_reasoning(filler)


def test_reasoning_gate_accepts_case_specific_explanations():
    from labs.phase2.api.contract import validate_reasoning

    assert validate_reasoning(valid_reasoning()) == valid_reasoning()


def test_checkpoint_is_restored_after_an_api_restart(tmp_path):
    first = create_app(MemoryStore(), tmp_path)
    with TestClient(first) as client:
        client.post("/api/phase2/phase1", json=passed_phase1())
        response = client.post(
            "/api/phase2/train",
            json={
                "prediction": "I expect a reproducible checkpoint to survive an API restart.",
                "epochs": 300,
                "learning_rate": 0.05,
                "hidden_width": 12,
                "patience": 30,
            },
        )
        assert response.status_code == 200

    restarted = create_app(MemoryStore(), tmp_path)
    with TestClient(restarted) as client:
        assert client.get("/api/phase2/status").json()["model_ready"] is True
