"""Run this after implementing exercises.py.

This intentionally lives outside the main CI suite: the starter exercises are
supposed to be incomplete, while reference implementations are tested by CI.
"""

import numpy as np

from exercises import (
    cosine_similarity,
    dense_layer,
    dot_product,
    pairwise_scores,
    vector_magnitude,
)


def main() -> None:
    assert np.isclose(vector_magnitude(np.array([3.0, 4.0])), 5.0)
    assert np.isclose(
        dot_product(np.array([1.0, 2.0, 3.0]), np.array([4.0, -1.0, 2.0])),
        8.0,
    )

    a = np.array([1.0, 2.0])
    b = np.array([2.0, 1.0])
    assert np.isclose(cosine_similarity(a, b), cosine_similarity(10 * a, b))

    inputs = np.array([[1.0, 2.0], [3.0, 4.0]])
    weights = np.array([[1.0, 0.0, -1.0], [0.5, 2.0, 1.0]])
    bias = np.array([0.1, 0.2, 0.3])
    expected_layer = np.array([[2.1, 4.2, 1.3], [5.1, 8.2, 1.3]])
    np.testing.assert_allclose(dense_layer(inputs, weights, bias), expected_layer)

    queries = np.array([[1.0, 0.0], [0.0, 1.0]])
    keys = np.array([[1.0, 2.0], [3.0, 4.0], [-1.0, 1.0]])
    expected_scores = np.array([[1.0, 3.0, -1.0], [2.0, 4.0, 1.0]])
    np.testing.assert_allclose(pairwise_scores(queries, keys), expected_scores)
    print("Lesson 02 exercises passed.")


if __name__ == "__main__":
    main()
