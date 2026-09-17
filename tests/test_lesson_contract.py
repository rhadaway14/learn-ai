import json
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_reusable_lesson_contract_defines_both_depths_and_continuity():
    contract = (ROOT / "LESSON_CONTRACT.md").read_text(encoding="utf-8")
    for required in (
        "Core path",
        "Advanced engineering",
        "AI story",
        "Hands-on activity",
        "Phase-project increment",
        "guided to challenge",
        "Docker Compose",
    ):
        assert required.lower() in contract.lower()


def test_shared_components_support_contract_markup():
    css = (ROOT / "lessons/lesson-components.css").read_text(encoding="utf-8")
    script = (ROOT / "lessons/lesson-ui.js").read_text(encoding="utf-8")
    accessibility = (ROOT / "lessons/accessibility.css").read_text(encoding="utf-8")
    for component in (".learning-lanes", ".ai-story", ".advanced-section", ".hands-on-activity", ".phase-increment"):
        assert component in css
    assert "lesson-components.css" in accessibility
    assert 'aria-current","step"' in script
    assert "Optional advanced material" in script
    assert "Activity level" in script


def test_artifact_schemas_are_valid_json_and_require_evidence_contracts():
    activity = json.loads((ROOT / "schemas/lesson-activity.schema.json").read_text(encoding="utf-8"))
    increment = json.loads((ROOT / "schemas/phase-project-increment.schema.json").read_text(encoding="utf-8"))
    assert activity["$schema"].endswith("2020-12/schema")
    assert increment["$schema"].endswith("2020-12/schema")
    for field in ("levels", "evidence", "artifact", "acceptance_criteria", "recovery", "phase_increment"):
        assert field in activity["required"]
    assert set(activity["properties"]["levels"]["required"]) == {"guided", "challenge", "engineer_extension"}
    for field in ("upstream_evidence", "contract", "acceptance_criteria", "failure_behavior", "verification", "downstream_consumer", "decision"):
        assert field in increment["required"]


def test_learner_templates_and_phase_map_are_connected():
    activity = (ROOT / "templates/lesson-activity.md").read_text(encoding="utf-8")
    increment = (ROOT / "templates/phase-project-increment.md").read_text(encoding="utf-8")
    phases = (ROOT / "PHASE_PROJECTS.md").read_text(encoding="utf-8")
    assert "Level 1 — Guided" in activity
    assert "Level 2 — Challenge" in activity
    assert "Engineer extension" in activity
    assert "Failure experiment" in activity
    assert "Downstream consumer" in increment
    assert "Failure behavior" in increment
    for phase in range(1, 7):
        assert f"Phase {phase}" in phases
    assert "P1-I01" in phases and "P6-I05" in phases
