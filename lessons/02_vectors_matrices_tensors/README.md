# Lesson 02 — Vectors, Matrices, and Tensors

## Why this lesson matters

Modern AI is largely organized numerical computation. Tokens become vectors, collections of vectors become matrices, batches become higher-dimensional tensors, and model layers transform them with matrix multiplication.

You do not need to become a mathematician before building AI systems. You do need to be comfortable answering two questions:

1. What does each axis represent?
2. Are the shapes compatible with the operation?

Shape errors are the compiler errors of machine learning—except they often arrive after the expensive GPU job starts, because the universe enjoys timing.

## 1. Scalars, vectors, matrices, tensors

| Object | Example shape | Interpretation |
|---|---:|---|
| Scalar | `()` | One number, such as loss |
| Vector | `(3,)` | One ordered feature or embedding vector |
| Matrix | `(4, 3)` | Four examples, each with three features |
| Rank-3 tensor | `(8, 128, 768)` | Eight sequences, 128 tokens each, 768 values per token |
| Rank-4 tensor | `(32, 3, 224, 224)` | Image batch: batch, channels, height, width |

A **tensor** is the general term for a multidimensional numeric array. In this course, **rank** means the number of axes. A tensor's `shape` gives the size of each axis.

```python
scalar.shape       # ()
vector.shape       # (3,)
matrix.shape       # (4, 3)
token_batch.shape  # (8, 128, 768)
```

Be careful: “rank” can also mean matrix rank in linear algebra. Context determines which meaning is intended.

## 2. Vectors

A vector can represent many things:

- a row of input features: `[square_feet, bedrooms, age]`;
- a learned embedding for a word, image, or document;
- the activations within one neural-network layer;
- a gradient indicating how parameters should change.

Vector addition is element-wise:

$$
[1,2,3]+[4,5,6]=[5,7,9]
$$

Multiplication by a scalar scales every component:

$$
2[1,2,3]=[2,4,6]
$$

### Magnitude

The Euclidean magnitude (L2 norm) is:

$$
\|x\|_2=\sqrt{\sum_i x_i^2}
$$

For `[3, 4]`, the magnitude is `5`.

### Dot product

For equal-length vectors:

$$
a\cdot b=\sum_i a_i b_i
$$

The dot product combines corresponding components into one scalar. It is both a weighted sum and a measure connected to alignment. Neural-network neurons and attention scores rely on this operation.

## 3. Matrices and matrix multiplication

A matrix is a two-dimensional arrangement of values. If a batch contains 100 examples with 4 features each, its shape is `(100, 4)`.

Matrix multiplication is not element-wise multiplication:

$$
(m\times n)(n\times p)\rightarrow(m\times p)
$$

The inner dimensions must match.

Suppose `X` is a batch with shape `(batch, input_features)`, `W` has shape `(input_features, output_features)`, and `b` has shape `(output_features,)`:

$$
Y=XW+b
$$

Then `Y` has shape `(batch, output_features)`. That equation is the computational core of a dense neural-network layer.

NumPy's `@` operator performs matrix multiplication:

```python
output = inputs @ weights + bias
```

## 4. Transpose

Transposing a 2D matrix swaps its axes:

```python
matrix.shape    # (2, 3)
matrix.T.shape  # (3, 2)
```

Transpose becomes important whenever examples and features are oriented differently, and later when attention computes `Q @ K.T`.

## 5. Broadcasting

Broadcasting lets NumPy apply compatible smaller arrays across larger ones. In:

```python
output = inputs @ weights + bias
```

`inputs @ weights` might be `(32, 8)`, while `bias` is `(8,)`. NumPy adds the same bias vector to each of the 32 rows.

Broadcasting is convenient, but an accidentally compatible shape can silently calculate the wrong thing. Always attach semantic names to axes.

## 6. Embeddings and similarity

An embedding maps an object to a vector. Similar meanings should be represented by vectors that point in similar directions.

Cosine similarity is:

$$
\cos(\theta)=\frac{a\cdot b}{\|a\|\|b\|}
$$

It ranges from `-1` to `1` for nonzero real vectors:

- `1`: same direction;
- `0`: orthogonal;
- `-1`: opposite direction.

Cosine similarity cares about direction rather than magnitude. That is often desirable in semantic retrieval, although production retrieval decisions also involve model quality, normalization, distance metric, indexing, filtering, and reranking.

## 7. Connection to transformers

A language model might represent a batch as:

```text
(batch_size, sequence_length, hidden_dimension)
```

For `(8, 128, 768)`:

- 8 sequences are processed together;
- each sequence contains 128 token positions;
- each token is represented by 768 values.

Linear projections turn those token representations into queries, keys, and values. Attention later computes a scaled form of:

$$
QK^T
$$

The dot products express how strongly each token's query aligns with each token's key. We will derive and implement this in the attention lesson.

## Lab

Run:

```bash
python lessons/02_vectors_matrices_tensors/lab.py
```

Then open `outputs/vectors_and_transformations.png`.

Complete each `TODO` in `exercises.py`, then run the learner check:

```bash
python lessons/02_vectors_matrices_tensors/check_exercises.py
```

Only compare with `solutions.py` after making a serious attempt. The repository's normal `pytest` suite verifies the reference implementation and should remain green even while your learner exercises are intentionally incomplete.

## Experiments

1. Change the feature vector and dense-layer weights. Predict the output shape and values first.
2. Multiply one embedding by `10`. Compare dot product, Euclidean distance, and cosine similarity before and after scaling.
3. Add a second example to the dense-layer batch. Verify the weights do not change shape.
4. Intentionally try `(2, 3) @ (4, 2)`. Read the error and explain the inner-dimension mismatch.

## Knowledge checkpoint

Answer without looking back:

1. What is the difference among a scalar, vector, matrix, and tensor?
2. What does tensor rank mean here, and how is it different from shape?
3. Why must the inner dimensions match during matrix multiplication?
4. Why does a dense layer use matrix multiplication?
5. What does a dot product produce, and where does it appear in AI?
6. Why can cosine similarity remain unchanged when a vector is scaled?
7. Interpret `(16, 256, 1024)` for an LLM activation tensor.
8. What operation allows one bias vector to be added to every example in a batch?

## Speak about it confidently

You should now be able to say:

> AI models represent inputs and internal states as tensors. Dense layers transform batches of vectors using matrix multiplication plus a broadcast bias. Embeddings encode objects as vectors, and similarity functions such as cosine similarity compare their direction. In transformer models, rank-3 tensors commonly represent batches of token sequences, with a learned vector at every token position.

## What comes next

Lesson 03 will deepen the training loop: loss surfaces, analytical and numerical gradients, batch versus stochastic gradient descent, learning-rate behavior, and common optimizers.
