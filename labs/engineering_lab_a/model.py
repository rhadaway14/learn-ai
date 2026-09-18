from __future__ import annotations

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
    epochs: int = 80
    learning_rate: float = 0.03
    hidden_width: int = 8


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
    signal = 1.1 * features[:, 0] + 0.7 * features[:, 1] - 0.8 * features[:, 2] + 0.45 * features[:, 3]
    probability = torch.sigmoid(signal - 1.1)
    labels = torch.bernoulli(probability, generator=generator)
    return features, labels


def split_dataset(features: torch.Tensor, labels: torch.Tensor) -> dict[str, tuple[torch.Tensor, torch.Tensor]]:
    return {"train": (features[:400], labels[:400]), "validation": (features[400:500], labels[400:500]), "test": (features[500:], labels[500:])}


def binary_metrics(logits: torch.Tensor, labels: torch.Tensor) -> dict[str, float]:
    predictions = (torch.sigmoid(logits) >= 0.5).float()
    true_positive = float(((predictions == 1) & (labels == 1)).sum())
    false_positive = float(((predictions == 1) & (labels == 0)).sum())
    false_negative = float(((predictions == 0) & (labels == 1)).sum())
    return {
        "accuracy": float((predictions == labels).float().mean()),
        "precision": true_positive / max(1.0, true_positive + false_positive),
        "recall": true_positive / max(1.0, true_positive + false_negative),
    }


def train(config: RunConfig) -> tuple[DeliveryRiskNet, dict[str, object]]:
    seed_everything(config.seed)
    splits = split_dataset(*make_dataset(config.seed))
    model = DeliveryRiskNet(hidden_width=config.hidden_width)
    optimizer = torch.optim.SGD(model.parameters(), lr=config.learning_rate)
    loss_function = nn.BCEWithLogitsLoss()
    best_state: dict[str, torch.Tensor] | None = None
    best_loss = math.inf
    best_epoch = 0
    history: list[dict[str, float | int]] = []
    for epoch in range(1, config.epochs + 1):
        model.train()
        optimizer.zero_grad()
        train_logits = model(splits["train"][0])
        train_loss = loss_function(train_logits, splits["train"][1])
        if not torch.isfinite(train_loss) or float(train_loss) > 100:
            raise RuntimeError(f"unstable training at epoch {epoch}: loss={float(train_loss)}")
        train_loss.backward()
        if any(parameter.grad is None or not torch.isfinite(parameter.grad).all() for parameter in model.parameters()):
            raise RuntimeError(f"invalid gradient at epoch {epoch}")
        optimizer.step()
        model.eval()
        with torch.no_grad():
            validation_loss = loss_function(model(splits["validation"][0]), splits["validation"][1])
        record = {"epoch": epoch, "train_loss": float(train_loss), "validation_loss": float(validation_loss)}
        history.append(record)
        if record["validation_loss"] < best_loss:
            best_loss = record["validation_loss"]
            best_epoch = epoch
            best_state = {name: value.detach().clone() for name, value in model.state_dict().items()}
    if best_state is None:
        raise RuntimeError("training produced no qualifying checkpoint")
    model.load_state_dict(best_state)
    model.eval()
    with torch.no_grad():
        test_logits = model(splits["test"][0])
        test_loss = float(loss_function(test_logits, splits["test"][1]))
        metrics = binary_metrics(test_logits, splits["test"][1])
    evidence = {"config": asdict(config), "feature_order": list(FEATURE_ORDER), "architecture": [5, config.hidden_width, 1], "selection_rule": "lowest validation loss", "selected_epoch": best_epoch, "history": history, "test_loss": test_loss, "test_metrics": metrics}
    return model, evidence


def save_checkpoint(path: Path, model: DeliveryRiskNet, evidence: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state": model.state_dict(), "metadata": evidence}, path)


def write_evidence(path: Path, evidence: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
