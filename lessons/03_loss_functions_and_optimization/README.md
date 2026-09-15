# Lesson 03 — Loss Functions and Optimization

## Why this matters

Training needs a scalar objective and a reliable way to reduce it.

## Learning outcomes

- Explain and apply MSE, MAE, and cross-entropy.
- Explain and apply loss surfaces and local slope.
- Explain and apply analytical and finite-difference gradients.
- Explain and apply batch, stochastic, and mini-batch descent.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Mse, mae, and cross-entropy** — identify its inputs, outputs, assumptions, and role.
2. **Loss surfaces and local slope** — identify its inputs, outputs, assumptions, and role.
3. **Analytical and finite-difference gradients** — identify its inputs, outputs, assumptions, and role.
4. **Batch, stochastic, and mini-batch descent** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/03_loss_functions_and_optimization/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Try learning rates 0.001, 0.15, 0.7, and 1.1 and graph parameter and loss trajectories.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A large learning rate oscillates or diverges while a tiny one looks stable but makes negligible progress.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Implement central finite differences for a two-parameter function and compare with its analytical gradient.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why must an ordinary gradient-based objective be differentiable?
2. What do gradient sign and magnitude mean?
3. When would MAE be preferable to MSE?

## Connection to modern AI

Every trained neural network still optimizes a scalar objective.

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
