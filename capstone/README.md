# Capstone — Production-Grade Agentic AI Platform

The capstone combines model access, retrieval, tools, evaluation, security, and operations into one defensible system.

It is assembled throughout the curriculum rather than started from scratch in Lesson 35. See the [cumulative capstone path](../CAPSTONE_PATH.md) for lesson-by-lesson artifacts and readiness gates.

## Workbooks and executable slice

- [Architecture workbook](ARCHITECTURE.md)
- [Evaluation plan](EVALUATION_PLAN.md)
- [Threat model](THREAT_MODEL.md)
- [Operations runbook](RUNBOOK.md)
- [Deterministic vertical slice](vertical_slice.py)

## Required capabilities

- API and minimal user interface;
- model-provider abstraction with local-development option;
- document ingestion and versioned knowledge sources;
- vector plus lexical retrieval and metadata filtering;
- reranking and cited responses;
- bounded tool execution with authorization and human approval;
- durable workflow state and idempotent retries;
- prompt-injection defenses and adversarial tests;
- offline evaluation corpus and CI regression gates;
- traces, logs, quality signals, latency, token usage, and cost;
- containerized local environment and cloud deployment design;
- architecture decision records and operational runbook.

## Suggested domain

Build an AI delivery advisor that can analyze project requirements and evidence, retrieve relevant engineering knowledge, recommend an implementation plan, generate artifacts, and explain every recommendation. The domain is complex enough to exercise real architecture without requiring a frontier-scale model.

## Definition of done

The capstone is complete when another engineer can clone it, run it, understand its security boundaries, reproduce its evaluation results, and operate it without relying on undocumented knowledge.
