from __future__ import annotations

from datetime import datetime, timezone
import re
from typing import Any


SCHEMA_VERSION = "1.0"
ARTIFACT_TYPE = "phase2-neural-risk"
PHASE1_PROJECT_ID = "phase1-model-investigation"
MINIMUM_DISTINCT_WORDS = 18
REASONING_WORDS = {
    "because", "causing", "could", "if", "may", "means", "reveals",
    "so", "therefore", "when", "which", "while", "would",
}
REASONING_RULES = {
    "observation": {
        "evidence": {"accuracy", "checkpoint", "curve", "epoch", "loss", "metric", "recall", "validation"},
        "comparison": {"baseline", "compare", "exceeded", "test", "training"},
    },
    "failure_diagnosis": {
        "cause": {"excessive", "exploded", "gradient", "learning", "loss", "rate", "unstable"},
        "signal": {"checkpoint", "failed", "failure", "protected", "signal", "stopped"},
    },
    "recovery": {
        "control": {"constant", "controlled", "held", "same", "seed", "while"},
        "recovery_evidence": {"checkpoint", "passed", "recovered", "reproduced", "stable"},
    },
    "promotion_rationale": {
        "gate": {"accuracy", "baseline", "checkpoint", "gate", "passed", "recall", "validation"},
        "decision": {"accept", "promote", "promotion", "release"},
    },
    "limitation": {
        "population": {"customer", "population", "real", "sample", "subgroup", "synthetic"},
        "uncertainty": {"calibration", "drift", "fairness", "generalize", "shift", "uncertainty"},
        "response": {"collect", "compare", "monitor", "recalibrate", "review", "segment", "validate"},
    },
}


def _words(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:[-'][a-z0-9]+)*", value.lower())


def _matches_concept(token: str, concept: str) -> bool:
    return token == concept or (len(concept) >= 5 and token.startswith(concept))


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
    if not isinstance(value, dict):
        raise ValueError("reasoning must be an object")
    result: dict[str, str] = {}
    for field, required_groups in REASONING_RULES.items():
        text = str(value.get(field, "")).strip()
        tokens = _words(text)
        distinct_words = len(set(tokens))
        sentence_count = sum(
            len(_words(sentence)) >= 5 for sentence in re.split(r"[.!?]+", text)
        )
        missing_groups = [
            group
            for group, concepts in required_groups.items()
            if not any(
                _matches_concept(token, concept)
                for token in tokens
                for concept in concepts
            )
        ]
        problems = []
        if distinct_words < MINIMUM_DISTINCT_WORDS:
            problems.append(f"at least {MINIMUM_DISTINCT_WORDS} distinct words")
        if sentence_count < 2:
            problems.append("two substantive sentences")
        if "northstar" not in tokens:
            problems.append("Northstar case context")
        if not any(token in REASONING_WORDS for token in tokens):
            problems.append("a causal or conditional reasoning word")
        if missing_groups:
            problems.append("concepts for " + ", ".join(missing_groups))
        if problems:
            raise ValueError(f"reasoning.{field} requires " + "; ".join(problems))
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
