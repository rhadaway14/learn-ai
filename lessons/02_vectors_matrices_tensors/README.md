# Lesson 02 — The Shapes of AI Data

## Start here

Open [index.html](index.html) in a browser. The complete lesson is visual and interactive. It requires no Python, terminal, installation, account, or internet connection.

Lesson 2 builds the mathematical vocabulary used throughout neural networks, embeddings, attention, image models, and language models. The goal is not memorizing notation. The goal is answering two engineering questions reliably:

1. What does each axis mean?
2. Are the shapes compatible with the intended operation?

## Prerequisites

You should be able to:

- add and multiply ordinary numbers;
- understand that an ordered list keeps values in specific positions;
- explain the Lesson 1 terms feature, model, prediction, and parameter.

No linear-algebra or programming background is assumed.

## Learning outcomes

After completing the lesson, you should be able to:

- distinguish scalars, vectors, matrices, and higher-rank tensors;
- distinguish tensor rank from tensor shape;
- attach semantic names to axes;
- perform and explain element-wise vector operations;
- calculate vector magnitude and a dot product;
- determine whether two matrix shapes can multiply;
- calculate an individual matrix-multiplication cell;
- explain transpose and broadcasting;
- explain how a dense neural-network layer uses matrix multiplication and bias;
- compare dot product, Euclidean distance, and cosine similarity;
- interpret a transformer activation shape such as `(8, 128, 768)`.

## Scalars, vectors, matrices, and tensors

A **scalar** is one number. Loss in Lesson 1 was a scalar.

A **vector** is an ordered one-axis collection of numbers. One vector might describe a house using size, bedrooms, and age. The order and units are part of its meaning.

A **matrix** is a two-axis collection. A table containing examples as rows and features as columns can be represented as a matrix.

A **tensor** is the general term for a numeric collection with zero or more axes. Scalars, vectors, and matrices are all tensors. In practice, people often say “tensor” especially when an object has three or more axes.

| Object | Tensor rank | Example shape | Possible meaning |
|---|---:|---:|---|
| Scalar | 0 | `()` | One loss value |
| Vector | 1 | `(3,)` | One example with three features |
| Matrix | 2 | `(4, 3)` | Four examples with three features each |
| Rank-3 tensor | 3 | `(8, 128, 768)` | Sequences, token positions, values per token |
| Rank-4 tensor | 4 | `(32, 3, 224, 224)` | Images, color channels, height, width |

### What a token means in this lesson

A language model cannot operate directly on the sentence you type. A **tokenizer** first divides the text into pieces selected from that model's vocabulary. A token can be:

- a whole word;
- part of a word;
- punctuation;
- whitespace or a whitespace-plus-word combination;
- a special marker added by the model or application.

For illustration, a tokenizer might divide `unbelievable!` into pieces resembling:

> `un` · `believ` · `able` · `!`

The exact split and numeric IDs depend on the tokenizer. The example should not be treated as the output of every model.

Each vocabulary piece receives an integer **token ID**. The model uses that ID to look up an initial vector called a token embedding. As the vector passes through transformer layers, it becomes a context-sensitive hidden representation. Therefore these are different things:

| Term | Meaning |
|---|---|
| Token | One model-specific piece of the input sequence |
| Token ID | The integer used to identify that vocabulary piece |
| Token position | The ordered slot occupied by the token in a sequence |
| Token embedding | The initial learned vector retrieved for the token ID |
| Hidden vector | The representation at that position after some model processing |

One token does **not** necessarily equal one word. “128 token positions” means 128 ordered model-input slots, not necessarily 128 words.

## Rank, shape, and meaning

**Rank** answers “how many axes?”

**Shape** answers “how long is every axis, in order?”

Shape `(4, 3)` tells us there are two axes with lengths 4 and 3. It does not tell us whether those axes mean customers and features, documents and terms, or something else.

Axis semantics are a contract. Two components can agree that a tensor has shape `(32, 8)` while disagreeing about whether the first axis means examples or features. The computation may run and still be wrong.

## Vectors

A vector can represent:

- input features for one example;
- a learned embedding;
- activations inside a model;
- gradients for several parameters;
- probabilities across categories.

### Element-wise operations

Element-wise addition combines matching positions:

$$
[1,2,3]+[4,5,6]=[5,7,9]
$$

This assumes corresponding positions have compatible meaning. Adding `[height, age]` to `[temperature, income]` is numerically possible but semantically meaningless.

Addition is relevant because models frequently need to preserve and combine compatible signals:

- a transformer adds a token embedding and position embedding so the vector carries both token identity and location;
- a residual connection adds a layer's input back to its output, preserving a direct information path;
- a bias vector adds one learned adjustment to each output feature across a batch.

The crucial word is **compatible**. Vector addition assumes the same position in both vectors refers to the same learned coordinate or feature.

Scaling multiplies every component by one scalar:

