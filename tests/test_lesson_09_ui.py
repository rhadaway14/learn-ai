from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "09_train_and_evaluate_a_neural_network"


def test_lesson_09_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_09_learner_material_is_no_code() -> None:
    for filename in ("README.md", "EXERCISES.md", "SOLUTIONS.md", "index.html"):
        material = (LESSON / filename).read_text(encoding="utf-8").lower()
        assert "```python" not in material
        assert "python lessons/" not in material
    assert "lab.py" not in (LESSON / "index.html").read_text(encoding="utf-8").lower()


def test_lesson_09_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "readinessFeedback",
        "trainShare",
        "validationShare",
        "splitStrategy",
        "duplicateLeak",
        "splitBar",
        "batchSize",
        "epochCount",
        "batchesPerEpoch",
        "totalUpdates",
        "learningRate",
        "trainingSeed",
        "runTraining",
        "trainingChart",
        "bestEpoch",
        "patience",
        "minimumImprovement",
        "stoppingTimeline",
        "confusionMatrix",
        "accuracyMetric",
        "recallMetric",
        "precisionMetric",
        "runOneSeed",
        "runFiveSeeds",
        "seedResults",
        "releaseCheckpoint",
        "evaluateRelease",
        "releaseResult",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_09_teaches_training_evaluation_and_release_boundaries() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "Training creates candidate models; evaluation earns confidence in one",
        "Data splits assign evidence different jobs",
        "Batches organize work; epochs measure coverage",
        "A training dashboard tells a story across time",
        "Early stopping preserves the best validated state",
        "A confusion matrix turns one score into specific mistakes",
        "A seed makes one run repeatable; multiple seeds test robustness",
        "Model selection and final evaluation must remain separate",
        "Capstone increment: training, evaluation, and release protocol",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 3
    assert html.count('class="quiz"') >= 8


def test_lesson_09_reading_contains_complete_experiment_lifecycle() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8")
    for concept in (
        "Define the prediction contract before splitting",
        "Split strategies must match the deployment question",
        "Leakage can occur outside the model",
        "Dataset, batch, step, and epoch",
        "Correct loss aggregation",
        "Validation is an evaluation pass, not a training pass",
        "Read curves as relationships",
        "Early stopping is a state machine",
        "A confusion matrix names the mistakes",
        "Reproducibility, determinism, and robustness differ",
        "Model selection must precede final testing",
        "Evaluation continues after release",
    ):
        assert concept in readme


def test_lesson_09_exercises_include_calculation_diagnosis_and_capstone() -> None:
    exercises = (LESSON / "EXERCISES.md").read_text(encoding="utf-8")
    for concept in (
        "Prediction contract",
        "Batch and epoch calculations",
        "Correct aggregation",
        "Curve diagnosis",
        "Early-stopping trace",
        "Confusion-matrix analysis",
        "Seed evidence",
        "Release-gate review",
        "training, evaluation, and release protocol",
    ):
        assert concept in exercises


def test_course_dashboard_opens_lesson_09_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=10" in script
    assert "requestedLesson<=10" in script
    assert '"09_train_and_evaluate_a_neural_network"' in script
