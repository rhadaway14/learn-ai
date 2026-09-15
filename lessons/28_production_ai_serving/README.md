# Lesson 28 — Production AI Serving

## Why this matters

Production inference balances quality with latency, throughput, availability, and cost.

## Learning outcomes

- Explain and apply routing and fallbacks.
- Explain and apply batching, streaming, and caching.
- Explain and apply rate limits and queues.
- Explain and apply tracing, SLOs, and cost.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Routing and fallbacks** — identify its inputs, outputs, assumptions, and role.
2. **Batching, streaming, and caching** — identify its inputs, outputs, assumptions, and role.
3. **Rate limits and queues** — identify its inputs, outputs, assumptions, and role.
4. **Tracing, slos, and cost** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/28_production_ai_serving/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Replay duplicates through different cache keys and measure hit correctness.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Caching user-specific or nondeterministic output under weak keys leaks or corrupts results.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Design latency and error budgets across retrieval, model, and tool stages.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What can be cached safely?
2. Why batch inference?
3. Which AI-specific signals belong in telemetry?

## Connection to modern AI

Serving architecture determines whether a good demo survives real traffic.

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
