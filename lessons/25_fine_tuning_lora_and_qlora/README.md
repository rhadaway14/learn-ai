# Lesson 25 — Fine-Tuning, LoRA, and QLoRA

## Why this matters

Fine-tuning changes behavior or specialization when prompting and retrieval are insufficient.

## Learning outcomes

- Explain and apply SFT and training examples.
- Explain and apply full tuning versus PEFT.
- Explain and apply low-rank adapters.
- Explain and apply quantization and catastrophic forgetting.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Sft and training examples** — identify its inputs, outputs, assumptions, and role.
2. **Full tuning versus peft** — identify its inputs, outputs, assumptions, and role.
3. **Low-rank adapters** — identify its inputs, outputs, assumptions, and role.
4. **Quantization and catastrophic forgetting** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/25_fine_tuning_lora_and_qlora/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Vary adapter rank and compare parameter count and update rank.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Bad or narrow training data efficiently teaches the wrong behavior.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Choose among RAG, prompts, tools, and fine-tuning for four scenarios.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What does LoRA train?
2. What does QLoRA add?
3. Why keep an untouched evaluation set?

## Connection to modern AI

PEFT makes customization feasible without updating every base-model parameter.

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
