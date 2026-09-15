# Lesson 35 — Capstone Production-Grade Agentic AI Platform

## Why this matters

The capstone proves model, retrieval, tool, evaluation, security, and operational decisions work together.

## Learning outcomes

- Explain and apply end-to-end architecture.
- Explain and apply evidence-grounded workflows.
- Explain and apply bounded agency.
- Explain and apply evaluation gates and production operations.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **End-to-end architecture** — identify its inputs, outputs, assumptions, and role.
2. **Evidence-grounded workflows** — identify its inputs, outputs, assumptions, and role.
3. **Bounded agency** — identify its inputs, outputs, assumptions, and role.
4. **Evaluation gates and production operations** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/35_capstone_production_grade_agentic_ai_platform/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Inject retrieval, model, tool, and approval failures and demonstrate recovery.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A happy-path demonstration is not evidence of production readiness.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Implement one vertical slice from ingestion through cited answer and approved action with a trace and regression case.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Can another engineer reproduce the system?
2. Are consequential actions authorized outside the model?
3. Can every release be evaluated and rolled back?

## Connection to modern AI

The final system demonstrates AI engineering and architecture as one discipline.

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
