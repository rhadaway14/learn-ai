# Capstone Evaluation Plan

## Evaluation layers

1. ingestion correctness and source identity;
2. retrieval Recall at k, MRR, nDCG, filters, and latency;
3. citation existence and entailment;
4. answer requirements and forbidden claims;
5. tool selection, schema validity, authorization, and side effects;
6. workflow completion, termination, retry, and approval behavior;
7. end-to-end quality, latency, token usage, and cost.

## Corpus

Include ordinary cases, edge cases, adversarial instructions, missing evidence, conflicting evidence, stale sources, tool failures, timeouts, and tenant-boundary tests.

## Release gate

A release must preserve raw per-case results and fail when:

- any critical security invariant fails;
- citation provenance is invalid;
- a consequential tool bypasses authorization or approval;
- a protected slice regresses beyond its threshold;
- results cannot be reproduced from recorded artifacts.
