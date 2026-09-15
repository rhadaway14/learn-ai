"""Explore the linear-algebra primitives beneath neural networks."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    if denominator == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector")
    return float(np.dot(a, b) / denominator)


def dense_layer(inputs: np.ndarray, weights: np.ndarray, bias: np.ndarray) -> np.ndarray:
    """Compute a dense layer for an entire batch."""
    return inputs @ weights + bias


def describe(name: str, value: np.ndarray) -> None:
    print(f"{name:18s} shape={str(value.shape):12s} rank={value.ndim} values=\n{value}\n")


def main() -> None:
    scalar = np.array(3.0)
    vector = np.array([2.0, -1.0, 3.0])
    matrix = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    tensor_3d = np.arange(24).reshape(2, 3, 4)

    print("=== Shapes and ranks ===")
    for name, value in (("scalar", scalar), ("vector", vector), ("matrix", matrix), ("rank-3 tensor", tensor_3d)):
        describe(name, value)

    print("=== Vector operations ===")
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, -1.0, 2.0])
    print(f"a + b: {a + b}")
    print(f"2a: {2 * a}")
    print(f"||a||: {np.linalg.norm(a):.4f}")
    print(f"a dot b: {np.dot(a, b):.4f}")
    print(f"cosine(a, b): {cosine_similarity(a, b):.4f}\n")

    print("=== One dense neural-network layer ===")
    inputs = np.array([[1.0, 0.5, -1.0], [0.0, 2.0, 1.0]])  # (batch=2, features=3)
    weights = np.array([[0.2, 0.8], [-0.5, 0.1], [1.0, -0.3]])  # (3 inputs, 2 outputs)
    bias = np.array([0.1, -0.2])  # broadcast across batch
    output = dense_layer(inputs, weights, bias)
    print(f"{inputs.shape} @ {weights.shape} + {bias.shape} -> {output.shape}")
    print(output)

    print("\n=== Tiny semantic-vector example ===")
    dog = np.array([0.90, 0.80])
    puppy = np.array([0.82, 0.76])
    database = np.array([-0.70, 0.30])
    print(f"dog ↔ puppy:    {cosine_similarity(dog, puppy):.4f}")
    print(f"dog ↔ database: {cosine_similarity(dog, database):.4f}")
    print("These hand-authored vectors illustrate the geometry; real embeddings are learned.")

    output_dir = Path(__file__).parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "vectors_and_transformations.png"

    origin = np.zeros(3)
    _, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    vectors = np.stack([dog, puppy, database])
    axes[0].quiver(origin, origin, vectors[:, 0], vectors[:, 1], angles="xy", scale_units="xy", scale=1, color=["tab:blue", "tab:green", "tab:red"])
    axes[0].set(xlim=(-1, 1.1), ylim=(-0.1, 1), aspect="equal", title="Embedding directions", xlabel="dimension 1", ylabel="dimension 2")
    axes[0].legend(["dog", "puppy", "database"])

    transformed = matrix @ weights
    axes[1].imshow(transformed, cmap="viridis", aspect="auto")
    axes[1].set(title=f"Matrix transform {matrix.shape} @ {weights.shape}", xlabel="output feature", ylabel="example")
    for row in range(transformed.shape[0]):
        for col in range(transformed.shape[1]):
            axes[1].text(col, row, f"{transformed[row, col]:.1f}", ha="center", va="center", color="white")

    plt.tight_layout()
    plt.savefig(output_path, dpi=160)
    plt.close()
    print(f"\nPlot saved to {output_path}")


if __name__ == "__main__":
    main()
