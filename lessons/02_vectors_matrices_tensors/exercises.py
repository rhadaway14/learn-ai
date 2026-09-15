"""Lesson 02 exercises. Replace each NotImplementedError with your code."""

import numpy as np


def vector_magnitude(vector: np.ndarray) -> float:
    """Return the L2 magnitude without calling np.linalg.norm."""
    raise NotImplementedError("TODO: square, sum, and take the square root")


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """Return the dot product without calling np.dot or using @."""
    raise NotImplementedError("TODO: multiply corresponding values and sum")


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Return cosine similarity using the two functions above."""
    raise NotImplementedError("TODO: dot(a,b) / (magnitude(a) * magnitude(b))")


def dense_layer(inputs: np.ndarray, weights: np.ndarray, bias: np.ndarray) -> np.ndarray:
    """Apply one dense layer to a batch using matrix multiplication."""
    raise NotImplementedError("TODO: matrix multiply, then add the broadcast bias")


def pairwise_scores(queries: np.ndarray, keys: np.ndarray) -> np.ndarray:
    """Return every query-key dot product; a preview of attention."""
    raise NotImplementedError("TODO: multiply queries by the transpose of keys")
