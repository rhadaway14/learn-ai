# Lesson 19 — RAG Fundamentals

## Why this matters

RAG supplies retrieved evidence at inference time instead of expecting memorization of changing private knowledge.

## Learning outcomes

- Explain and apply ingestion and chunking.
- Explain and apply embedding and indexing.
- Explain and apply retrieval and context assembly.
- Explain and apply grounded answers and citations.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Ingestion and chunking** — identify its inputs, outputs, assumptions, and role.
2. **Embedding and indexing** — identify its inputs, outputs, assumptions, and role.
3. **Retrieval and context assembly** — identify its inputs, outputs, assumptions, and role.
4. **Grounded answers and citations** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/19_rag_fundamentals/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Test chunk sizes on questions requiring local and cross-section evidence.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Bad retrieval cannot be repaired reliably by eloquent generation.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Build a three-document retriever and require each factual sentence to cite a source ID.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What problem does RAG solve?
2. Why separate retrieval and generation?
3. What makes a citation trustworthy?

## Connection to modern AI

Enterprise assistants combine governed data stores with retrieval and generation.

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
