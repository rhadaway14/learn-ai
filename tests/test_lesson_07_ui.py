from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "07_backpropagation_from_scratch"


def test_lesson_07_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_07_learner_material_is_no_code() -> None:
    for filename in ("README.md", "EXERCISES.md", "SOLUTIONS.md", "index.html"):
        material = (LESSON / filename).read_text(encoding="utf-8").lower()
        assert "```python" not in material
        assert "python lessons/" not in material
    assert "lab.py" not in (LESSON / "index.html").read_text(encoding="utf-8").lower()


def test_lesson_07_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "readinessFeedback",
        "graphX",
        "graphW",
        "graphB",
        "nodeM",
        "nodeP",
        "nodeY",
        "gradX",
        "gradW",
        "gradB",
        "nextTrace",
        "traceCalculation",
        "chainX",
        "totalChain",
        "gateZ",
        "upstreamGradient",
        "gateActivation",
        "gateDownstream",
        "branchX",
        "branchTotal",
        "backwardButton",
        "zeroButton",
        "stepButton",
        "gradientBuffer",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_07_teaches_backpropagation_mechanisms_and_failures() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in (
        "A forward pass produces a prediction; backpropagation assigns responsibility",
        "A computational graph records values and dependencies",
        "The chain rule multiplies sensitivity along a path",
        "Every operation acts like a local gradient gate",
        "Gradients multiply along paths and add across paths",
        "Reverse-mode differentiation fits one loss and many parameters",
        "Gradient buffers are state and must be managed deliberately",
        "Stop-gradient deliberately cuts a backward path",
        "Capstone increment: manual backward-pass and gradient-state contract",
    ):
        assert concept in html
    assert html.count('class="metaphor"') >= 3
    assert html.count('class="quiz"') >= 8


def test_lesson_07_reading_contains_complete_manual_trace() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8")
    for concept in (
        "A derivative answers a local “what if?” question",
        "Complete forward pass",
        "Backward pass starts by seeding the scalar loss",
        "The completed leaf gradients",
        "Gradients add when a value has multiple paths",
        "Reverse-mode differentiation fits neural-network training",
        "Tensor gradients match the tensors they describe",
        "Zeroing and optimizer order",
        "Verify gradients with finite differences",
        "Vanishing and exploding gradients",
    ):
        assert concept in readme
    for expected in ("42", "28", "14"):
        assert expected in readme


def test_lesson_07_capstone_prepares_autograd_comparison() -> None:
    exercises = (LESSON / "EXERCISES.md").read_text(encoding="utf-8")
    assert "Backward-pass and gradient-state contract" in exercises
    assert "Forward graph" in exercises
    assert "Backward graph" in exercises
    assert "centered finite-difference estimate" in exercises


def test_course_dashboard_opens_lesson_07_interactively() -> None:
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert "number<=9" in script
    assert "requestedLesson<=9" in script
    assert '"07_backpropagation_from_scratch"' in script
