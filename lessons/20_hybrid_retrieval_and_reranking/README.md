# Lesson 20 — Hybrid Retrieval and Reranking

## Why this matters

Strong retrieval combines complementary signals and measures ranking before generation.

## Learning outcomes

- Explain and apply lexical and vector retrieval.
- Explain and apply metadata filters.
- Explain and apply reciprocal-rank fusion.
- Explain and apply cross-encoder reranking.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Lexical and vector retrieval** — identify its inputs, outputs, assumptions, and role.
2. **Metadata filters** — identify its inputs, outputs, assumptions, and role.
3. **Reciprocal-rank fusion** — identify its inputs, outputs, assumptions, and role.
4. **Cross-encoder reranking** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/20_hybrid_retrieval_and_reranking/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Construct lexical and semantic rankings with different winners and tune fusion constants.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Semantic retrieval can miss identifiers while lexical retrieval can miss paraphrases.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Calculate Recall at k, MRR, and nDCG for a labeled query set.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why combine lexical and vector search?
2. When should filtering happen?
3. What does a reranker trade?

## Connection to modern AI

Production RAG quality is often won or lost in retrieval and reranking.

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
