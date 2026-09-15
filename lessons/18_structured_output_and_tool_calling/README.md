# Lesson 18 — Structured Output and Tool Calling

## Why this matters

Models can propose typed actions but trusted code must validate and authorize them.

## Learning outcomes

- Explain and apply JSON Schema and typed output.
- Explain and apply tool descriptions.
- Explain and apply dispatch and validation.
- Explain and apply idempotency and approval.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Json schema and typed output** — identify its inputs, outputs, assumptions, and role.
2. **Tool descriptions** — identify its inputs, outputs, assumptions, and role.
3. **Dispatch and validation** — identify its inputs, outputs, assumptions, and role.
4. **Idempotency and approval** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/18_structured_output_and_tool_calling/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Fuzz tool arguments with missing, extra, and wrong-typed fields.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Executing plausible but invalid model output creates security and reliability failures.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Create a registry that rejects unknown tools and unexpected arguments.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Who executes the tool?
2. Why validate schema-constrained output?
3. What makes a tool idempotent?

## Connection to modern AI

Tool calling bridges language generation to consequential action.

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
