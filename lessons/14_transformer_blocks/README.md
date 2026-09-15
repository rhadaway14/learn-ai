# Lesson 14 — Transformer Blocks

## Why this matters

A transformer block combines attention, token-wise computation, residual streams, and normalization.

## Learning outcomes

- Explain and apply multi-head attention.
- Explain and apply residual connections.
- Explain and apply layer normalization.
- Explain and apply feed-forward networks.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Multi-head attention** — identify its inputs, outputs, assumptions, and role.
2. **Residual connections** — identify its inputs, outputs, assumptions, and role.
3. **Layer normalization** — identify its inputs, outputs, assumptions, and role.
4. **Feed-forward networks** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/14_transformer_blocks/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Ablate residual connections and compare signal norms across many blocks.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Deep stacks without stable residual and normalization design become difficult to optimize.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Trace shapes through a pre-norm decoder block and calculate parameter counts.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why use multiple heads?
2. What does the FFN do?
3. Why are residuals important?

## Connection to modern AI

Stacked transformer blocks form most modern language-model backbones.

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
