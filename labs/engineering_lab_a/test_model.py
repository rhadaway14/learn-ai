import pytest

torch = pytest.importorskip("torch")

from model import DeliveryRiskNet, RunConfig, make_dataset, split_dataset, train


def test_shape_contract_and_gradients():
    model = DeliveryRiskNet()
    logits = model(torch.ones(4, 5))
    assert logits.shape == (4,)
    logits.sum().backward()
    assert all(parameter.grad is not None and torch.isfinite(parameter.grad).all() for parameter in model.parameters())


def test_invalid_feature_width_has_actionable_error():
    with pytest.raises(ValueError, match=r"expected features shaped \(batch, 5\)"):
        DeliveryRiskNet()(torch.ones(4, 4))


def test_splits_are_disjoint_and_have_expected_sizes():
    splits = split_dataset(*make_dataset())
    assert {name: len(values[0]) for name, values in splits.items()} == {"train": 400, "validation": 100, "test": 100}


def test_training_is_reproducible_and_selects_validation_checkpoint():
    config = RunConfig(epochs=12)
    _, first = train(config)
    _, second = train(config)
    assert first["selected_epoch"] == second["selected_epoch"]
    assert first["history"] == second["history"]
    assert 1 <= first["selected_epoch"] <= config.epochs


def test_explosive_learning_rate_fails_closed():
    with pytest.raises(RuntimeError, match="unstable training"):
        train(RunConfig(epochs=20, learning_rate=1_000_000))
