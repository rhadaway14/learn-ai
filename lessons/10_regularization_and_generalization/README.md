# Lesson 10 — Regularization and Generalization

## Why this matters

Generalization requires controlling capacity, data quality, and optimization rather than merely lowering training loss.

## Learning outcomes

- Explain and apply bias-variance tradeoff.
- Explain and apply L1 and L2 regularization.
- Explain and apply dropout and augmentation.
- Explain and apply normalization and early stopping.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Bias-variance tradeoff** — identify its inputs, outputs, assumptions, and role.
2. **L1 and l2 regularization** — identify its inputs, outputs, assumptions, and role.
3. **Dropout and augmentation** — identify its inputs, outputs, assumptions, and role.
4. **Normalization and early stopping** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/10_regularization_and_generalization/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Fit high-degree polynomials with several L2 penalties and compare train and test error.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Excessive regularization underfits while inadequate regularization memorizes noise.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Design a learning-curve experiment that distinguishes data shortage from insufficient capacity.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. How does L2 affect weights?
2. Why is dropout disabled during inference?
3. What does a learning curve reveal?

## Connection to modern AI

Fine-tuning can overfit tiny instruction datasets just as ordinary models overfit.

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
