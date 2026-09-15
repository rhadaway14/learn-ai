# Lesson 13 — Attention From Scratch

## Why this matters

Attention lets each token dynamically combine information from other permitted token positions.

## Learning outcomes

- Explain and apply queries, keys, and values.
- Explain and apply scaled dot-product attention.
- Explain and apply softmax and masks.
- Explain and apply attention tensor shapes.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Queries, keys, and values** — identify its inputs, outputs, assumptions, and role.
2. **Scaled dot-product attention** — identify its inputs, outputs, assumptions, and role.
3. **Softmax and masks** — identify its inputs, outputs, assumptions, and role.
4. **Attention tensor shapes** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/13_attention_from_scratch/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Remove scaling and increase key dimension then compare softmax entropy.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Missing causal masks leak future tokens and unscaled scores saturate softmax.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Given Q and K shapes B,H,T,D derive score and output shapes.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why divide by the square root of key dimension?
2. What does a causal mask prevent?
3. Why are attention weights not explanations by default?

## Connection to modern AI

Self-attention is the primary token-mixing mechanism in transformers.

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
