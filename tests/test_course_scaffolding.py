from pathlib import Path
import importlib.util


ROOT = Path(__file__).parents[1]
GENERATOR_PATH = ROOT / "tools" / "build_lessons.py"
SPEC = importlib.util.spec_from_file_location("build_lessons", GENERATOR_PATH)
assert SPEC and SPEC.loader
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)


def test_scaffolder_never_overwrites_authored_material(tmp_path: Path) -> None:
    lesson = tmp_path / "README.md"
    lesson.write_text("carefully authored explanation", encoding="utf-8")
    GENERATOR.write_if_missing(lesson, "generic scaffold")
    assert lesson.read_text(encoding="utf-8") == "carefully authored explanation"


def test_scaffolder_creates_a_missing_file(tmp_path: Path) -> None:
    lesson = tmp_path / "README.md"
    GENERATOR.write_if_missing(lesson, "new scaffold")
    assert lesson.read_text(encoding="utf-8") == "new scaffold"


def test_course_defines_student_readiness_and_capstone_continuity() -> None:
    standard = (ROOT / "COURSE_DESIGN.md").read_text(encoding="utf-8")
    capstone = (ROOT / "CAPSTONE_PATH.md").read_text(encoding="utf-8")
    assert "no-surprise rule" in standard.lower()
    assert "Student-ready acceptance gate" in standard
    assert "Increment map" in capstone
    assert "What Lesson 35 must not require unexpectedly" in capstone
