# Capstone Operations Runbook

## Before deployment

- identify the exact code, data, prompt, model, policy, and evaluation versions;
- verify evaluation and security gates;
- confirm dashboards, alerts, rollback target, and incident owner;
- test credentials without printing them;
- confirm provider quotas and cost limits.

## Triage sequence

1. classify scope: one request, tenant, region, model, or global;
2. stop consequential actions if authorization or integrity is uncertain;
3. preserve request IDs, traces, artifact fingerprints, and evidence;
4. identify the failing stage;
5. degrade, fail over, roll back, or disable the affected capability;
6. communicate impact without exposing sensitive prompts or data.

## Recovery verification

Replay protected evaluation cases, confirm queues and state transitions, check latency/error/cost signals, and document the decision to resume.
