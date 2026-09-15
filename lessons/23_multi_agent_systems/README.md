# Lesson 23 — Multi-Agent Systems

## Why this matters

Multiple agents help when specialization or ownership boundaries outweigh coordination cost.

## Learning outcomes

- Explain and apply supervisors and routers.
- Explain and apply handoffs and shared state.
- Explain and apply parallel specialists.
- Explain and apply coordination failures.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Supervisors and routers** — identify its inputs, outputs, assumptions, and role.
2. **Handoffs and shared state** — identify its inputs, outputs, assumptions, and role.
3. **Parallel specialists** — identify its inputs, outputs, assumptions, and role.
4. **Coordination failures** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/23_multi_agent_systems/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Compare one capable agent with three specialists on the same workflow.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Extra agents multiply prompts, latency, synchronization, and ambiguous responsibility.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Define a handoff contract with objective, evidence, output schema, and completion status.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. When is multi-agent justified?
2. What belongs in shared state?
3. How can agents disagree safely?

## Connection to modern AI

Enterprise workflows may split research, analysis, policy, and action across roles.

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
