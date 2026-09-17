from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_first_ten_lessons_have_an_explicit_code_boundary():
    curriculum = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
    design = (ROOT / "COURSE_DESIGN.md").read_text(encoding="utf-8")
    capstone = (ROOT / "CAPSTONE_PATH.md").read_text(encoding="utf-8")

    assert "Lessons 1–10 are browser-first and require no Python" in curriculum
    assert "Engineering Lab A" in curriculum
    assert "required release gate" in design
    assert "Reproducible model-training specification and model evidence card" in capstone
    assert "write a correct PyTorch training loop" not in curriculum


def test_lesson_eight_does_not_hide_the_bridge_in_lesson_nine():
    lesson = (ROOT / "lessons/08_pytorch_and_autograd/index.html").read_text(encoding="utf-8")
    assert "Engineering Lab A" in lesson
    assert "Lesson 9 must teach" not in lesson
