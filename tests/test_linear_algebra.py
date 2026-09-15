from pathlib import Path
import importlib.util

import numpy as np
import pytest


MODULE_PATH = Path(__file__).parents[1] / "lessons" / "02_vectors_matrices_tensors" / "solutions.py"
SPEC = importlib.util.spec_from_file_location("linear_algebra_solutions", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_vector_magnitude() -> None:
    assert MODULE.vector_magnitude(np.array([3.0, 4.0])) == pytest.approx(5.0)


def test_dot_product() -> None:
    assert MODULE.dot_product(np.array([1.0, 2.0, 3.0]), np.array([4.0, -1.0, 2.0])) == pytest.approx(8.0)


def test_cosine_similarity_scale_invariant() -> None:
    a = np.array([1.0, 2.0])
    b = np.array([2.0, 1.0])
    assert MODULE.cosine_similarity(a, b) == pytest.approx(MODULE.cosine_similarity(10 * a, b))


def test_cosine_similarity_rejects_zero_vector() -> None:
    with pytest.raises(ValueError):
        MODULE.cosine_similarity(np.zeros(2), np.ones(2))


def test_dense_layer_shape_and_values() -> None:
    inputs = np.array([[1.0, 2.0], [3.0, 4.0]])
    weights = np.array([[1.0, 0.0, -1.0], [0.5, 2.0, 1.0]])
    bias = np.array([0.1, 0.2, 0.3])
    expected = np.array([[2.1, 4.2, 1.3], [5.1, 8.2, 1.3]])
    np.testing.assert_allclose(MODULE.dense_layer(inputs, weights, bias), expected)


def test_pairwise_scores() -> None:
    queries = np.array([[1.0, 0.0], [0.0, 1.0]])
    keys = np.array([[1.0, 2.0], [3.0, 4.0], [-1.0, 1.0]])
    expected = np.array([[1.0, 3.0, -1.0], [2.0, 4.0, 1.0]])
    np.testing.assert_allclose(MODULE.pairwise_scores(queries, keys), expected)
