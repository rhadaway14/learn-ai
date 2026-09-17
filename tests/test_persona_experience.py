from pathlib import Path

import pytest


ROOT = Path(__file__).parents[1]


@pytest.mark.parametrize("lesson", [1, 2, 3])
def test_reference_lessons_make_both_learning_depths_discoverable(lesson: int):
    directory = next((ROOT / "lessons").glob(f"{lesson:02d}_*"))
    html = (directory / "index.html").read_text(encoding="utf-8")
    lanes = html.index('class="learning-lanes"')
    core = html.index('data-depth="core"')
    advanced = html.index('data-depth="advanced"')
    story = html.index('id="ai-story"')
    assert lanes < story
    assert core < story and advanced < story
    assert "Core path" in html
    assert "Engineer path" in html
    assert "no coding is required" in html.lower() or "without writing code" in html.lower()
    assert "CORE REQUIRED, EXTENSION OPTIONAL" in html
    assert "about " in html and "add " in html


def test_persona_protocol_requires_behavioral_evidence_not_component_presence():
    protocol = (ROOT / "PERSONA_TESTING.md").read_text(encoding="utf-8")
    for requirement in (
        "New-to-AI engineer",
        "Experienced engineer",
        "first point of hesitation",
        "Trigger the documented failure",
        "Human pilot capture",
        "not mark a future lesson persona-validated solely",
    ):
        assert requirement.lower() in protocol.lower()


def test_reference_review_discloses_method_limitations_and_actions():
    review = (ROOT / "evaluations/persona-review-foundations-reference.md").read_text(encoding="utf-8")
    assert "no observed external human sessions" in review
    assert "pre-pilot" in review
    assert "Windows Docker Desktop" in review
    assert "Unix-like host" in review
    assert "Lessons 1–3 pass" in review


def test_workbench_renders_selected_activity_and_preserves_api_fallback():
    html = (ROOT / "labs/foundations/index.html").read_text(encoding="utf-8")
    script = (ROOT / "labs/foundations/app.js").read_text(encoding="utf-8")
    assert 'id="activityGuide"' in html
    assert "Short plain-language notes are enough" in html
    assert "Observed evidence" in html
    assert "../../activities/" in script
    assert "Engineer extension · optional" in script
    assert "activity.artifact.path_or_download" in script
    assert "Keep your notes here" in script
