import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSONS = {
    4: ("04_probability_and_statistics_for_ml", "P1-I04"),
    5: ("05_regression_and_classification", "P1-I05"),
    6: ("06_neural_network_anatomy", "P2-I01"),
    7: ("07_backpropagation_from_scratch", "P2-I02"),
    8: ("08_pytorch_and_autograd", "P2-I03"),
    9: ("09_train_and_evaluate_a_neural_network", "P2-I04"),
    10: ("10_regularization_and_generalization", "P2-I05"),
}


def test_lessons_04_10_implement_the_full_lesson_contract():
    for lesson, (directory, increment) in LESSONS.items():
        html = (ROOT / "lessons" / directory / "index.html").read_text(encoding="utf-8")
        for marker in ("learning-lanes", 'id="ai-story"', "advanced-section", "hands-on-activity", "phase-increment"):
            assert marker in html, f"Lesson {lesson} missing {marker}"
        assert f'data-activity-id="L{lesson:02d}-A1"' in html
        assert f'data-increment-id="{increment}"' in html
        assert "no coding" in html.lower()
        assert "Engineer extension · optional" in html


def test_activity_and_increment_records_are_connected():
    for lesson, (_, increment_id) in LESSONS.items():
        activity_id = f"L{lesson:02d}-A1"
        activity = json.loads((ROOT / "activities" / f"{activity_id}.json").read_text(encoding="utf-8"))
        phase = int(increment_id[1])
        increment = json.loads((ROOT / "phase-projects" / f"phase{phase}" / f"{increment_id}.json").read_text(encoding="utf-8"))
        assert activity["activity_id"] == activity_id
        assert activity["lesson"] == lesson
        assert activity["phase_increment"] == increment_id
        assert set(activity["levels"]) == {"guided", "challenge", "engineer_extension"}
        assert activity["levels"]["engineer_extension"]["optional"] is True
        assert increment["increment_id"] == increment_id
        assert increment["lesson"] == lesson
        assert f"activities/{activity_id}.json" in increment["upstream_evidence"]
        assert len(increment["acceptance_criteria"]) >= 3


def test_phase_one_project_is_browser_first_and_assesses_release_reasoning():
    html = (ROOT / "projects/phase1/index.html").read_text(encoding="utf-8")
    app = (ROOT / "projects/phase1/app.js").read_text(encoding="utf-8")
    assert html.count("data-question=") == 7
    assert html.count('data-critical="true"') == 2
    assert html.count("data-feedback=") == 21
    for evidence in ("normal_case", "failure_case", "limitations"):
        assert f'name="{evidence}"' in html
    assert "no coding required" in html.lower()
    assert "PhaseOneAssessment.evaluate" in app
    assert "phase1-model-investigation.json" in app
    assert "localStorage" in app
