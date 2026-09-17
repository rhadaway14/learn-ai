from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "10_regularization_and_generalization"


def test_lesson_10_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_10_learner_material_is_no_code() -> None:
    for filename in ("README.md", "EXERCISES.md", "SOLUTIONS.md", "index.html"):
        material = (LESSON / filename).read_text(encoding="utf-8").lower()
        assert "```python" not in material
        assert "python lessons/" not in material
    assert "lab.py" not in (LESSON / "index.html").read_text(encoding="utf-8").lower()


def test_lesson_10_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "readinessFeedback",
        "capacity",
        "evidence",
        "noise",
        "regularization",
        "fitChart",
        "fitTrainError",
        "fitValidationError",
        "learningCurveChart",
        "curveAction",
        "penaltyStrength",
        "weightBars",
        "nonzeroWeights",
        "dropRate",
        "runDropout",
        "dropoutUnits",
        "augmentationCards",
        "augmentationReviewed",
        "distanceSpread",
        "delaySpread",
        "standardizedValues",
        "strategyTrain",
        "strategyValidation",
        "strategyGap",
        "strategyData",
        "diagnoseStrategy",
        "strategyResult",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_10_teaches_generalization_mechanisms_and_diagnosis() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "Generalization is the goal; regularization is one set of tools",
        "Capacity, evidence, noise, and regularization interact",
        "Learning curves ask whether more data is likely to help",
        "Weight penalties trade fit for simpler parameter values",
        "Dropout trains many temporary subnetworks",
        "Data augmentation encodes invariances—not arbitrary distortion",
        "Normalization and regularization solve different problems",
        "Choose the control from evidence, not habit",
        "Capstone increment: generalization stress-test and control plan",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 3
    assert html.count('class="quiz"') >= 8


def test_lesson_10_reading_contains_complete_regularization_framework() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8")
    for concept in (
        "Generalization is observed behavior",
        "Underfitting and overfitting",
        "Bias and variance are diagnostic tendencies",
        "Capacity must be interpreted relative to evidence",
        "Learning curves separate several hypotheses",
        "The regularized objective",
        "L2 regularization",
        "L1 regularization",
        "Dropout changes the training network temporarily",
        "Data augmentation encodes invariance",
        "Early stopping is implicit regularization",
        "Normalization is not one thing",
        "Design controlled regularization experiments",
        "Connection to modern AI",
        "Phase 2 milestone",
    ):
        assert concept in readme


def test_lesson_10_exercises_include_math_diagnosis_and_capstone() -> None:
    exercises = (LESSON / "EXERCISES.md").read_text(encoding="utf-8")
    for concept in (
        "Diagnose the evidence",
        "Capacity–evidence matrix",
        "Learning-curve diagnosis",
        "Regularized-objective calculations",
        "Parameter-group policy",
        "Dropout reasoning",
        "Augmentation policy",
        "Normalization distinctions",
        "Ablation plan",
        "generalization stress-test and control plan",
    ):
        assert concept in exercises


def test_course_dashboard_opens_lesson_10_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=10" in script
    assert "requestedLesson<=10" in script
    assert '"10_regularization_and_generalization"' in script
