"""Reference solutions for Lesson 02. Attempt exercises.py first."""

import numpy as np


def vector_magnitude(vector: np.ndarray) -> float:
    return float(np.sqrt(np.sum(vector**2)))


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sum(a * b))


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denominator = vector_magnitude(a) * vector_magnitude(b)
    if denominator == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector")
    return dot_product(a, b) / denominator


def dense_layer(inputs: np.ndarray, weights: np.ndarray, bias: np.ndarray) -> np.ndarray:
    return inputs @ weights + bias


def pairwise_scores(queries: np.ndarray, keys: np.ndarray) -> np.ndarray:
    return queries @ keys.T
