from pathlib import Path


LESSON = Path(__file__).parents[1] / "lessons" / "01_linear_regression"


def test_lesson_01_browser_experience_is_self_contained() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="app.js"></script>' in html
    assert (LESSON / "styles.css").is_file()
    assert (LESSON / "app.js").is_file()


def test_lesson_01_learner_material_does_not_show_python() -> None:
    readme = (LESSON / "README.md").read_text(encoding="utf-8").lower()
    html = (LESSON / "index.html").read_text(encoding="utf-8").lower()
    assert "```python" not in readme
    assert "train.py" not in html
    assert "python " not in html


def test_lesson_01_contains_core_explanations_and_interactions() -> None:
    html = (LESSON / "index.html").read_text(encoding="utf-8")
    for concept in ("Feature", "Label", "Model", "Training", "Inference", "gradient", "Generalization"):
        assert concept in html
    for control in ("learningRate", "epochs", "samples", "noise", "relationship", "outlier"):
        assert f'id="{control}"' in html
