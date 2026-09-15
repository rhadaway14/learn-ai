# Project D — Production-Style RAG Agent

## Mission

Build a cited assistant that retrieves governed evidence and invokes bounded read-only tools.

## Required work

1. Define ten or more representative questions and relevance judgments first.
2. Build versioned ingestion with stable source and chunk identifiers.
3. implement lexical and vector retrieval, filters, fusion, and reranking;
4. measure Recall at k, MRR, latency, and answer invariants separately;
5. require citations traceable to retrieved evidence;
6. add a bounded agent loop with explicit state and termination;
7. red-team prompt injection in documents and tool results.

## Deliverables

- local containerized environment;
- ingestion, retrieval, answer, and evaluation commands;
- architecture and threat-model documents;
- trace viewer or structured trace output;
- regression corpus and CI gate.

## Acceptance

- no answer citation refers to unretrieved evidence;
- tool schemas and authorization are enforced outside the model;
- failure states are visible and resumable;
- retrieval and generation regressions are distinguishable.