$$
2[1,2,3]=[2,4,6]
$$

### Magnitude

Magnitude measures vector length from the origin. For `[3, 4]`:

1. Square the components: `9` and `16`.
2. Add them: `25`.
3. Take the square root: `5`.

The symbolic form compresses those steps:

$$
\lVert x\rVert_2=\sqrt{\sum_i x_i^2}
$$

The subscript `2` names the L2 or Euclidean norm. The lesson's magnitude interaction lets you change components and see the geometric length.

Magnitude is relevant because it measures overall scale:

- cosine similarity divides by magnitudes so it compares direction rather than raw size;
- gradient magnitude describes the size of a proposed parameter update;
- extremely large activation or gradient magnitudes can signal unstable training;
- normalization methods control scale so later calculations behave more predictably.

Magnitude does not, by itself, explain what a vector means. Different vectors can have the same length while pointing in completely different directions.

## Dot product

The dot product takes two equally long vectors and produces one scalar:

1. multiply values at matching positions;
2. add all of those products.

For `[1, 2, 3]` and `[4, −1, 2]`:

> `(1 × 4) + (2 × −1) + (3 × 2) = 8`

Symbolically:

$$
a\cdot b=\sum_i a_i b_i
$$

Positive paired components raise the score. Opposing signs lower it. The result combines alignment with magnitude.

Reducing many component comparisons to one score is useful whenever a model must rank, activate, or choose:

- a neuron compares an input vector with its learned weight vector;
- a retrieval system ranks a document vector against a query vector;
- attention compares one token position's query with other positions' keys;
- a classifier produces one score, or logit, for each possible category.

A large dot product may result from close directional alignment, large vector magnitudes, or both. If magnitude should not affect the comparison, normalize the vectors or use cosine similarity.

Dot products appear throughout AI:

- a neuron forms a weighted sum of inputs;
- attention scores query-key alignment;
- similarity systems compare vector representations;
- matrix multiplication organizes many dot products at once.

## Matrices

A matrix has rows and columns. In a data matrix, rows often represent examples and columns represent features—but never assume this without checking the contract.

### What a transformation means

A transformation maps a vector from one representation to another. Matrix multiplication mixes the input components using learned weights. It can change both the number and interpretation of the components.

For example, a vector with 10 measured input features can be transformed into 8 learned features. Each output feature is a different weighted combination of all 10 inputs. In a transformer, separate learned matrices transform each token's hidden vector into query, key, and value vectors.

Geometrically, matrices can stretch, shrink, rotate, reflect, and combine directions. In machine learning, training adjusts those transformations until the resulting representation helps minimize the task's loss. The matrix does not automatically know the desired meaning; that behavior emerges from the learned weights and training objective.

### Matrix multiplication

Matrix multiplication is not element-wise multiplication. Each result cell is a dot product between:

- one row from the left matrix;
- one column from the right matrix.

For shapes:

$$
(m\times n)(n\times p)\rightarrow(m\times p)
$$

The two `n` dimensions must match because both identify the number of values participating in each dot product. That shared dimension is consumed. The outside dimensions determine the output shape.

Example:

> `(2, 3) × (3, 4) → (2, 4)`

There will be two output rows and four output columns, and every output cell combines three paired values.

The interactive cell inspector shows the exact row-column calculation for every result cell.

## Transpose

Transposing a matrix swaps its two axes. A `(2, 3)` matrix becomes `(3, 2)`:

- the first original row becomes the first new column;
- the second original row becomes the second new column;
- no value is discarded.

Transpose is important when vectors are stored in the wrong orientation for an intended dot product. Attention later computes query-key scores using a transposed key matrix.

## Broadcasting

Broadcasting applies a compatible smaller tensor across a larger one without manually copying it.

Suppose a neural-network layer produces shape `(4, 3)`:

- 4 examples;
- 3 output features per example.

A bias vector with shape `(3,)` contains one adjustment for each output feature. Broadcasting adds that same three-value vector to all four rows. The output remains `(4, 3)`.

Broadcasting is convenient, but an accidentally compatible shape can hide a semantic defect. A robust system names axes, checks shapes at boundaries, and tests known examples.

## Dense neural-network layers

A dense layer transforms a batch of input vectors:

$$
Y=XW+b
$$

Read it in words:

> output = input batch × weight matrix + bias vector

If:

- input batch `X` has shape `(32, 10)`;
- weights `W` have shape `(10, 8)`;
- bias `b` has shape `(8,)`;

then:

1. `(32, 10) × (10, 8)` produces `(32, 8)`;
2. the `(8,)` bias broadcasts across all 32 rows;
3. the final output shape is `(32, 8)`.

The 10 input features have been transformed into 8 learned output features for each example.

## Embeddings and similarity

An embedding maps an object to a vector. The object might be a token, document, image, product, user, or graph node. Training arranges the vector space so geometry is useful for a particular objective.

### Dot product

