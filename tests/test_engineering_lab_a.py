import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
LAB = ROOT / "labs/engineering_lab_a"


def test_engineering_lab_a_is_a_real_resolvable_gate():
    required = {
        "README.md",
        "diagnostic.py",
        "model.py",
        "run_lab.py",
        "test_model.py",
        "EVIDENCE_TEMPLATE.md",
    }
    assert required <= {path.name for path in LAB.iterdir()}
    guide = (LAB / "README.md").read_text(encoding="utf-8")
    for requirement in (
        "Experienced Python route",
        "Supported route",
        "Windows PowerShell",
        "macOS/Linux",
        "read an error",
        "tensor shape",
        "controlled failure",
        "pytest -q labs/engineering_lab_a/test_model.py",
    ):
        assert requirement.lower() in guide.lower()


def test_p2_i06_closes_the_phase_two_dependency_chain():
    p2_i05 = json.loads((ROOT / "phase-projects/phase2/P2-I05.json").read_text(encoding="utf-8"))
    p2_i06_path = ROOT / p2_i05["downstream_consumer"]
    assert p2_i06_path.is_file()
    p2_i06 = json.loads(p2_i06_path.read_text(encoding="utf-8"))
    assert p2_i06["increment_id"] == "P2-I06"
    assert p2_i06["verification"]["automated_command"] == "pytest -q labs/engineering_lab_a/test_model.py"
    assert "phase-projects/phase2/P2-I05.json" in p2_i06["upstream_evidence"]
    assert len(p2_i06["acceptance_criteria"]) >= 3


def test_lab_is_linked_from_course_and_lesson_ten():
    course = (ROOT / "course.js").read_text(encoding="utf-8")
    lesson = (ROOT / "lessons/10_regularization_and_generalization/index.html").read_text(encoding="utf-8")
    target = "labs/engineering_lab_a/index.html"
    assert target in course
    assert "../../labs/engineering_lab_a/README.md" in lesson


def test_lab_card_follows_lesson_ten_and_opens_a_learner_page():
    course = (ROOT / "course.js").read_text(encoding="utf-8")
    page = (LAB / "index.html").read_text(encoding="utf-8")
    assert "phaseIndex === 1" in course
    assert course.index("host.appendChild(section)") < course.index('href="labs/engineering_lab_a/index.html"')
    for learner_need in ("Choose your route", "What you will prove", "Six-stage path", "Start the lab"):
        assert learner_need in page


def test_pytorch_is_an_explicit_optional_dependency():
    project = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'engineering-lab-a = ["torch>=2.4,<3"]' in project
