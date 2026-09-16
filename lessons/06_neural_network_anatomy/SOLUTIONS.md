# Lesson 06 Reference Notes — Neural Network Anatomy

Review these notes after attempting the exercises.

## Exercise 1

Weighted contributions are 1.5, −2.5, and −1.0. Adding bias gives:

$$
z=1.5-2.5-1.0+0.75=-1.25
$$

ReLU outputs 0. If $w_2=-1.25$, the second contribution becomes +2.5 and z becomes 3.75, so ReLU outputs 3.75. The bias is a learned offset that shifts the response independently of the current input values.

## Exercise 2

Approximate values:

| z | ReLU | sigmoid | tanh | linear |
|---:|---:|---:|---:|---:|
| −4 | 0 | 0.018 | −0.999 | −4 |
| −1 | 0 | 0.269 | −0.762 | −1 |
| 0 | 0 | 0.500 | 0 | 0 |
| 1 | 1 | 0.731 | 0.762 | 1 |
| 4 | 4 | 0.982 | 0.999 | 4 |

Sigmoid and tanh saturate at both extremes. ReLU has zero slope on its negative side. Linear output is common for unrestricted regression. Sigmoid maps a binary logit into 0–1 but can shrink gradients through repeated saturated hidden layers.

## Exercise 3

- Input: `(20, 12)`
- Weights: `(12, 8)`
- Bias: `(8)`
- Pre-activation and activated output: `(20, 8)`
- Weights: 96
- Biases: 8
- Total parameters: 104

Batch size 200 changes activation shapes to `(200, 12)` and `(200, 8)` but parameter count remains 104. The same learned layer processes more examples.

## Exercise 4

| Layer | Input | Weights | Bias | Pre-activation | Output | Parameters |
|---|---|---|---|---|---|---:|
| Dense 1 + ReLU | `(32, 10)` | `(10, 64)` | `(64)` | `(32, 64)` | `(32, 64)` | 704 |
| Dense 2 + ReLU | `(32, 64)` | `(64, 16)` | `(16)` | `(32, 16)` | `(32, 16)` | 1,040 |
| Output | `(32, 16)` | `(16, 3)` | `(3)` | `(32, 3)` | `(32, 3)` | 51 |

Total parameters are 1,795. The largest activation tensor is `(32, 64)`, containing 2,048 values.

## Exercise 5

$$
y=3(4x-2)+5=12x-6+5=12x-1
$$

The composition is one linear map with weight 12 and bias −1. Any finite stack of affine transformations can be algebraically composed into one affine transformation. A nonlinear activation prevents that reduction and lets the representation bend or fold.

## Exercise 6

| x₁ | x₂ | h₁ | h₂ | sum | XOR |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |

The hidden layer creates new features expressing directional disagreement. The output can then separate the pattern using those features.

## Exercise 7

- Engineer-hours: one linear output for an unrestricted numeric estimate.
- Late/on time: one logit followed by sigmoid for a positive-class score, then a threshold.
- Three mutually exclusive routes: three logits followed by softmax.
- Twelve independent tags: twelve logits, each with its own sigmoid, because several tags may apply simultaneously.

## Exercise 8

Strong diagnoses connect observations to measurements:

- Poor train and validation: insufficient capacity, weak features, unsuitable optimization, or noisy labels; inspect training loss against the baseline and data quality.
- Good train but degrading validation: overfitting, leakage in tuning, or distribution mismatch; inspect learning curves and slices.
- Mostly zero ReLUs: negative pre-activations or dead units; inspect pre-activation and gradient distributions.
- Extreme sigmoid values: saturation; inspect pre-activation scale and gradient magnitudes.
- Shape error: adjacent widths or storage convention mismatch; write every named axis and expected multiplication.

## Capstone quality bar

A strong contract:

- preserves the Lesson 5 target and evaluation rather than changing success criteria;
- names every tensor axis;
- makes every adjacent dimension compatible;
- includes every bias and parameter count;
- justifies nonlinearity and output head from the task;
- keeps batch-dependent activation size separate from learned parameter count;
- defines observable failure signals; and
- permits the simpler baseline to win if the neural candidate does not add held-out value.
