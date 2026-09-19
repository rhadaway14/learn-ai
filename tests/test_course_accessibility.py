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


def test_phase_one_milestone_is_navigable_and_persisted():
    course = (ROOT / "course.js").read_text(encoding="utf-8")
    project = (ROOT / "projects/phase1/index.html").read_text(encoding="utf-8")
    app = (ROOT / "projects/phase1/app.js").read_text(encoding="utf-8")
    progress = (ROOT / "lessons/progress.js").read_text(encoding="utf-8")
    assert 'projects/phase1/index.html' in course
    assert 'state.milestones?.phase1?.completed' in course
    assert '../../lessons/progress.js' in project
    assert 'CourseProgress.completeMilestone("phase1")' in app
    assert "completeMilestone" in progress and "isMilestoneComplete" in progress


def test_phase_one_artifacts_are_versioned_and_attempt_numbered():
    project = (ROOT / "projects/phase1/index.html").read_text(encoding="utf-8")
    app = (ROOT / "projects/phase1/app.js").read_text(encoding="utf-8")
    artifact = (ROOT / "projects/phase1/artifact.js").read_text(encoding="utf-8")
    assert 'src="artifact.js"' in project
    assert "validateDraft(state)" in app
    assert "attempt_number" in artifact
    assert "validateArtifact" in artifact
    assert "-attempt-${String(attempt).padStart(2, \"0\")}.json" in artifact


def test_storage_failures_have_visible_recovery_guidance():
    course_html = (ROOT / "course.html").read_text(encoding="utf-8")
    project_html = (ROOT / "projects/phase1/index.html").read_text(encoding="utf-8")
    project_app = (ROOT / "projects/phase1/app.js").read_text(encoding="utf-8")
    progress = (ROOT / "lessons/progress.js").read_text(encoding="utf-8")
    assert 'id="storageWarning"' in course_html and 'aria-live="polite"' in course_html
    assert 'id="storageWarning"' in project_html and 'aria-live="polite"' in project_html
    assert 'catch (_)' in project_app and "download your evidence artifact" in project_app
    assert "course-storage-error" in progress and "localStorage.setItem" in progress


def test_known_contrast_and_mobile_overflow_regressions_are_covered():
    css = (ROOT / "lessons/accessibility.css").read_text(encoding="utf-8")
    for selector in (
        ".hero-card .cycle-arrow",
        ".split-visual .test-block",
        ".token-flow b",
        ".parameter-count small",
        ".count-grid .posterior small",
        ".branch-paths .total small",
        ".module-total small",
        ".module-total strong",
    ):
        assert selector in css
    assert ".split-visual .test-block{background:#087064!important}" in css
    assert ".architecture-visual,.autograd-graph" in css
    assert ".architecture-layer,.autograd-node" in css
    assert "min-width:0!important" in css
