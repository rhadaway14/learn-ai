from __future__ import annotations

import copy
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path

import torch
from torch import nn


FEATURE_ORDER = ("planned_integrations", "document_count", "deadline_days", "customer_tier", "prior_projects")


@dataclass(frozen=True)
class RunConfig:
    seed: int = 17
    epochs: int = 300
    learning_rate: float = 0.03
    hidden_width: int = 12
    patience: int = 30
    minimum_improvement: float = 0.001

    def validate(self) -> None:
        if not 2 <= self.epochs <= 2_000:
            raise ValueError("epochs must be between 2 and 2000")
        if not 0 < self.learning_rate <= 1_000_000:
            raise ValueError("learning_rate must be greater than zero")
        if not 2 <= self.hidden_width <= 128:
            raise ValueError("hidden_width must be between 2 and 128")
        if not 1 <= self.patience < self.epochs:
            raise ValueError("patience must be positive and less than epochs")


class DeliveryRiskNet(nn.Module):
    def __init__(self, input_width: int = 5, hidden_width: int = 8) -> None:
        super().__init__()
        self.layers = nn.Sequential(nn.Linear(input_width, hidden_width), nn.ReLU(), nn.Linear(hidden_width, 1))

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        if features.ndim != 2 or features.shape[1] != 5:
            raise ValueError(f"expected features shaped (batch, 5), received {tuple(features.shape)}")
        return self.layers(features).squeeze(1)


def seed_everything(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)


def make_dataset(seed: int = 17, rows: int = 600) -> tuple[torch.Tensor, torch.Tensor]:
    generator = torch.Generator().manual_seed(seed)
    features = torch.randn(rows, 5, generator=generator)
    signal = (
        1.15 * features[:, 0]
        + 0.85 * features[:, 1]
        - 0.95 * features[:, 2]
        + 0.45 * features[:, 3]
        - 0.35 * features[:, 4]
        + 0.30 * features[:, 0] * features[:, 1]
        + 0.60 * torch.randn(rows, generator=generator)
    )
    cutoff = torch.quantile(signal, 0.88)
    labels = (signal >= cutoff).float()
    permutation = torch.randperm(rows, generator=generator)
    return features[permutation], labels[permutation]


def split_dataset(features: torch.Tensor, labels: torch.Tensor) -> dict[str, tuple[torch.Tensor, torch.Tensor]]:
    return split_and_normalize(features, labels)[0]


def split_and_normalize(
    features: torch.Tensor, labels: torch.Tensor
) -> tuple[dict[str, tuple[torch.Tensor, torch.Tensor]], torch.Tensor, torch.Tensor]:
    training = features[:400]
    means = training.mean(dim=0)
    scales = training.std(dim=0).clamp_min(1e-6)
    normalize = lambda values: (values - means) / scales
    return (
        {
            "train": (normalize(training), labels[:400]),
            "validation": (normalize(features[400:500]), labels[400:500]),
            "test": (normalize(features[500:]), labels[500:]),
        },
        means,
        scales,
    )


def binary_metrics(logits: torch.Tensor, labels: torch.Tensor) -> dict[str, float]:
    predictions = (torch.sigmoid(logits) >= 0.5).float()
    true_positive = int(((predictions == 1) & (labels == 1)).sum().item())
    false_positive = int(((predictions == 1) & (labels == 0)).sum().item())
    false_negative = int(((predictions == 0) & (labels == 1)).sum().item())
    return {
        "accuracy": (predictions == labels).float().mean().item(),
        "precision": true_positive / max(1, true_positive + false_positive),
        "recall": true_positive / max(1, true_positive + false_negative),
    }


def majority_baseline(labels: torch.Tensor) -> dict[str, float]:
    logits = torch.full_like(labels, 100.0 if labels.mean().item() >= 0.5 else -100.0)
    return binary_metrics(logits, labels)


def train(config: RunConfig) -> tuple[DeliveryRiskNet, dict[str, object]]:
    config.validate()
    seed_everything(config.seed)
    splits, means, scales = split_and_normalize(*make_dataset(config.seed))
    model = DeliveryRiskNet(hidden_width=config.hidden_width)
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
    positives = splits["train"][1].sum().clamp_min(1)
    negatives = len(splits["train"][1]) - positives
    loss_function = nn.BCEWithLogitsLoss(pos_weight=negatives / positives)
    best_state: dict[str, torch.Tensor] | None = None
    best_loss = math.inf
    best_epoch = 0
    stale_epochs = 0
    finite_gradients = True
    history: list[dict[str, float | int]] = []
    for epoch in range(1, config.epochs + 1):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        train_logits = model(splits["train"][0])
        train_loss = loss_function(train_logits, splits["train"][1])
        train_value = train_loss.detach().item()
        if not torch.isfinite(train_loss) or train_value > 100:
            raise RuntimeError(f"unstable training at epoch {epoch}: loss={train_value}")
        train_loss.backward()
        finite_gradients = all(
            parameter.grad is not None and torch.isfinite(parameter.grad).all().item()
            for parameter in model.parameters()
        )
        if not finite_gradients:
            raise RuntimeError(f"invalid gradient at epoch {epoch}")
        optimizer.step()
        model.eval()
        with torch.no_grad():
            validation_loss = loss_function(model(splits["validation"][0]), splits["validation"][1])
        record = {
            "epoch": epoch,
            "train_loss": train_value,
            "validation_loss": validation_loss.item(),
        }
        history.append(record)
        if record["validation_loss"] < best_loss - config.minimum_improvement:
            best_loss = record["validation_loss"]
            best_epoch = epoch
            best_state = copy.deepcopy(model.state_dict())
            stale_epochs = 0
        else:
            stale_epochs += 1
        if stale_epochs >= config.patience:
            break
    if best_state is None:
        raise RuntimeError("training produced no qualifying checkpoint")
    model.load_state_dict(best_state)
    model.eval()
    with torch.no_grad():
        test_logits = model(splits["test"][0])
        test_loss = loss_function(test_logits, splits["test"][1]).item()
        metrics = binary_metrics(test_logits, splits["test"][1])
    baseline = majority_baseline(splits["test"][1])
    checks = {
        "nonzero_recall": metrics["recall"] > 0,
        "accuracy_beats_majority_baseline": metrics["accuracy"] > baseline["accuracy"],
        "checkpoint_precedes_final_epoch": best_epoch < config.epochs,
        "all_gradients_finite": finite_gradients,
    }
    evidence = {
        "config": asdict(config),
        "feature_order": list(FEATURE_ORDER),
        "architecture": [5, config.hidden_width, 1],
        "preprocessing": {"means": means.tolist(), "scales": scales.tolist()},
        "selection_rule": "lowest validation loss with patience-based early stopping",
        "selected_epoch": best_epoch,
        "epochs_completed": len(history),
        "history": history,
        "baseline_metrics": baseline,
        "test_loss": test_loss,
        "test_metrics": metrics,
        "acceptance": {"passed": all(checks.values()), "checks": checks},
    }
    return model, evidence


def save_checkpoint(path: Path, model: DeliveryRiskNet, evidence: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state": model.state_dict(), "metadata": evidence}, path)


def write_evidence(path: Path, evidence: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
