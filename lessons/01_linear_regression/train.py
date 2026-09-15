"""Train a one-feature linear-regression model using only NumPy."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def make_dataset(seed: int = 42, samples: int = 200) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    x = rng.uniform(0, 10, samples)
    noise = rng.normal(0, 1.5, samples)
    return x, 3.5 * x + 2 + noise


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


def main() -> None:
    x, y = make_dataset()
    rng = np.random.default_rng(7)
    indices = rng.permutation(len(x))
    train_indices, test_indices = indices[:160], indices[160:]

    w, b, losses = train(x[train_indices], y[train_indices])
    test_predictions = w * x[test_indices] + b
    test_loss = float(np.mean((test_predictions - y[test_indices]) ** 2))

    print(f"\nFinal model: y = {w:.3f}x + {b:.3f}")
    print(f"Test loss: {test_loss:.4f}")

    line_x = np.linspace(0, 10, 100)
    output_dir = Path(__file__).parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "learned_line.png"

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
