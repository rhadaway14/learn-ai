# Lesson 34 — Enterprise AI Architecture

## Why this matters

Enterprise AI coordinates data, identity, models, tools, governance, and operations across trust boundaries.

## Learning outcomes

- Explain and apply model and data boundaries.
- Explain and apply identity and authorization.
- Explain and apply governance and human oversight.
- Explain and apply quality, cost, resilience, and portability.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Model and data boundaries** — identify its inputs, outputs, assumptions, and role.
2. **Identity and authorization** — identify its inputs, outputs, assumptions, and role.
3. **Governance and human oversight** — identify its inputs, outputs, assumptions, and role.
4. **Quality, cost, resilience, and portability** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/34_enterprise_ai_architecture/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Change decision weights and observe when the architecture recommendation flips.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A diagram omitting identity, provenance, evaluation, or failure paths is not operational architecture.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Produce an ADR comparing hosted, self-hosted, and hybrid model strategies.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Where should policy be enforced?
2. What requires provenance?
3. How can lock-in be limited without lowest-common-denominator design?

## Connection to modern AI

This phase turns AI components into systems an organization can govern and operate.

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
