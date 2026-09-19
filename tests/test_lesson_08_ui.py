from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "08_pytorch_and_autograd"


def test_lesson_08_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_08_learner_material_is_no_code() -> None:
    for filename in ("README.md", "EXERCISES.md", "SOLUTIONS.md", "index.html"):
        material = (LESSON / filename).read_text(encoding="utf-8").lower()
        assert "```python" not in material
        assert "python lessons/" not in material
    assert "lab.py" not in (LESSON / "index.html").read_text(encoding="utf-8").lower()


def test_lesson_08_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "readinessFeedback",
        "tensorBatch",
        "tensorWidth",
        "tensorDtype",
        "tensorDevice",
        "tensorGrad",
        "tensorMemory",
        "trackX",
        "trackW",
        "trackB",
        "noGradMode",
        "autogradGraph",
        "availableGradients",
        "moduleTree",
        "selectedParameters",
        "loopStages",
        "nextLoopStage",
        "loopGradient",
        "runModePass",
        "modeOutputs",
        "checkpointItems",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_08_teaches_framework_state_and_failures() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "PyTorch turns the mechanics from Lessons 2–7 into managed runtime state",
        "A tensor carries values plus execution metadata",
        "Autograd records a graph while differentiable operations run",
        "A module is a registered tree of model state and behavior",
        "The training loop is an ordered state machine",
        "Training and evaluation modes change selected layer behavior",
        "A checkpoint is a versioned state package—not the whole application",
        "Capstone increment: PyTorch execution and state contract",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 3
    assert html.count('class="quiz"') >= 8


def test_lesson_08_reading_contains_runtime_details_and_code_boundary() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8")
    for concept in (
        "A tensor is more than an array of numbers",
        "Estimate tensor value memory",
        "Autograd records differentiable operations dynamically",
        "Leaves and non-leaves",
        "A module is a registered component tree",
        "The canonical batch lifecycle",
        "Mode and gradient context are independent",
        "Checkpoint contents depend on restoration goal",
        "Code-readiness boundary",
    ):
        assert concept in readme


def test_lesson_08_capstone_prepares_lesson_09_implementation() -> None:
    exercises = (LESSON / "EXERCISES.md").read_text(encoding="utf-8")
    assert "PyTorch execution and state contract" in exercises
    assert "Tensor inventory" in exercises
    assert "Module-state inventory" in exercises
    assert "Execution-mode matrix" in exercises
    assert "Validation gates" in exercises


def test_autograd_flow_stacks_without_horizontal_overflow_on_mobile() -> None:
    css = (LESSON / "styles.css").read_text(encoding="utf-8")
    mobile = css[css.index("@media(max-width:720px)") :]
    assert ".autograd-flow{display:grid" in mobile
    assert "grid-template-columns:minmax(0,1fr)" in mobile
    assert ".autograd-flow article{min-width:0;width:100%}" in mobile
    assert ".autograd-flow i{text-align:center;transform:rotate(90deg)}" in mobile


def test_course_dashboard_opens_lesson_08_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=10" in script
    assert "requestedLesson<=10" in script
    assert '"08_pytorch_and_autograd"' in script
