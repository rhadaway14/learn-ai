# Lesson 29 — MLOps and LLMOps

## Why this matters

Reproducible delivery requires versioning data, code, prompts, models, and evaluations together.

## Learning outcomes

- Explain and apply experiment tracking.
- Explain and apply data, model, and prompt registries.
- Explain and apply CI evaluation gates.
- Explain and apply drift and rollback.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Experiment tracking** — identify its inputs, outputs, assumptions, and role.
2. **Data, model, and prompt registries** — identify its inputs, outputs, assumptions, and role.
3. **Ci evaluation gates** — identify its inputs, outputs, assumptions, and role.
4. **Drift and rollback** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/29_mlops_and_llmops/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Change one artifact version and verify the deployment fingerprint changes.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A model version alone cannot reproduce behavior when prompts and data also changed.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Define promotion criteria from experiment to staging to production.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What must be versioned?
2. How does drift differ from regression?
3. What makes rollback possible?

## Connection to modern AI

LLMOps extends MLOps to prompts, retrieval corpora, providers, and agent policies.

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
