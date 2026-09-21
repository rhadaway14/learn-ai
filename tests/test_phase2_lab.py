from __future__ import annotations

import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).parents[1]
LAB = ROOT / "labs/phase2"


def test_phase2_spec_has_bounded_contract_and_numeric_gate():
    spec = (LAB / "SPEC.md").read_text(encoding="utf-8")
    for requirement in (
        "Phase 1 remains a zero-install browser experience",
        "sealed-test recall is at least `0.25`",
        "majority-class accuracy plus `0.03`",
        "selected checkpoint epoch is earlier",
        "sealed test is evaluated exactly once",
        "Reasoning gate",
        "Accessibility contract",
        "Out of scope for the pilot",
        "seeded Gaussian noise (`σ = 0.6`)",
        "at least 18 distinct words",
        "uncalibrated model risk `score`",
    ):
        assert requirement in spec


def test_phase2_compose_profile_has_only_the_required_pilot_services():
    compose = (ROOT / "compose.yaml").read_text(encoding="utf-8")
    for service in ("phase2-web:", "phase2-api:", "phase2-db:"):
        assert service in compose
    for excluded in ("phase2-redis:", "phase2-minio:", "phase2-grafana:"):
        assert excluded not in compose
    assert 'profiles: ["phase2"]' in compose
    assert '"8090:80"' in compose
    assert '"8091:8080"' in compose


def test_phase2_artifact_schema_is_valid_and_encodes_the_gate():
    schema = json.loads((ROOT / "schemas/phase2-lab-artifact.schema.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    assert schema["properties"]["schema_version"]["const"] == "1.0"
    assert schema["properties"]["attempt_number"]["minimum"] == 1
    assert schema["properties"]["sealed_test"]["allOf"][1]["properties"]["evaluations"]["const"] == 1


def test_phase2_ui_exposes_the_complete_guided_loop_and_accessible_evidence():
    html = (LAB / "web/index.html").read_text(encoding="utf-8")
    css = (LAB / "web/styles.css").read_text(encoding="utf-8")
    script = (LAB / "web/app.js").read_text(encoding="utf-8")
    for identifier in (
        "checkStack",
        "phase1File",
        "trainingPrediction",
        "trainModel",
        "trainingChart",
        "historyTable",
        "runFailure",
        "recoverModel",
        "predictionForm",
        "createArtifact",
        "downloadArtifact",
    ):
        assert f'id="{identifier}"' in html
    assert 'aria-live="polite"' in html
    assert 'role="img"' in html
    assert html.count("<caption>") >= 2
    assert "prefers-reduced-motion" in css
    assert "header .eyebrow{color:#d6e2ff}" in css
    assert "Phase 1 evidence" in html
    assert "drawHistory" in script and "acceptanceChecks" in script
    assert "model risk score" in script and "real-world probability" in script


def test_phase2_lifecycle_and_generated_artifacts_are_explicit():
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    readme = (LAB / "README.md").read_text(encoding="utf-8")
    for command in ("phase2-start", "phase2-status", "phase2-test", "phase2-reset", "phase2-clean"):
        assert f"{command}:" in makefile
        assert command in readme
    assert "artifacts/" in ignore


def test_phase2_lab_is_linked_from_the_course_dashboard():
    course = (ROOT / "course.js").read_text(encoding="utf-8")
    assert 'href="labs/phase2/index.html"' in course
    assert "PHASE 2 CUMULATIVE LAB" in course
