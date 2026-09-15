# Lesson 15 — Build a Tiny GPT

## Why this matters

Autoregressive language models learn to predict each next token from prior context.

## Learning outcomes

- Explain and apply causal language modeling.
- Explain and apply input and target shifting.
- Explain and apply negative log-likelihood.
- Explain and apply generation and exposure bias.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Causal language modeling** — identify its inputs, outputs, assumptions, and role.
2. **Input and target shifting** — identify its inputs, outputs, assumptions, and role.
3. **Negative log-likelihood** — identify its inputs, outputs, assumptions, and role.
4. **Generation and exposure bias** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/15_build_a_tiny_gpt/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Train a bigram baseline before a transformer and compare loss.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Generated text can look plausible while revealing shallow memorization and weak generalization.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Create training pairs from a token sequence using context length four.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What is next-token prediction?
2. Why establish a baseline?
3. What does perplexity summarize?

## Connection to modern AI

GPT-style models scale this objective across massive models and corpora.

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
