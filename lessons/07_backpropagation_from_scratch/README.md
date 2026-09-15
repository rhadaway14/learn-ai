# Lesson 07 — Backpropagation From Scratch

## Why this matters

Backpropagation efficiently applies the chain rule through a computational graph.

## Learning outcomes

- Explain and apply computational graphs.
- Explain and apply local derivatives.
- Explain and apply reverse-mode differentiation.
- Explain and apply gradient accumulation and zeroing.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Computational graphs** — identify its inputs, outputs, assumptions, and role.
2. **Local derivatives** — identify its inputs, outputs, assumptions, and role.
3. **Reverse-mode differentiation** — identify its inputs, outputs, assumptions, and role.
4. **Gradient accumulation and zeroing** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/07_backpropagation_from_scratch/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Build two paths into one value and verify their gradients add.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Incorrect graph order or forgotten gradient resets silently corrupt training.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Differentiate y equals the square of xw plus b manually and verify each leaf gradient with finite differences.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why traverse the graph backward?
2. Why do gradients accumulate?
3. What does stop-gradient do?

## Connection to modern AI

Autograd frameworks automate this graph traversal.

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
