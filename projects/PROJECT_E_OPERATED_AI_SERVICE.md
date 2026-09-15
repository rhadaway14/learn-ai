# Project E — Operated AI Service

## Mission

Deploy an AI service that remains understandable under traffic, dependency failure, and model change.

## Required work

1. Define latency, availability, quality, and cost objectives.
2. Add request IDs and traces across retrieval, model, and tools.
3. Implement rate limits, timeouts, bounded retries, circuit breaking, and backpressure.
4. Add safe caching with tenant and configuration-aware keys.
5. Version code, data, prompt, model, and evaluation artifacts.
6. Build deployment and rollback gates.
7. Run load, failure-injection, security, and recovery exercises.

## Deliverables

- service and deployment manifests;
- dashboards and actionable alerts;
- capacity and cost model;
- incident, rollback, and model-provider outage runbooks;
- release evidence bundle.

## Acceptance

- every request is attributable to an artifact fingerprint;
- dependency failures degrade deliberately;
- consequential actions remain approval-gated;
- rollback is tested rather than merely documented.
