from __future__ import annotations

import copy
import math
import random
from dataclasses import asdict, dataclass
from typing import Any

import torch
from torch import nn


FEATURE_ORDER = (
    "planned_integrations",
    "document_count",
    "deadline_days",
    "customer_tier",
    "prior_projects",
)
LABEL_NOISE_STD = 0.6


@dataclass(frozen=True)
class TrainingConfig:
    seed: int = 17
    epochs: int = 300
    learning_rate: float = 0.05
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


class NeuralRiskModel(nn.Module):
    def __init__(self, hidden_width: int = 12) -> None:
        super().__init__()
        second_width = max(4, hidden_width // 2)
        self.layers = nn.Sequential(
            nn.Linear(5, hidden_width),
            nn.ReLU(),
            nn.Linear(hidden_width, second_width),
            nn.ReLU(),
            nn.Linear(second_width, 1),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        if features.ndim != 2 or features.shape[1] != 5:
            raise ValueError(
                f"expected features shaped (batch, 5), received {tuple(features.shape)}"
            )
        return self.layers(features).squeeze(1)


@dataclass
class TrainedModel:
    model: NeuralRiskModel
    means: torch.Tensor
    scales: torch.Tensor
    evidence: dict[str, Any]


def seed_everything(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)


def make_dataset(seed: int = 17, rows: int = 2_400) -> tuple[torch.Tensor, torch.Tensor]:
    """Create a deterministic, production-shaped Northstar teaching dataset."""
    generator = torch.Generator().manual_seed(seed)
    integrations = torch.randint(0, 13, (rows,), generator=generator).float()
    document_count = torch.exp(torch.randn(rows, generator=generator) * 0.75 + 8.0)
    deadline_days = torch.randint(14, 181, (rows,), generator=generator).float()
    customer_tier = torch.randint(0, 4, (rows,), generator=generator).float()
    prior_projects = torch.randint(0, 31, (rows,), generator=generator).float()
    raw = torch.stack(
        (integrations, document_count, deadline_days, customer_tier, prior_projects),
        dim=1,
    )
    standardized = (raw - raw.mean(dim=0)) / raw.std(dim=0).clamp_min(1e-6)
    risk = (
        1.15 * standardized[:, 0]
        + 0.85 * standardized[:, 1]
        - 0.95 * standardized[:, 2]
        + 0.45 * standardized[:, 3]
        - 0.35 * standardized[:, 4]
        + 0.30 * standardized[:, 0] * standardized[:, 1]
        + LABEL_NOISE_STD * torch.randn(rows, generator=generator)
    )
    cutoff = torch.quantile(risk, 0.88)
    labels = (risk >= cutoff).float()
    permutation = torch.randperm(rows, generator=generator)
    return raw[permutation], labels[permutation]


def split_and_normalize(
    raw: torch.Tensor, labels: torch.Tensor
) -> tuple[dict[str, tuple[torch.Tensor, torch.Tensor]], torch.Tensor, torch.Tensor]:
    train_raw, validation_raw, test_raw = raw[:1_600], raw[1_600:2_000], raw[2_000:]
    means = train_raw.mean(dim=0)
    scales = train_raw.std(dim=0).clamp_min(1e-6)
    normalize = lambda values: (values - means) / scales
    return (
        {
            "train": (normalize(train_raw), labels[:1_600]),
            "validation": (normalize(validation_raw), labels[1_600:2_000]),
            "test": (normalize(test_raw), labels[2_000:]),
        },
        means,
        scales,
    )


def binary_metrics(logits: torch.Tensor, labels: torch.Tensor) -> dict[str, float | int]:
    predictions = (torch.sigmoid(logits) >= 0.5).float()
    true_positive = int(((predictions == 1) & (labels == 1)).sum().item())
    false_positive = int(((predictions == 1) & (labels == 0)).sum().item())
    false_negative = int(((predictions == 0) & (labels == 1)).sum().item())
    true_negative = int(((predictions == 0) & (labels == 0)).sum().item())
    return {
        "accuracy": float((predictions == labels).float().mean().item()),
        "precision": true_positive / max(1, true_positive + false_positive),
        "recall": true_positive / max(1, true_positive + false_negative),
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "true_negative": true_negative,
    }


def majority_baseline(labels: torch.Tensor) -> dict[str, float | int]:
    logits = torch.full_like(labels, -100.0 if labels.mean().item() < 0.5 else 100.0)
    return binary_metrics(logits, labels)


def acceptance_checks(
    *, baseline: dict[str, float | int], metrics: dict[str, float | int], selected_epoch: int,
    configured_epochs: int, finite_gradients: bool, sealed_test_evaluations: int
) -> dict[str, bool]:
    return {
        "recall_at_least_0_25": float(metrics["recall"]) >= 0.25,
        "accuracy_beats_baseline_by_0_03": float(metrics["accuracy"]) > float(baseline["accuracy"]) + 0.03,
        "checkpoint_precedes_final_epoch": selected_epoch < configured_epochs,
        "all_gradients_finite": finite_gradients,
        "sealed_test_evaluated_once": sealed_test_evaluations == 1,
    }


def train_model(config: TrainingConfig) -> TrainedModel:
    config.validate()
    seed_everything(config.seed)
    splits, means, scales = split_and_normalize(*make_dataset(config.seed))
    model = NeuralRiskModel(config.hidden_width)
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
    positives = splits["train"][1].sum().clamp_min(1)
    negatives = len(splits["train"][1]) - positives
    loss_function = nn.BCEWithLogitsLoss(pos_weight=(negatives / positives))
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
        gradients = [parameter.grad for parameter in model.parameters()]
        finite_gradients = all(
            gradient is not None and torch.isfinite(gradient).all().item()
            for gradient in gradients
        )
        if not finite_gradients:
            raise RuntimeError(f"invalid gradient at epoch {epoch}")
        gradient_norm = math.sqrt(
            sum(float(gradient.detach().pow(2).sum().item()) for gradient in gradients if gradient is not None)
        )
        optimizer.step()

        model.eval()
        with torch.no_grad():
            validation_logits = model(splits["validation"][0])
            validation_loss = loss_function(validation_logits, splits["validation"][1]).item()
        history.append(
            {
                "epoch": epoch,
                "train_loss": train_value,
                "validation_loss": float(validation_loss),
                "gradient_norm": gradient_norm,
            }
        )
        if validation_loss < best_loss - config.minimum_improvement:
            best_loss = float(validation_loss)
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
    sealed_test_evaluations = 0
    with torch.no_grad():
        test_logits = model(splits["test"][0])
        sealed_test_evaluations += 1
        metrics = binary_metrics(test_logits, splits["test"][1])
    baseline = majority_baseline(splits["test"][1])
    checks = acceptance_checks(
        baseline=baseline,
        metrics=metrics,
        selected_epoch=best_epoch,
        configured_epochs=config.epochs,
        finite_gradients=finite_gradients,
        sealed_test_evaluations=sealed_test_evaluations,
    )
    evidence = {
        "feature_order": list(FEATURE_ORDER),
        "dataset": {
            "rows": 2_400,
            "train_rows": 1_600,
            "validation_rows": 400,
            "test_rows": 400,
            "positive_rate": float(splits["test"][1].mean().item()),
            "label_noise_std": LABEL_NOISE_STD,
        },
        "configuration": asdict(config),
        "architecture": [5, config.hidden_width, max(4, config.hidden_width // 2), 1],
        "baseline": baseline,
        "training": {
            "selected_epoch": best_epoch,
            "epochs_completed": len(history),
            "finite_gradients": finite_gradients,
            "history": history,
        },
        "sealed_test": {**metrics, "evaluations": sealed_test_evaluations},
        "acceptance": {"passed": all(checks.values()), "checks": checks},
    }
    return TrainedModel(model=model, means=means, scales=scales, evidence=evidence)


def predict(trained: TrainedModel, values: dict[str, float]) -> dict[str, float | str]:
    missing = [name for name in FEATURE_ORDER if name not in values]
    if missing:
        raise ValueError(f"missing features: {', '.join(missing)}")
    raw = torch.tensor([[float(values[name]) for name in FEATURE_ORDER]], dtype=torch.float32)
    normalized = (raw - trained.means) / trained.scales
    trained.model.eval()
    with torch.no_grad():
        probability = torch.sigmoid(trained.model(normalized)).item()
    return {
        "score": probability,
        "decision": "high risk" if probability >= 0.5 else "standard review",
        "threshold": 0.5,
        "calibrated_probability": False,
    }
