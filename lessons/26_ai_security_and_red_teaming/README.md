# Lesson 26 — AI Security and Red Teaming

## Why this matters

AI systems process untrusted language and may control privileged tools, creating new attack paths.

## Learning outcomes

- Explain and apply prompt injection.
- Explain and apply data exfiltration.
- Explain and apply excessive agency.
- Explain and apply poisoned retrieval and supply chain.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Prompt injection** — identify its inputs, outputs, assumptions, and role.
2. **Data exfiltration** — identify its inputs, outputs, assumptions, and role.
3. **Excessive agency** — identify its inputs, outputs, assumptions, and role.
4. **Poisoned retrieval and supply chain** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/26_ai_security_and_red_teaming/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Place malicious instructions inside retrieved documents and keep them treated as data.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Keyword filters alone are brittle and cannot enforce authorization boundaries.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Threat-model a RAG agent across assets, actors, entry points, boundaries, and mitigations.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why is prompt injection not SQL injection?
2. What is excessive agency?
3. Why treat tool output as untrusted?

## Connection to modern AI

Security must be enforced outside the model wherever consequences matter.

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