Sensitive to both direction and magnitude. Scaling one vector changes the score.

### Euclidean distance

Measures straight-line distance between vector endpoints. Scaling or shifting affects it.

### Cosine similarity

Compares direction while normalizing both vector lengths:

$$
\cos(\theta)=\frac{a\cdot b}{\lVert a\rVert\lVert b\rVert}
$$

- `1` means the same direction;
- `0` means a right angle;
- `−1` means opposite directions.

The similarity interaction demonstrates that resizing a vector changes its dot product and distance while cosine similarity remains fixed if direction does not change.

Similarity is not universal understanding. It reflects the embedding model's training data and objective. Production retrieval also depends on filters, indexing, data quality, reranking, and measured relevance.

## Batches and transformer shapes

AI systems process multiple examples together for efficient hardware use. This introduces a batch axis.

A common language-model activation shape is:

> `(batch, sequence, hidden)`

For `(8, 128, 768)`:

- 8 sequences are processed together;
- each sequence has 128 token positions;
- each position has a 768-value learned representation.

The middle axis contains ordered token positions. A token begins as a vocabulary ID, while the 768-number vector is the model's current representation at that position. The vector can change across layers as surrounding tokens contribute context, even though the position still refers to the same original input slot.

The tensor contains `8 × 128 × 768 = 786,432` numeric activations.

Transformer layers use matrix multiplication to produce query, key, and value vectors at each token position. Query-key dot products then produce attention scores. Lesson 13 will build that operation using the foundations taught here.

## Interactive practice sequence

Complete these in [index.html](index.html):

1. Change tensor rank and interpret shape.
2. Identify an axis in a transformer-shaped tensor.
3. Add and scale vectors.
4. Construct vector magnitude geometrically.
5. Change dot-product components and explain the score.
6. Validate compatible and incompatible matrix shapes.
7. Inspect every cell of a matrix product.
8. Transpose a matrix.
9. Apply one broadcast bias across a batch.
10. Compare embedding similarity measures.
11. Configure and explain a transformer activation tensor.

## Common failures

### Inner dimensions do not match

The row and column used for an output dot product have different lengths. Recheck orientation and whether a transpose is intended.

### Shape is valid but meaning is wrong

Axes or component order were swapped. Attach semantic names and test a small known example.

### Broadcasting silently changes the wrong axis

The smaller shape is numerically compatible but not semantically intended. Assert the expected output and axis roles.

### High similarity is treated as proof of relevance

The embedding or distance function may not represent the task well. Evaluate retrieval on labeled queries and expected evidence.

### A zero vector is used with cosine similarity

Its magnitude is zero, so division by both magnitudes is undefined.

## Capstone increment

Create a data-shape contract for the future AI delivery advisor. Name and describe:

- one raw input example;
- one document or evidence representation;
- one embedding vector;
- one batch of embeddings;
- one retrieval-result set;
- the expected shape and meaning of every axis.

Include at least one invalid shape example and explain how the system will detect it.

## Knowledge checkpoint

1. How do scalar, vector, matrix, and tensor relate?
2. How do rank and shape differ?
3. Why is axis meaning not contained in shape alone?
4. What does vector magnitude measure?
5. How is a dot product calculated and what does it produce?
6. Why must matrix-multiplication inner dimensions match?
7. What happens to shape during transpose?
8. Why can a bias vector broadcast across a batch?
9. How do dot product, distance, and cosine similarity differ?
10. Interpret `(16, 256, 1,024)` for an LLM activation tensor.
11. Where do matrix multiplication and dot products appear in attention?

## Speak about it confidently

Plain-language version:

> AI systems organize numbers into multidimensional collections whose axes carry specific meaning. Vectors describe individual objects, matrices organize and transform batches, and tensors generalize these structures. Shape compatibility determines whether operations are possible, while axis meaning determines whether they are correct.

Technical version:

> Tensor rank counts axes and shape gives each axis length. Dense layers transform `(batch, input)` by `(input, output)` weights, then broadcast an `(output,)` bias. Dot products produce weighted alignment scores, matrix multiplication computes many such scores, and cosine similarity normalizes dot product by vector magnitudes. Transformer activations commonly use `(batch, sequence, hidden)` layouts.

## Definition of done

- [ ] Complete every embedded interaction.
- [ ] Answer all three knowledge checks correctly.
- [ ] Explain rank, shape, and axis meaning without notes.
- [ ] Calculate a dot product by hand.
- [ ] Validate matrix multiplication from shapes.
- [ ] Explain broadcasting with a batch-and-bias example.
- [ ] Compare cosine similarity, dot product, and distance.
- [ ] Interpret a transformer tensor shape.
- [ ] Produce the capstone data-shape contract.
- [ ] Mark Lesson 2 complete in the course interface.

## Instructor note

The learner-facing path is the browser lesson. Tested numerical reference files remain in the repository for maintainers; learners are not required to read or execute them.
