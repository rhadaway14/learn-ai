# Lesson 07 Exercises — Backpropagation From Scratch

Complete these exercises after the [interactive lesson](index.html). No programming is required.

## Exercise 1 — Forward and backward trace

For:

$$
m=xw,\qquad p=m+b,\qquad y=p^2
$$

use x = −2, w = 4, and b = 3.

### Forward

| Node | Calculation | Value |
|---|---|---:|
| m | | |
| p | | |
| y | | |

### Backward

| Gradient | Upstream gradient | Local derivative | Result |
|---|---:|---:|---:|
| ∂y/∂y | | | |
| ∂y/∂p | | | |
| ∂y/∂m | | | |
| ∂y/∂b | | | |
| ∂y/∂x | | | |
| ∂y/∂w | | | |

Explain what the signs of ∂y/∂w and ∂y/∂b tell gradient descent.

## Exercise 2 — Chain rule through three operations

Let:

$$
u=3x,qquad v=u-2,qquad y=v^3
$$

At x = 2:

1. calculate u, v, and y;
2. calculate $dy/dv$;
3. calculate $dv/du$;
4. calculate $du/dx$; and
5. multiply the local derivatives to obtain $dy/dx$.

Then explain why addition by −2 affects the forward value but has local derivative 1.

## Exercise 3 — Activation gradient gates

An activation receives upstream gradient 4. Calculate the downstream gradient for:

1. ReLU at z = −2;
2. ReLU at z = 3;
3. sigmoid whose forward output is 0.5;
4. sigmoid whose forward output is 0.99; and
5. tanh whose forward output is 0.8.

Explain which cases block or strongly shrink the signal.

## Exercise 4 — Branch accumulation

Let:

$$
y=x^3+2x^2-5x
$$

1. Identify the three paths from x to y.
2. Calculate each path's derivative contribution.
3. Sum them to obtain dy/dx.
4. Evaluate the contributions and total at x = 2.
5. Show the incorrect result if an implementation overwrites the buffer with only the last path.

## Exercise 5 — Tensor gradient shapes

A dense layer uses:

- X shaped `(32, 10)`;
- W shaped `(10, 64)`;
- b shaped `(64)`; and
- Z = XW + b shaped `(32, 64)`.

Fill in:

| Gradient | Shape | What it describes |
|---|---|---|
| ∂L/∂Z | | |
| ∂L/∂X | | |
| ∂L/∂W | | |
| ∂L/∂b | | |

Explain why ∂L/∂b sums contributions across the batch axis while retaining one value per output feature.

## Exercise 6 — Gradient buffer state

A parameter begins at w = 2 with gradient buffer 0 and learning rate 0.1. Three independent batch gradients are +3, −1, and +4.

### Correct independent-batch behavior

Clear before each batch, run backward, and step. Record the weight after each step.

### Forgotten-zero behavior

Never clear the buffer. Let each backward call add into it, then step after each batch. Record each buffer and weight.

Compare the final weights and explain the bug.

## Exercise 7 — Intentional microbatch accumulation

Four equal-sized microbatches produce mean-loss gradients 2, 4, 6, and 8. You want the gradient of the mean loss across the combined effective batch.

1. What result should be applied?
2. What happens if the four mean gradients are summed without normalization?
3. How could you scale each microbatch loss or the final accumulated gradient correctly?
4. How would the answer change if microbatch sizes were unequal?

## Exercise 8 — Gradient check

For:

$$
y=(xw+b)^2
$$

at x = 2, w = 3, b = 1:

1. derive ∂y/∂w analytically;
2. use centered finite differences with $\epsilon=0.01$;
3. compare the results; and
4. explain why an epsilon that is extremely large or extremely small can reduce the check's usefulness.

## Exercise 9 — Diagnose failures

For each symptom, give a plausible cause and next check:

1. An earlier layer's parameters have no gradients at all.
2. Gradient norms grow until values become non-finite.
3. A shared parameter receives only one branch's contribution.
4. Results depend on how many earlier batches ran.
5. Full-batch and microbatch-accumulated updates differ greatly.
6. A parameter gradient's shape does not match the parameter.

## Capstone worksheet — Backward-pass and gradient-state contract

### A. Select the trace

| Item | Your answer |
|---|---|
| Lesson 6 architecture | |
| Representative input | |
| Selected output | |
| Target | |
| Scalar loss | |

### B. Forward graph

List every operation in dependency order.

| Node | Operation | Input shapes | Output shape | Forward value or example |
|---|---|---|---|---|
| | | | | |

### C. Backward graph

List nodes in reverse topological order.

| Node | Upstream gradient | Local derivative rule | Downstream gradient | Gradient shape |
|---|---|---|---|---|
| | | | | |

### D. Branch and state rules

| Rule | Your design |
|---|---|
| Where graph branches rejoin | |
| How branch contributions combine | |
| When gradient buffers are cleared | |
| Whether microbatches accumulate | |
| How accumulated gradients are normalized | |
| When the optimizer applies updates | |
| Any intentional stop-gradient boundary | |

### E. Verification

Choose one parameter element and record:

- analytical gradient;
- centered finite-difference estimate;
- epsilon;
- absolute or relative difference;
- acceptable tolerance; and
- corrective action if the check fails.

Finish by naming the activation-gradient and gradient-norm telemetry Lesson 9 should collect during real training.
