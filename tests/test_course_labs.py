import numpy as np
import pytest

from learn_ai.course_labs import LABS, run_lesson
from capstone.vertical_slice import run as run_capstone_slice


@pytest.mark.parametrize("number", sorted(LABS))
def test_every_registered_lab_runs(number: int) -> None:
    result = run_lesson(number)
    assert isinstance(result, dict)
    assert result


def test_all_advanced_lessons_are_registered() -> None:
    assert set(LABS) == set(range(3, 36))


def test_finite_difference_matches_analytical_gradient() -> None:
    result = run_lesson(3)
    assert result["numerical_gradient"] == pytest.approx(
        result["analytical_gradient"], abs=1e-8
    )


def test_classifier_learns_signal() -> None:
    assert run_lesson(5)["accuracy"] > 0.9


def test_backpropagation_gradients() -> None:
    result = run_lesson(7)
    assert result == {
        "prediction": -5.0,
        "loss": 25.0,
        "d_loss_dx": 20.0,
        "d_loss_dw": -30.0,
        "d_loss_db": -10.0,
    }


def test_xor_network_converges() -> None:
    assert run_lesson(9)["accuracy"] == 1.0


def test_attention_is_causal_and_normalized() -> None:
    weights = np.array(run_lesson(13)["attention_weights"])[0]
    np.testing.assert_allclose(weights.sum(axis=-1), 1.0, atol=1e-4)
    assert np.allclose(np.triu(weights, k=1), 0.0)


def test_lora_update_respects_requested_rank() -> None:
    result = run_lesson(25)
    assert result["update_rank"] <= result["rank"]
    assert result["adapter_parameters"] < result["full_parameters"]


def test_high_risk_capstone_action_requires_approval() -> None:
    assert run_lesson(35)["status"] == "awaiting_human_approval"


def test_unknown_lesson_is_rejected() -> None:
    with pytest.raises(ValueError):
        run_lesson(99)


def test_capstone_vertical_slice_preserves_approval_gate() -> None:
    result = run_capstone_slice()
    assert result["retrieval"]["grounded"]
    assert result["evaluation"]["passes"]
    assert result["workflow"]["status"] == "awaiting_human_approval"
    assert result["release_allowed"]
