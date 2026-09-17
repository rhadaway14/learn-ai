import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).parents[1]
API_PATH = ROOT / "labs/foundations/api.py"
SPEC = importlib.util.spec_from_file_location("foundations_api", API_PATH)
assert SPEC and SPEC.loader
API = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = API
SPEC.loader.exec_module(API)


@pytest.mark.parametrize("lesson", [1, 2, 3])
def test_first_three_lessons_implement_the_reference_contract(lesson: int):
    directory = next((ROOT / "lessons").glob(f"{lesson:02d}_*"))
    html = (directory / "index.html").read_text(encoding="utf-8")
    assert 'class="ai-story"' in html
    assert 'class="advanced-section"' in html
    assert 'class="hands-on-activity"' in html
    assert 'class="phase-increment"' in html
    assert f'data-activity-id="L{lesson:02d}-A1"' in html
    assert f'data-increment="P1-I{lesson:02d}"' in html
    assert "Engineer extension" in html
    assert "Reused in:" in html


@pytest.mark.parametrize("lesson", [1, 2, 3])
def test_reference_activity_definitions_are_connected(lesson: int):
    activity = json.loads((ROOT / f"activities/L{lesson:02d}-A1.json").read_text(encoding="utf-8"))
    increment = json.loads((ROOT / f"phase-projects/phase1/P1-I{lesson:02d}.json").read_text(encoding="utf-8"))
    assert activity["lesson"] == lesson
    assert activity["activity_id"] == f"L{lesson:02d}-A1"
    assert activity["phase_increment"] == f"P1-I{lesson:02d}"
    assert set(activity["levels"]) == {"guided", "challenge", "engineer_extension"}
    assert activity["failure_experiment"]["failure_signal"]
    assert activity["artifact"]["path_or_download"]
    assert activity["acceptance_criteria"]
    assert activity["recovery"]
    assert increment["lesson"] == lesson
    assert increment["increment_id"] == activity["phase_increment"]
    assert increment["upstream_evidence"]
    assert increment["downstream_consumer"]
    assert increment["verification"]["expected_evidence"]


def test_foundations_store_persists_validated_experiments(tmp_path: Path):
    store = API.ExperimentStore(tmp_path / "experiments.db")
    experiment = API.Experiment.from_payload(
        {
            "lesson": 2,
            "activity_id": "L02-A1",
            "hypothesis": "Named axes prevent a semantic mismatch.",
            "observation": "The known row exposed the wrong ordering.",
            "conclusion": "Shape compatibility alone is insufficient.",
        }
    )
    created = store.add(experiment)
    rows = store.list()
    assert created["id"] == 1
    assert rows[0]["activity_id"] == "L02-A1"
    assert rows[0]["conclusion"] == "Shape compatibility alone is insufficient."


@pytest.mark.parametrize(
    "payload,error",
    [
        ({"lesson": 4, "activity_id": "L04-A1", "hypothesis": "abc", "observation": "abc", "conclusion": "abc"}, "lesson"),
        ({"lesson": 1, "activity_id": "L03-A1", "hypothesis": "abc", "observation": "abc", "conclusion": "abc"}, "activity_id"),
        ({"lesson": 1, "activity_id": "L01-A1", "hypothesis": "", "observation": "abc", "conclusion": "abc"}, "required"),
    ],
)
def test_foundations_api_rejects_invalid_evidence(payload, error):
    with pytest.raises(ValueError, match=error):
        API.Experiment.from_payload(payload)


def test_foundations_compose_profile_is_optional_and_persistent():
    compose = (ROOT / "compose.yaml").read_text(encoding="utf-8")
    assert compose.count('profiles: ["foundations"]') == 2
    assert "course-ui:" in compose
    assert "foundations-api:" in compose
    assert "foundations-data:/data" in compose
    assert "condition: service_healthy" in compose
    assert '"8080:80"' in compose and '"8081:8080"' in compose
    readme = (ROOT / "labs/foundations/README.md").read_text(encoding="utf-8")
    assert "optional" in readme.lower()
    assert "down --volumes" in readme
    assert "destructive" in readme.lower()
