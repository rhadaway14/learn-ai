from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSON = ROOT / "lessons" / "02_vectors_matrices_tensors"


def test_lesson_02_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert '<script src="../progress.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_02_learner_material_is_no_code() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8").lower()
    html = (LESSON / "index.html").read_text(encoding="utf-8").lower()
    assert "```python" not in readme
    assert "train.py" not in html
    assert "python " not in html


def test_lesson_02_has_required_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for interaction in (
        "objectVisual",
        "vectorScale",
        "magnitudeChart",
        "dotControls",
        "shapeResult",
        "matrixC",
        "transposeButton",
        "animateBroadcast",
        "embeddingChart",
        "transformerShape",
        "completeLesson",
    ):
        assert f'id="{interaction}"' in html


def test_lesson_02_explains_tokens_tensor_layers_and_operation_relevance() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    script = (LESSON / "app.js").read_text(encoding="utf-8")
    for concept in (
        "A token is a piece of input assigned a vocabulary ID",
        "Why addition matters in AI",
        "Why magnitude matters in AI",
        "Why one score is useful",
        "What “transformation” means here",
    ):
        assert concept in html
    assert 'id="objectAxisKey"' in html
    assert 'class="tensor-layer"' in script
    assert "token positions per sequence" in script


def test_course_dashboard_tracks_all_lessons() -> None:
    html = (ROOT / "course.html").read_text(encoding="utf-8")
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    progress = (ROOT / "lessons" / "progress.js").read_text(encoding="utf-8")
    assert 'id="completedCount"' in html
    assert 'id="coursePhases"' in html
    assert 'id="lessonViewer"' in html
    assert script.count('"01_linear_regression"') == 1
    assert '"35_capstone_production_grade_agentic_ai_platform"' in script
    assert "course.html?lesson=" in script
    assert "learn-ai-progress-state" in script
    assert "localStorage" in progress
    assert "postMessage" in progress
    assert "complete" in progress
