"""Train a one-feature linear-regression model using only NumPy.

Run ``python train.py --help`` to see the experiment controls. Learners change
command-line options rather than editing this file.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def make_dataset(
    seed: int = 42,
    samples: int = 200,
    noise_std: float = 1.5,
    true_weight: float = 3.5,
    true_bias: float = 2.0,
    relationship: str = "linear",
    outlier: float = 0.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Create a reproducible synthetic regression dataset."""
    if samples < 3:
        raise ValueError("samples must be at least 3")
    if noise_std < 0:
        raise ValueError("noise_std cannot be negative")
    if relationship not in {"linear", "quadratic"}:
        raise ValueError("relationship must be 'linear' or 'quadratic'")

    rng = np.random.default_rng(seed)
    x = rng.uniform(0, 10, samples)
    noise = rng.normal(0, noise_std, samples)
    signal = true_weight * x + true_bias
    if relationship == "quadratic":
        signal = x**2 + true_bias
    y = signal + noise
    if outlier:
        y[0] += outlier
    return x, y


def train(
    x: np.ndarray,
    y: np.ndarray,
    learning_rate: float = 0.01,
    epochs: int = 2_000,
) -> tuple[float, float, list[float]]:
    w = 0.0
    b = 0.0
    losses: list[float] = []

    for epoch in range(epochs):
        predictions = w * x + b
        errors = predictions - y
        loss = float(np.mean(errors**2))
        losses.append(loss)

        dw = float(2 * np.mean(errors * x))
        db = float(2 * np.mean(errors))
        w -= learning_rate * dw
        b -= learning_rate * db

        if epoch % 200 == 0:
            print(f"epoch={epoch:4d} loss={loss:8.4f} w={w:8.4f} b={b:8.4f}")

    return w, b, losses


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore linear regression without editing Python code."
    )
    parser.add_argument("--learning-rate", type=float, default=0.01)
    parser.add_argument("--epochs", type=int, default=2_000)
    parser.add_argument("--samples", type=int, default=200)
    parser.add_argument("--train-size", type=int, default=None)
    parser.add_argument("--noise", type=float, default=1.5)
    parser.add_argument("--data-seed", type=int, default=42)
    parser.add_argument("--split-seed", type=int, default=7)
    parser.add_argument("--true-weight", type=float, default=3.5)
    parser.add_argument("--true-bias", type=float, default=2.0)
    parser.add_argument(
        "--relationship", choices=("linear", "quadratic"), default="linear"
    )
    parser.add_argument(
        "--outlier",
        type=float,
        default=0.0,
        help="add this amount to one label to demonstrate outlier sensitivity",
    )
    parser.add_argument("--output-name", default="learned_line.png")
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    if args.learning_rate <= 0:
        raise ValueError("learning_rate must be positive")
    if args.epochs < 1:
        raise ValueError("epochs must be at least 1")

    x, y = make_dataset(
        seed=args.data_seed,
        samples=args.samples,
        noise_std=args.noise,
        true_weight=args.true_weight,
        true_bias=args.true_bias,
        relationship=args.relationship,
        outlier=args.outlier,
    )
    train_size = args.train_size if args.train_size is not None else int(0.8 * len(x))
    if not 2 <= train_size < len(x):
        raise ValueError("train_size must leave at least two training and one test example")

    print("Experiment configuration")
    for name in (
        "relationship", "samples", "noise", "learning_rate", "epochs",
        "data_seed", "split_seed", "true_weight", "true_bias", "outlier",
    ):
        print(f"  {name:15s}: {getattr(args, name)}")
    print(f"  {'train_size':15s}: {train_size}")

    rng = np.random.default_rng(args.split_seed)
    indices = rng.permutation(len(x))
    train_indices, test_indices = indices[:train_size], indices[train_size:]

    w, b, losses = train(
        x[train_indices],
        y[train_indices],
        learning_rate=args.learning_rate,
        epochs=args.epochs,
    )
    test_predictions = w * x[test_indices] + b
    test_loss = float(np.mean((test_predictions - y[test_indices]) ** 2))

    print(f"\nFinal model: y = {w:.3f}x + {b:.3f}")
    print(f"Test loss: {test_loss:.4f}")

    line_x = np.linspace(0, 10, 100)
    output_dir = Path(__file__).parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / Path(args.output_name).name

    _, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].scatter(x[test_indices], y[test_indices], label="Test data")
    axes[0].plot(line_x, w * line_x + b, color="tab:red", label="Learned model")
    axes[0].set(xlabel="x", ylabel="y", title="Model fit")
    axes[0].legend()
    axes[1].plot(losses)
    axes[1].set(xlabel="Epoch", ylabel="MSE", title="Training loss")
    plt.tight_layout()
    plt.savefig(output_path, dpi=160)
    plt.close()
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    main()
