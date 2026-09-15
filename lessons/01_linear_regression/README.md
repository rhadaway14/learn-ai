# Lesson 01 — Machine Learning and Linear Regression

## Goal

Understand a model as a parameterized function and train one without a machine-learning framework.

The model is:

\[
\hat{y}=wx+b
\]

Training repeatedly performs a forward pass, calculates mean squared error, calculates gradients, and updates `w` and `b` in the direction that lowers loss.

## Run

From the repository root:

```bash
python lessons/01_linear_regression/train.py
```

The learned relationship should be close to `y = 3.5x + 2`. The exact result differs because the generated data contains noise.

## Experiments

Change one thing at a time:

1. Try learning rates `0.00001`, `0.01`, `0.1`, and `1.0`.
2. Increase the noise standard deviation from `1.5` to `8.0`.
3. Train on only 10 samples.
4. Remove noise.

For every experiment, record what happened to training loss, test loss, and the learned parameters.
