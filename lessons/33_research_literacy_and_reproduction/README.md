# Lesson 33 — Research Literacy and Reproduction

## Why this matters

Confident engineering distinguishes evidence from claims and reproduces bounded results.

## Learning outcomes

- Explain and apply hypotheses and baselines.
- Explain and apply datasets, metrics, and leakage.
- Explain and apply ablations and uncertainty.
- Explain and apply reproduction versus replication.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Hypotheses and baselines** — identify its inputs, outputs, assumptions, and role.
2. **Datasets, metrics, and leakage** — identify its inputs, outputs, assumptions, and role.
3. **Ablations and uncertainty** — identify its inputs, outputs, assumptions, and role.
4. **Reproduction versus replication** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/33_research_literacy_and_reproduction/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Bootstrap a metric difference and examine whether its interval supports the headline.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Benchmark contamination and selective reporting can make weak methods look decisive.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Write a one-page review covering claim, mechanism, evidence, threats, and reproduction plan.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What does an ablation establish?
2. Why report uncertainty?
3. How does reproduction differ from replication?

## Connection to modern AI

Architecture decisions should rest on evidence you can interrogate.

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
