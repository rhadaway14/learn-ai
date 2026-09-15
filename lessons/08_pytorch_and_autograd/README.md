# Lesson 08 — PyTorch and Autograd

## Why this matters

PyTorch turns tensor programs into differentiable training systems and portable model artifacts.

## Learning outcomes

- Explain and apply tensors, devices, and dtypes.
- Explain and apply requires_grad and autograd.
- Explain and apply nn.Module and optimizers.
- Explain and apply train and eval modes plus checkpoints.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Tensors, devices, and dtypes** — identify its inputs, outputs, assumptions, and role.
2. **Requires_grad and autograd** — identify its inputs, outputs, assumptions, and role.
3. **Nn.module and optimizers** — identify its inputs, outputs, assumptions, and role.
4. **Train and eval modes plus checkpoints** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/08_pytorch_and_autograd/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Rebuild Lesson 01 in PyTorch and compare its learned parameters with NumPy.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Device or dtype mismatches fail loudly while forgotten train or eval mode can fail quietly.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Write the canonical zero_grad, forward, loss, backward, step loop and explain its order.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What does backward compute?
2. Why use model.eval?
3. What belongs in a state dictionary?

## Connection to modern AI

Most open-model research and training systems expose PyTorch-compatible weights and operations.

## Explain it at two levels

- **Plain language:** explain the purpose without equations or framework names.
- **Technical:** explain the mechanism, shapes or state, assumptions, metric, and failure mode.

## Definition of done

- [ ] Lab executed and output understood
- [ ] Primary experiment recorded
- [ ] Exercise completed before reviewing the solution
- [ ] Failure mode reproduced or analyzed
- [ ] Checkpoint answered in your own words
- [ ] Plain-language and technical explanations written
