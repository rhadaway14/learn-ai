from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "06_neural_network_anatomy"


def test_lesson_06_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_06_learner_material_is_no_code() -> None:
    for filename in ("README.md", "EXERCISES.md", "SOLUTIONS.md", "index.html"):
        material = (LESSON / filename).read_text(encoding="utf-8").lower()
        assert "```python" not in material
        assert "python lessons/" not in material
    assert "lab.py" not in (LESSON / "index.html").read_text(encoding="utf-8").lower()


def test_lesson_06_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "readinessFeedback",
        "x1",
        "w1",
        "x2",
        "w2",
        "neuronBias",
        "neuronActivation",
        "zValue",
        "activationValue",
        "batchSize",
        "inputWidth",
        "outputWidth",
        "layerParameterCount",
        "activationInput",
        "activationChart",
        "xorChart",
        "xorTable",
        "networkBatch",
        "hidden1",
        "hidden2",
        "networkParameterCount",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_06_teaches_mechanisms_examples_and_failures() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "Neural networks learn intermediate representations",
        "A neuron computes a weighted sum, adds a bias, then activates",
        "A dense layer runs many neurons in parallel",
        "Activation functions decide how a neuron responds",
        "Without nonlinear activations, depth collapses into one linear map",
        "Separate the XOR pattern",
        "Width, depth, and parameter count shape model capacity",
        "The output layer must match the task",
        "Capstone increment: neural architecture and tensor-shape contract",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 5
    assert html.count('class="quiz"') >= 8


def test_lesson_06_reading_has_complete_shape_and_parameter_trace() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8")
    for concept in (
        "Fully worked example",
        "Dense-layer shape tracing",
        "Framework convention warning",
        "Why nonlinear activations are essential",
        "XOR as a small example",
        "Full shape trace: 10 → 64 → 16 → 3",
        "1,795",
        "The output head must match the task",
        "Important failure modes and diagnostics",
    ):
        assert concept in readme


def test_lesson_06_capstone_prepares_later_model_mechanics() -> None:
    exercises = (LESSON / "EXERCISES.md").read_text(encoding="utf-8")
    assert "Neural architecture and tensor-shape contract" in exercises
    assert "Do not implement the network yet" in exercises
    assert "Primary held-out metric" in exercises
    assert "Trace every layer" in exercises


def test_course_dashboard_opens_lesson_06_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=10" in script
    assert "requestedLesson<=10" in script
    assert '"06_neural_network_anatomy"' in script
