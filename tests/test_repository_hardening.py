import json
import re
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).parents[1]


@pytest.mark.parametrize("artifact", sorted((ROOT / "activities").glob("L*-A*.json")))
def test_activity_artifacts_validate_against_schema(artifact: Path):
    schema = json.loads((ROOT / "schemas/lesson-activity.schema.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(json.loads(artifact.read_text(encoding="utf-8")))


@pytest.mark.parametrize("artifact", sorted((ROOT / "phase-projects").glob("phase*/*.json")))
def test_phase_increments_validate_against_schema(artifact: Path):
    schema = json.loads((ROOT / "schemas/phase-project-increment.schema.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(json.loads(artifact.read_text(encoding="utf-8")))


def test_foundations_runtime_does_not_expose_repository_root():
    compose = (ROOT / "compose.yaml").read_text(encoding="utf-8")
    assert "- ./:/usr/share/nginx/html" not in compose
    for required in ("./lessons:", "./projects:", "./labs:", "./templates:"):
        assert required in compose
    assert "FOUNDATIONS_ALLOWED_ORIGIN: http://localhost:8080" in compose
    assert 'FOUNDATIONS_MAX_BODY_BYTES: "65536"' in compose


def test_foundations_api_restricts_cors_and_request_size():
    source = (ROOT / "labs/foundations/api.py").read_text(encoding="utf-8")
    assert 'Access-Control-Allow-Origin", "*"' not in source
    assert 'self.headers.get("Origin") == self.allowed_origin' in source
    assert "HTTPStatus.REQUEST_ENTITY_TOO_LARGE" in source
    assert "length > self.max_body_bytes" in source


def test_advanced_sections_have_real_prerequisites_and_engineering_depth():
    lessons = sorted((ROOT / "lessons").glob("0[1-9]_*/index.html")) + sorted((ROOT / "lessons").glob("10_*/index.html"))
    assert len(lessons) == 10
    for lesson in lessons:
        html = lesson.read_text(encoding="utf-8")
        section = re.search(r'<details[^>]*class="advanced-section"[^>]*>([\s\S]*?)</details>', html)
        assert section, lesson
        text = re.sub(r"<[^>]+>", " ", section.group(1))
        words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’–—-]*", text)
        assert len(words) >= 500, f"{lesson}: {len(words)} advanced words"
        assert "Complete the core interactions first" not in section.group(1)
        for keyword in ("contract", "failure", "monitor", "scale", "rollback"):
            assert keyword in text.lower(), f"{lesson}: missing {keyword}"


def test_every_interactive_lesson_links_the_activity_template():
    ui = (ROOT / "lessons/lesson-ui.js").read_text(encoding="utf-8")
    assert '../../templates/lesson-activity.md' in ui


def test_lessons_nine_and_ten_have_renderable_math():
    for lesson in ("09_train_and_evaluate_a_neural_network", "10_regularization_and_generalization"):
        readme = (ROOT / f"lessons/{lesson}/README.md").read_text(encoding="utf-8")
        assert readme.count("$$") >= 2


def test_first_ten_titles_are_consistent_across_navigation_and_docs():
    titles = [
        "How Machines Learn",
        "The Shapes of AI Data",
        "Loss Functions and Optimization",
        "Probability and Statistics for ML",
        "Regression and Classification",
        "Neural Network Anatomy",
        "Backpropagation From Scratch",
        "PyTorch and Autograd",
        "Train and Evaluate a Neural Network",
        "Regularization and Generalization",
    ]
    course = (ROOT / "course.js").read_text(encoding="utf-8")
    curriculum = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
    lesson_index = (ROOT / "lessons/README.md").read_text(encoding="utf-8")
    directories = sorted((ROOT / "lessons").glob("0[1-9]_*/")) + sorted((ROOT / "lessons").glob("10_*/"))
    for number, (title, directory) in enumerate(zip(titles, directories), 1):
        assert f'"{title}"' in course
        assert f"| {number:02d} | {title} |" in curriculum
        assert f"| {number:02d} | {title} |" in lesson_index
        assert f"# Lesson {number:02d} — {title}" in (directory / "README.md").read_text(encoding="utf-8")
        assert f"<h1>{title}</h1>" in (directory / "index.html").read_text(encoding="utf-8")


def test_curriculum_times_match_browser_learning_lanes():
    curriculum = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
    expected = {
        1: ("60", "20–30", "80–90m"),
        2: ("75", "25–35", "100–110m"),
        3: ("75", "25–35", "100–110m"),
        4: ("85", "35–45", "120–130m"),
        5: ("95", "40–50", "135–145m"),
        6: ("80", "35–45", "115–125m"),
        7: ("85", "40–50", "125–135m"),
        8: ("85", "40–50", "125–135m"),
        9: ("90", "40–50", "130–140m"),
        10: ("90", "40–50", "130–140m"),
    }
    for number, (core, advanced, total) in expected.items():
        directory = next((ROOT / "lessons").glob(f"{number:02d}_*"))
        html = (directory / "index.html").read_text(encoding="utf-8")
        assert f"Core path · about {core} minutes" in html
        assert f"Engineer path · add {advanced} minutes" in html
        assert f"| {number:02d} |" in curriculum and total in curriculum
