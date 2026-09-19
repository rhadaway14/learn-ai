from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


SCHEMA_VERSION = "1.0"
ARTIFACT_TYPE = "phase2-neural-risk"
PHASE1_PROJECT_ID = "phase1-model-investigation"


def validate_phase1_artifact(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("Phase 1 evidence must be a JSON object")
    if value.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Phase 1 evidence must use schema version 1.0")
    if value.get("project_id") != PHASE1_PROJECT_ID:
        raise ValueError("Phase 1 evidence has an unexpected project id")
    attempt = value.get("attempt_number")
    if not isinstance(attempt, int) or isinstance(attempt, bool) or attempt < 1:
        raise ValueError("Phase 1 evidence must contain a positive attempt number")
    evaluation = value.get("evaluation")
    if not isinstance(evaluation, dict) or evaluation.get("passed") is not True:
        raise ValueError("Phase 1 evidence must record a passed assessment")
    return value


def validate_reasoning(value: Any) -> dict[str, str]:
    fields = (
        "observation",
        "failure_diagnosis",
        "recovery",
        "promotion_rationale",
        "limitation",
    )
    if not isinstance(value, dict):
        raise ValueError("reasoning must be an object")
    result: dict[str, str] = {}
    for field in fields:
        text = str(value.get(field, "")).strip()
        if len(text) < 20:
            raise ValueError(f"reasoning.{field} must contain at least 20 characters")
        result[field] = text
    return result


def build_artifact(
    *,
    attempt_number: int,
    phase1_evidence_id: str,
    prediction: str,
    configuration: dict[str, Any],
    result: dict[str, Any],
    reasoning: dict[str, str],
) -> dict[str, Any]:
    if not isinstance(attempt_number, int) or isinstance(attempt_number, bool) or attempt_number < 1:
        raise ValueError("attempt_number must be a positive integer")
    prediction = prediction.strip()
    if len(prediction) < 20:
        raise ValueError("prediction must contain at least 20 characters")
    return {
        "schema_version": SCHEMA_VERSION,
        "artifact_type": ARTIFACT_TYPE,
        "attempt_number": attempt_number,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "phase1_evidence_id": phase1_evidence_id,
        "prediction": prediction,
        "configuration": configuration,
        "baseline": result["baseline"],
        "training": result["training"],
        "sealed_test": result["sealed_test"],
        "acceptance": result["acceptance"],
        "reasoning": validate_reasoning(reasoning),
    }


def artifact_filename(attempt_number: int) -> str:
    if not isinstance(attempt_number, int) or isinstance(attempt_number, bool) or attempt_number < 1:
        raise ValueError("attempt number must be positive")
    return f"phase2-neural-risk-attempt-{attempt_number:02d}.json"
