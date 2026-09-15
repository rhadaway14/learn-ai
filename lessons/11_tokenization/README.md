# Lesson 11 — Tokenization

## Why this matters

Language models operate on token IDs so tokenization controls representation, cost, and context usage.

## Learning outcomes

- Explain and apply character, word, byte, and subword tokens.
- Explain and apply BPE-style merges.
- Explain and apply vocabulary-size tradeoffs.
- Explain and apply special tokens and unknown text.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Character, word, byte, and subword tokens** — identify its inputs, outputs, assumptions, and role.
2. **Bpe-style merges** — identify its inputs, outputs, assumptions, and role.
3. **Vocabulary-size tradeoffs** — identify its inputs, outputs, assumptions, and role.
4. **Special tokens and unknown text** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/11_tokenization/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Train merges on two corpora and compare tokenization of technical terms.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A tokenizer mismatched to the domain wastes context and fragments meaningful units.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Calculate token-count and vocabulary tradeoffs for character and word tokenization.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why are tokens not words?
2. What does vocabulary size affect?
3. Why must tokenizer and model match?

## Connection to modern AI

Every LLM request is billed, truncated, embedded, and generated in tokens.

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
