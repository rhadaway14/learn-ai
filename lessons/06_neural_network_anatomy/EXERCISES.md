# Lesson 06 Exercises — Neural Network Anatomy

Complete these exercises after the [interactive lesson](index.html). No programming is required.

## Exercise 1 — Calculate one neuron

A neuron receives:

- $x_1=3$ with $w_1=0.5$;
- $x_2=-2$ with $w_2=1.25$;
- $x_3=4$ with $w_3=-0.25$; and
- bias $b=0.75$.

1. Calculate each weighted contribution.
2. Calculate pre-activation z.
3. Calculate the output for ReLU.
4. State how the result changes if $w_2$ changes from 1.25 to −1.25.
5. Explain the role of the bias without saying it is “just another weight.”

## Exercise 2 — Compare activations

Complete the approximate outputs:

| z | ReLU(z) | sigmoid(z) | tanh(z) | linear(z) |
|---:|---:|---:|---:|---:|
| −4 | | | | |
| −1 | | | | |
| 0 | | | | |
| 1 | | | | |
| 4 | | | | |

Then answer:

1. Which activations saturate at both extremes?
2. Which activation has zero local slope for negative inputs?
3. Which activation is suitable for an unrestricted regression output?
4. Why is sigmoid useful for a binary output but risky in many deep hidden layers?

Use the activation explorer to verify your reasoning.

## Exercise 3 — Trace one dense layer

A batch contains 20 examples with 12 input features. A dense layer has 8 neurons.

Fill in:

| Object | Shape | Meaning |
|---|---|---|
| Input X | | |
| Weights W | | |
| Bias b | | |
| Pre-activation Z | | |
| Activated output A | | |

Calculate the number of weights, biases, and total learned parameters. Then repeat the parameter calculation for batch size 200 and explain why it does or does not change.

## Exercise 4 — Trace the complete network

Trace a batch of shape `(32, 10)` through widths `10 → 64 → 16 → 3`.

| Layer | Input | Weights | Bias | Pre-activation | Activation output | Parameters |
|---|---|---|---|---|---|---:|
| Dense 1 + ReLU | | | | | | |
| Dense 2 + ReLU | | | | | | |
| Output | | | | | | |

Calculate the total parameter count and largest activation tensor by number of values.

## Exercise 5 — Prove the linear collapse

Two layers contain no nonlinear activation:

$$
h=4x-2
$$

$$
y=3h+5
$$

1. Substitute h into the second equation.
2. Reduce the result to one weight and one bias.
3. Explain why adding ten more linear-only layers does not solve this limitation.
4. State what a nonlinear activation changes structurally.

## Exercise 6 — Trace XOR hidden features

For each binary input pair, calculate:

$$
h_1=\operatorname{ReLU}(x_1-x_2)
$$

$$
h_2=\operatorname{ReLU}(x_2-x_1)
$$

| x₁ | x₂ | h₁ | h₂ | h₁ + h₂ | XOR target |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | | | | 0 |
| 0 | 1 | | | | 1 |
| 1 | 0 | | | | 1 |
| 1 | 1 | | | | 0 |

Explain why the hidden features succeed where one straight decision boundary fails.

## Exercise 7 — Choose the output head

Choose output width and final activation for each task. Explain every choice.

| Task | Output width | Final activation | Why |
|---|---:|---|---|
| Predict engineer-hours | | | |
| Predict late versus on time | | | |
| Route to billing, security, or platform | | | |
| Assign any applicable tags from 12 possible tags | | | |

## Exercise 8 — Diagnose architecture behavior

For each observation, give at least two plausible causes and the next measurement you would inspect.

1. Training and validation performance both remain near the baseline.
2. Training loss falls while validation performance degrades.
3. Most ReLU outputs in one layer remain zero.
4. Sigmoid hidden activations cluster around 0 and 1.
5. Matrix multiplication reports incompatible shapes.

## Capstone worksheet — Neural architecture and tensor-shape contract

### A. Preserve the decision contract

| Item | Your answer |
|---|---|
| Lesson 5 target | |
| Task type | |
| Naive baseline | |
| Primary held-out metric | |
| Minimum improvement needed | |
| Costly failure that must not regress | |

### B. Define model inputs and outputs

| Item | Your answer |
|---|---|
| Input feature names | |
| Number of input features | |
| Proposed batch size | |
| Input tensor shape | |
| Output width | |
| Output activation | |
| Meaning of each output value | |

### C. Trace every layer

| Layer | Input shape | Weight shape | Bias shape | Activation | Output shape | Parameters |
|---|---|---|---|---|---|---:|
| Hidden 1 | | | | | | |
| Hidden 2 | | | | | | |
| Output | | | | | | |

Record total parameters and the largest activation tensor.

### D. Defend the architecture

Answer:

1. Why is a neural network plausible for this target?
2. What interaction or nonlinear pattern might the baseline miss?
3. Why did you choose these hidden widths?
4. Why did you choose these activations?
5. Why does the output head match the target and Lesson 5 metric?
6. What would indicate dead activations, saturation, underfitting, or overfitting?
7. What evidence would cause you to keep the simpler baseline instead?

This document is the input specification for Lesson 7. Do not implement the network yet.
