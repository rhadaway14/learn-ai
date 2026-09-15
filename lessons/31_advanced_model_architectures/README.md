# Lesson 31 — Advanced Model Architectures

## Why this matters

New architectures trade computation, memory, context, and inductive bias differently.

## Learning outcomes

- Explain and apply mixture of experts.
- Explain and apply sparse and linear attention.
- Explain and apply state-space models.
- Explain and apply diffusion and multimodal transformers.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Mixture of experts** — identify its inputs, outputs, assumptions, and role.
2. **Sparse and linear attention** — identify its inputs, outputs, assumptions, and role.
3. **State-space models** — identify its inputs, outputs, assumptions, and role.
4. **Diffusion and multimodal transformers** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/31_advanced_model_architectures/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Route tokens through top-k experts and measure load imbalance.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Sparse routing saves compute only if experts receive balanced work and communication is manageable.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Create a comparison table for attention, SSM, MoE, and diffusion mechanisms.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why can MoE add parameters without proportional compute?
2. What problem does sparse attention target?
3. How does diffusion generation differ?

## Connection to modern AI

Architecture choice shapes scaling behavior and workload fit.

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
