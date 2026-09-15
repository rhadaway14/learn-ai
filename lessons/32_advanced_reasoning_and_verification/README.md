# Lesson 32 — Advanced Reasoning and Verification

## Why this matters

Reasoning systems can spend inference compute searching for and checking candidates.

## Learning outcomes

- Explain and apply chain-of-thought as latent work.
- Explain and apply self-consistency and search.
- Explain and apply verifiers and process supervision.
- Explain and apply test-time compute.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Chain-of-thought as latent work** — identify its inputs, outputs, assumptions, and role.
2. **Self-consistency and search** — identify its inputs, outputs, assumptions, and role.
3. **Verifiers and process supervision** — identify its inputs, outputs, assumptions, and role.
4. **Test-time compute** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/32_advanced_reasoning_and_verification/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Sample candidates with a controlled error rate and compare majority vote with verification.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Repeated reasoning can reinforce a systematic error and consume cost without adding evidence.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Design a solver-verifier loop with a hard budget and independently checkable criteria.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What is test-time compute?
2. Why separate solver and verifier?
3. When does self-consistency fail?

## Connection to modern AI

Reasoning models trade latency and tokens for better hard-problem performance.

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
