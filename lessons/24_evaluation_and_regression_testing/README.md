# Lesson 24 — Evaluation and Regression Testing

## Why this matters

AI quality must be measured against explicit tasks, datasets, and failure criteria.

## Learning outcomes

- Explain and apply golden datasets.
- Explain and apply deterministic and model-based graders.
- Explain and apply retrieval and generation metrics.
- Explain and apply confidence intervals and regression gates.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Golden datasets** — identify its inputs, outputs, assumptions, and role.
2. **Deterministic and model-based graders** — identify its inputs, outputs, assumptions, and role.
3. **Retrieval and generation metrics** — identify its inputs, outputs, assumptions, and role.
4. **Confidence intervals and regression gates** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/24_evaluation_and_regression_testing/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Introduce one regression at a time and confirm its evaluator detects it.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A single aggregate score conceals slices and judge models can be biased.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Create an evaluation record with input, invariants, evidence, output, scores, and failure reason.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What should be deterministic?
2. When is an LLM judge appropriate?
3. Why evaluate slices?

## Connection to modern AI

Evaluations are the test suite and release gate for probabilistic systems.

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
