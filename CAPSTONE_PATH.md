# Cumulative Capstone Path

The capstone is not postponed until Lesson 35. It grows through small, reviewable increments so the final lesson integrates familiar parts instead of introducing a new project all at once.

## Final system

The learner will build an evidence-grounded AI delivery advisor with retrieval, bounded tools, evaluation, security controls, observability, and an operational deployment design.

## Increment map

| Lessons | What the learner has learned | Capstone artifact produced |
|---:|---|---|
| 01–02 | Models, learning, data, vectors, shapes, similarity | Problem statement, glossary, sample inputs and expected outputs |
| 03–05 | Loss, optimization, probability, regression, classification, metrics | Baseline decision model and evaluation worksheet |
| 06–10 | Neural networks, backpropagation, training, validation, regularization | Reproducible model-training component and model card |
| 11–12 | Tokenization and embeddings | Document representation and semantic-search prototype |
| 13–16 | Attention, transformers, language modeling, inference | Small language-model experiment and inference decision record |
| 17–18 | Context design, structured output, tool contracts | Versioned instructions, response schema, and validated tool interface |
| 19–20 | Ingestion, retrieval, hybrid search, reranking | Cited retrieval pipeline with a measured retrieval dataset |
| 21–23 | Agent loops, state, MCP, multi-agent coordination | Bounded workflow with explicit state, stop conditions, and handoffs |
| 24 | Evaluation | Golden dataset and automated release gate |
| 25 | Fine-tuning | Evidence-based fine-tuning decision and optional adapter experiment |
| 26 | Security | Threat model, adversarial cases, authorization and approval controls |
| 27 | Multimodal systems | Optional non-text evidence path with modality-specific evaluation |
| 28–30 | Serving, LLMOps, distributed systems | API, telemetry, version registry, failure recovery, and scaling plan |
| 31–34 | Advanced architectures, reasoning, research, governance | Architecture decisions, verified reasoning path, evidence review, governance package |
| 35 | Integration | Operable capstone release with evaluation report and demonstration |

## Required artifact contract

Every increment records:

- the problem it solves;
- inputs and outputs;
- assumptions and trust boundaries;
- success metrics;
- a normal example;
- at least one failure example;
- automated or reproducible verification;
- the decision to keep, revise, or replace it.

Later lessons may replace earlier implementations, but they must preserve the evidence explaining why the design changed.

## Readiness gates

### Gate A — Foundations complete (after Lesson 05)

The learner can explain learning and evaluation, establish a naive baseline, select a meaningful metric, and detect obvious leakage.

### Gate B — Model mechanics complete (after Lesson 16)

The learner can trace data through a model, explain training and inference, and justify a model and decoding strategy.

### Gate C — Application vertical slice complete (after Lesson 23)

The system can retrieve evidence, produce a structured cited response, request a bounded tool action, and stop safely.

### Gate D — Production controls complete (after Lesson 30)

The system has evaluation gates, security controls, tracing, versioning, recovery behavior, and a scaling plan.

### Gate E — Capstone defense (Lesson 35)

The learner can run the system, reproduce its evaluation, demonstrate a contained failure, explain every major architecture decision, and operate or roll it back using documented procedures.

## What Lesson 35 must not require unexpectedly

The final capstone cannot introduce an unprepared requirement for:

- a new programming language or application framework;
- an unfamiliar cloud provider or paid model service;
- a new database, vector store, or orchestration framework;
- authentication, deployment, evaluation, or security concepts not previously practiced;
- undocumented infrastructure;
- a dataset the learner cannot legally and practically obtain.

If the final design uses one of these, an earlier lesson must teach it through a smaller working example first.
