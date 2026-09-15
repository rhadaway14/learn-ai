# Lesson 16 — LLM Inference and Decoding

## Why this matters

Inference converts logits into sequences under quality, latency, memory, and randomness constraints.

## Learning outcomes

- Explain and apply greedy and beam decoding.
- Explain and apply temperature, top-k, and top-p.
- Explain and apply KV caching.
- Explain and apply batching and quantization.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Greedy and beam decoding** — identify its inputs, outputs, assumptions, and role.
2. **Temperature, top-k, and top-p** — identify its inputs, outputs, assumptions, and role.
3. **Kv caching** — identify its inputs, outputs, assumptions, and role.
4. **Batching and quantization** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/16_llm_inference_and_decoding/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Sample 1000 times at several temperatures and compare entropy.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Aggressive randomness destroys coherence while deterministic decoding can become repetitive.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Implement nucleus sampling that retains the smallest set reaching cumulative probability p.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What does temperature change?
2. Why does KV caching accelerate generation?
3. What does quantization trade?

## Connection to modern AI

Serving architecture often matters as much as model architecture for cost and latency.

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
