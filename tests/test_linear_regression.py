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


def test_dataset_controls_do_not_require_source_edits() -> None:
    x, y = MODULE.make_dataset(
        seed=1,
        samples=20,
        noise_std=0,
        true_weight=2,
        true_bias=5,
    )
    np.testing.assert_allclose(y, 2 * x + 5)


def test_command_line_parser_exposes_experiment_controls() -> None:
    args = MODULE.build_parser().parse_args(
        ["--learning-rate", "0.001", "--samples", "50", "--noise", "4"]
    )
    assert args.learning_rate == 0.001
    assert args.samples == 50
    assert args.noise == 4
