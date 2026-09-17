from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "04_probability_and_statistics_for_ml"


def test_lesson_04_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_04_learner_material_is_no_code() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8").lower()
    html = (LESSON / "index.html").read_text(encoding="utf-8").lower()
    assert "```python" not in readme
    assert "lab.py" not in html
    assert "python " not in html


def test_lesson_04_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "readinessFeedback",
        "distributionChart",
        "expectedValue",
        "sampleBias",
        "sampleChart",
        "ciRange",
        "prevalence",
        "sensitivity",
        "falsePositive",
        "posteriorValue",
        "forecastProbability",
        "observedOutcomes",
        "calibrationGap",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_04_teaches_uncertainty_with_examples_and_metaphors() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "Probability describes possibilities; statistics learns from observations",
        "Same mean, different uncertainty",
        "More data narrows random uncertainty—but not bias",
        "Use counts before formulas",
        "A confidence interval describes an estimation procedure",
        "Calibration asks whether probabilities match observed frequencies",
        "Correlation is a clue, not proof of causation",
        "Capstone increment: create the uncertainty and sampling worksheet",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 5
    assert html.count('class="quiz"') >= 7


def test_lesson_04_reading_explains_core_statistical_cautions() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8")
    for concept in (
        "Sampling variation",
        "Sampling bias",
        "base-rate fallacy",
        "Bootstrap intervals",
        "Calibration is not the same as",
        "Prediction: “Given what I observe, what is likely next?”",
    ):
        assert concept in readme


def test_course_dashboard_opens_lesson_04_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=10" in script
    assert "requestedLesson<=10" in script
    assert '"04_probability_and_statistics_for_ml"' in script
