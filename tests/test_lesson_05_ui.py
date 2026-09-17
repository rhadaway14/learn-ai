from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "05_regression_and_classification"


def test_lesson_05_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_05_learner_material_is_no_code() -> None:
    for filename in ("README.md", "EXERCISES.md", "SOLUTIONS.md", "index.html"):
        material = (LESSON / filename).read_text(encoding="utf-8").lower()
        assert "```python" not in material
        assert "python lessons/" not in material
    html = (LESSON / "index.html").read_text(encoding="utf-8").lower()
    assert "lab.py" not in html


def test_lesson_05_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "readinessFeedback",
        "regressionChart",
        "trainMae",
        "testMae",
        "testRmse",
        "testR2",
        "classificationThreshold",
        "falsePositiveCost",
        "falseNegativeCost",
        "scoreRows",
        "tpCount",
        "fpCount",
        "fnCount",
        "tnCount",
        "precisionValue",
        "recallValue",
        "costValue",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_05_teaches_modeling_metrics_and_failures() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "Supervised learning learns from examples with known answers",
        "The prediction-time rule",
        "The target determines whether the task is regression or classification",
        "Compare a baseline, a useful trend, and an overfit curve",
        "A confusion matrix names all four classification outcomes",
        "The accuracy trap",
        "The threshold is where model evidence becomes a product decision",
        "Leakage lets the model peek at an answer",
        "ROC and precision–recall curves compare thresholds",
        "Gate A capstone: baseline decision model and evaluation worksheet",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 5
    assert html.count('class="quiz"') >= 8


def test_lesson_05_reading_explains_metrics_before_compressing_them() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8")
    for concept in (
        "MAE asks:",
        "RMSE asks:",
        "R² asks:",
        "Precision asks:",
        "Recall asks:",
        "Expected error cost",
        "ROC AUC summarizes",
        "Match the split to production",
        "Leakage makes validation fiction",
    ):
        assert concept in readme


def test_lesson_05_completes_foundation_gate_a() -> None:
    exercises = (LESSON / "EXERCISES.md").read_text(encoding="utf-8")
    capstone = (ROOT / "CAPSTONE_PATH.md").read_text(encoding="utf-8")
    assert "Gate A capstone worksheet" in exercises
    assert "Baseline and evaluation contract" in exercises
    assert "detect obvious leakage" in capstone


def test_course_dashboard_opens_lesson_05_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=9" in script
    assert "requestedLesson<=9" in script
    assert '"05_regression_and_classification"' in script
