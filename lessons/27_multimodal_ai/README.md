# Lesson 27 — Multimodal AI

## Why this matters

Multimodal models connect text with images, audio, video, and structured signals.

## Learning outcomes

- Explain and apply modality encoders.
- Explain and apply joint embedding spaces.
- Explain and apply early and late fusion.
- Explain and apply OCR, grounding, and modality evaluation.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Modality encoders** — identify its inputs, outputs, assumptions, and role.
2. **Joint embedding spaces** — identify its inputs, outputs, assumptions, and role.
3. **Early and late fusion** — identify its inputs, outputs, assumptions, and role.
4. **Ocr, grounding, and modality evaluation** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/27_multimodal_ai/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Perturb image and text features independently and observe fused similarity.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A fluent description can hallucinate details absent from the source modality.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Design a document workflow preserving page coordinates and source images with extracted text.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What is multimodal grounding?
2. How do early and late fusion differ?
3. Why evaluate each modality separately?

## Connection to modern AI

Modern assistants reason across screenshots, documents, speech, and text.

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
