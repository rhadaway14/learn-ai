from __future__ import annotations

import pytest

torch = pytest.importorskip("torch")

from labs.phase2.api.model import (
    FEATURE_ORDER,
    TrainingConfig,
    make_dataset,
    predict,
    train_model,
)


@pytest.fixture(scope="module")
def known_good():
    return train_model(TrainingConfig())


def test_dataset_is_deterministic_and_preserves_the_northstar_contract():
    first_features, first_labels = make_dataset()
    second_features, second_labels = make_dataset()
    assert first_features.shape == (2_400, len(FEATURE_ORDER))
    assert first_labels.shape == (2_400,)
    assert torch.equal(first_features, second_features)
    assert torch.equal(first_labels, second_labels)
    assert 0.11 <= first_labels.mean().item() <= 0.13


def test_known_good_run_passes_the_numeric_gate(known_good):
    evidence = known_good.evidence
    assert evidence["acceptance"]["passed"] is True
    assert evidence["sealed_test"]["recall"] >= 0.25
    assert evidence["sealed_test"]["accuracy"] > evidence["baseline"]["accuracy"] + 0.03
    assert evidence["training"]["selected_epoch"] < evidence["configuration"]["epochs"]
    assert evidence["training"]["finite_gradients"] is True
    assert evidence["sealed_test"]["evaluations"] == 1


def test_same_configuration_reproduces_selected_model(known_good):
    repeated = train_model(TrainingConfig())
    assert repeated.evidence["training"]["selected_epoch"] == known_good.evidence["training"]["selected_epoch"]
    assert repeated.evidence["sealed_test"] == known_good.evidence["sealed_test"]


def test_explosive_learning_rate_fails_without_a_checkpoint():
    with pytest.raises(RuntimeError, match="unstable training"):
        train_model(TrainingConfig(epochs=40, learning_rate=1_000_000, patience=10))


def test_promoted_model_scores_a_project(known_good):
    result = predict(
        known_good,
        {
            "planned_integrations": 7,
            "document_count": 4_500,
            "deadline_days": 45,
            "customer_tier": 2,
            "prior_projects": 4,
        },
    )
    assert 0 <= result["probability"] <= 1
    assert result["decision"] in {"high risk", "standard review"}
