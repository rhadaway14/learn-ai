from pathlib import Path
import importlib.util

import numpy as np


MODULE_PATH = Path(__file__).parents[1] / "lessons" / "01_linear_regression" / "train.py"
SPEC = importlib.util.spec_from_file_location("linear_regression", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_training_recovers_hidden_relationship() -> None:
    x, y = MODULE.make_dataset()
    w, b, losses = MODULE.train(x, y)
    assert np.isclose(w, 3.5, atol=0.2)
    assert np.isclose(b, 2.0, atol=1.0)
    assert losses[-1] < losses[0]
