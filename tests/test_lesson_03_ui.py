from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "03_loss_functions_and_optimization"


def test_lesson_03_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_03_learner_material_is_no_code() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8").lower()
    html = (LESSON / "index.html").read_text(encoding="utf-8").lower()
    assert "```python" not in readme
    assert "lab.py" not in html
    assert "python " not in html


def test_lesson_03_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "outlierPrediction",
        "lossRows",
        "correctProbability",
        "entropyChart",
        "landscapeWeight",
        "landscapeChart",
        "epsilon",
        "finiteGradient",
        "stepCount",
        "optimizationChart",
        "batchVisual",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_03_teaches_mechanisms_examples_and_failures() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "Loss is not the same as an evaluation metric",
        "Mean Absolute Error",
        "Mean Squared Error",
        "Cross-entropy",
        "hiking downhill in fog",
        "finite-difference estimate",
        "Too small",
        "Too large",
        "Full-batch descent",
        "Mini-batch descent",
        "Capstone increment: define the optimization contract",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 4
    assert html.count('class="quiz"') >= 6


def test_course_dashboard_opens_lesson_03_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=10" in script
    assert "requestedLesson<=10" in script
    assert '"03_loss_functions_and_optimization"' in script
