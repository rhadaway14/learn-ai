# Lesson 17 — Prompt and Context Engineering

## Why this matters

LLM behavior depends on instructions plus context deliberately assembled by the application.

## Learning outcomes

- Explain and apply instruction hierarchy.
- Explain and apply message roles.
- Explain and apply context budgets.
- Explain and apply prompt versioning and regression tests.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Instruction hierarchy** — identify its inputs, outputs, assumptions, and role.
2. **Message roles** — identify its inputs, outputs, assumptions, and role.
3. **Context budgets** — identify its inputs, outputs, assumptions, and role.
4. **Prompt versioning and regression tests** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/17_prompt_and_context_engineering/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Vary irrelevant context volume and measure whether required facts survive.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Longer prompts can dilute instructions, increase latency, and expand the attack surface.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Design a prompt contract with inputs, outputs, forbidden behavior, and test cases.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why is context selection an engineering problem?
2. What belongs in system instructions?
3. Why version prompts?

## Connection to modern AI

Prompts are one controlled component of an AI application.

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
