from pathlib import Path


ROOT = Path(__file__).parents[1]
LESSONS = sorted((ROOT / "lessons").glob("0[1-9]_*/index.html")) + sorted(
    (ROOT / "lessons").glob("10_*/index.html")
)


def test_all_first_ten_lessons_load_shared_accessibility_behavior():
    assert len(LESSONS) == 10
    for path in LESSONS:
        html = path.read_text(encoding="utf-8")
        assert '../accessibility.css' in html
        assert '../lesson-ui.js' in html


def test_shared_ui_covers_ranges_labs_toggle_groups_and_distractors():
    source = (ROOT / "lessons/lesson-ui.js").read_text(encoding="utf-8")
    assert 'input[type="range"]' in source
    assert 'aria-valuetext' in source
    assert 'aria-live' in source
    assert 'aria-pressed' in source
    assert 'document.querySelectorAll(".quiz")' in source
    assert 'quiz.dataset[key]' in source
    assert 'LessonUiLogic.feedbackFor' in source
    assert "dataset.remediation" in source
    assert "Review the relevant concept" in source


def test_every_quiz_uses_the_diagnostic_feedback_pattern():
    quiz_count = sum(path.read_text(encoding="utf-8").count('class="quiz"') for path in LESSONS)
    assert quiz_count == 70


def test_course_viewer_hides_and_disables_background_content():
    html = (ROOT / "course.html").read_text(encoding="utf-8")
    script = (ROOT / "course.js").read_text(encoding="utf-8")
    assert 'id="courseMain"' in html
    assert 'courseMain.inert=true' in script
    assert 'aria-hidden' in script
    assert 'document.title=' in script


def test_terminology_bridges_and_templates_exist():
    lesson_7 = (ROOT / "lessons/07_backpropagation_from_scratch/index.html").read_text(encoding="utf-8")
    lesson_10 = (ROOT / "lessons/10_regularization_and_generalization/index.html").read_text(encoding="utf-8")
    lesson_5 = (ROOT / "lessons/05_regression_and_classification/index.html").read_text(encoding="utf-8")
    assert "partial derivative" in lesson_7 and "The symbol <code>∂</code>" in lesson_7
    assert "called a <strong>logit</strong>" in lesson_5
    assert "Three meanings of “bias”" in lesson_10
    assert (ROOT / "templates/capstone-increment.md").exists()
    assert (ROOT / "templates/model-evidence-card.md").exists()
