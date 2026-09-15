# Capstone Architecture Workbook

## Context

State the users, jobs, authoritative data, consequences, expected scale, latency target, quality target, budget, compliance needs, and prohibited behavior.

## Required components

| Component | Decision to document |
|---|---|
| Interface | API/UI contract, authentication, tenant boundary |
| Orchestrator | Explicit workflow states, retries, idempotency |
| Retrieval | ingestion, identifiers, hybrid ranking, filters, reranking |
| Models | provider/local abstraction, routing, decoding, fallback |
| Tools | schemas, authorization, sandboxing, approval |
| State | durable workflow state versus conversational context |
| Evaluation | corpus, metrics, slices, gates, raw evidence |
| Observability | traces, quality signals, latency, tokens, cost |
| Operations | deployment, scaling, incidents, rollback |

## Required diagrams

1. component and trust-boundary diagram;
2. one end-to-end sequence including failure paths;
3. data lineage and retention diagram;
4. deployment topology.

Every arrow should name the data or authority crossing it.
