# Lesson 07 Reference Notes — Backpropagation From Scratch

Review these notes after attempting the exercises.

## Exercise 1

Forward:

- m = −2 × 4 = −8
- p = −8 + 3 = −5
- y = (−5)² = 25

Backward:

- ∂y/∂y = 1
- ∂y/∂p = 1 × 2p = −10
- ∂y/∂m = −10 × 1 = −10
- ∂y/∂b = −10 × 1 = −10
- ∂y/∂x = −10 × w = −40
- ∂y/∂w = −10 × x = 20

A positive weight gradient means gradient descent decreases w. A negative bias gradient means it increases b, assuming a positive learning rate.

## Exercise 2

At x = 2:

- u = 6
- v = 4
- y = 64
- dy/dv = 3v² = 48
- dv/du = 1
- du/dx = 3
- dy/dx = 48 × 1 × 3 = 144

Subtracting 2 shifts the forward value, which changes where the cubic derivative is evaluated. But a small change in u still creates the same small change in v, so dv/du = 1.

## Exercise 3

- ReLU at −2: 4 × 0 = 0
- ReLU at 3: 4 × 1 = 4
- Sigmoid output 0.5: derivative 0.5(0.5) = 0.25, downstream = 1
- Sigmoid output 0.99: derivative 0.99(0.01) = 0.0099, downstream = 0.0396
- Tanh output 0.8: derivative 1 − 0.64 = 0.36, downstream = 1.44

Negative ReLU blocks the signal. Saturated sigmoid strongly shrinks it.

## Exercise 4

Path contributions are:

$$
3x^2,\qquad4x,\qquad-5
$$

Therefore:

$$
\frac{dy}{dx}=3x^2+4x-5
$$

At x = 2, contributions are 12, 8, and −5, totaling 15. Keeping only the last path incorrectly reports −5.

## Exercise 5

| Gradient | Shape |
|---|---|
| ∂L/∂Z | `(32, 64)` |
| ∂L/∂X | `(32, 10)` |
| ∂L/∂W | `(10, 64)` |
| ∂L/∂b | `(64)` |

The same bias vector is broadcast to all 32 examples during forward. During backward, each example contributes to each bias element, so contributions sum across the batch axis and leave the output-width axis.

## Exercise 6

Correct independent batches:

- gradient +3: w = 2 − 0.1(3) = 1.7
- gradient −1: w = 1.7 − 0.1(−1) = 1.8
- gradient +4: w = 1.8 − 0.1(4) = 1.4

Without zeroing:

- buffer 3: w = 1.7
- buffer 2: w = 1.7 − 0.2 = 1.5
- buffer 6: w = 1.5 − 0.6 = 0.9

The later updates reuse stale gradients, so they no longer represent their independent batches.

## Exercise 7

For equal-sized microbatches, the combined mean gradient is $(2+4+6+8)\div4=5$. Applying the raw sum 20 makes the update four times too large relative to the desired mean. Divide the final buffer by four or scale each microbatch contribution by one quarter. With unequal sizes, use a sample-count-weighted mean rather than averaging microbatch means equally.

## Exercise 8

Analytically:

$$
\frac{\partial y}{\partial w}=2(xw+b)x=2(7)(2)=28
$$

Centered difference with epsilon 0.01:

$$
\frac{(2(3.01)+1)^2-(2(2.99)+1)^2}{0.02}=28
$$

A large epsilon measures a wide secant rather than local slope. An extremely small epsilon can suffer floating-point cancellation.

## Exercise 9

- Missing earlier gradients: accidental detach, frozen parameters, or blocked activation; inspect graph connectivity and `requires_grad` state in Lesson 8.
- Non-finite growth: exploding gradients or learning rate; inspect per-layer gradient norms and loss scale.
- One branch only: overwrite or wrong graph order; test a known multi-path expression.
- History-dependent results: stale gradient buffers; inspect and clear before independent batches.
- Accumulation mismatch: loss scaling or unequal microbatch weighting; compare effective sample-weighted gradients.
- Shape mismatch: incorrect local matrix rule or transpose convention; assert parameter/gradient shape equality.

## Capstone quality bar

A strong backward-pass contract:

- preserves the Lesson 6 forward architecture;
- reaches one scalar loss;
- records values required by every local derivative;
- multiplies along paths and adds across branches;
- processes dependencies in reverse topological order;
- gives every parameter a same-shaped gradient;
- distinguishes intentional accumulation from stale state;
- verifies at least one parameter numerically; and
- defines observable failure signals before relying on autograd.
