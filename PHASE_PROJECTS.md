# Phase Projects and Increment Map

Each lesson contributes evidence to a working project completed at the end of its phase. Phase projects are smaller integration checkpoints for the cumulative capstone; they are not unrelated portfolio exercises.

## Phase 1 — Model Investigation Workbench

**Lessons:** 1–5  
**Outcome:** Compare a regression and classification problem, inspect evidence, choose an evaluation measure, and explain leakage and uncertainty through a visual workbench.  
**Delivery:** [Browser-first Model Investigation Workbench](projects/phase1/index.html), followed by the [Project A implementation extension](projects/PROJECT_A_CLASSICAL_ML.md) after Engineering Lab A.

| Increment | Lesson contribution |
|---|---|
| P1-I01 | Prediction problem, features, labels, and baseline model |
| P1-I02 | Named vector, matrix, tensor, and shape contract |
| P1-I03 | Loss choice and optimization evidence |
| P1-I04 | Sampling, uncertainty, and evidence-quality record |
| P1-I05 | Task type, threshold, metrics, and phase evaluation report |

## Phase 2 — Reproducible Neural Model Training System

**Lessons:** 6–10 plus [Engineering Lab A](labs/engineering_lab_a/README.md)
**Outcome:** Specify, implement, train, diagnose, and evaluate a small neural model with reproducible evidence.  
**Delivery:** [Project B — Image classifier](projects/PROJECT_B_IMAGE_CLASSIFIER.md), preceded by a domain-neutral model-training workbench.

| Increment | Lesson contribution |
|---|---|
| P2-I01 | Network architecture, parameter count, and shape trace |
| P2-I02 | Backpropagation and gradient-diagnosis trace |
| P2-I03 | Framework execution, state, mode, and checkpoint contract |
| P2-I04 | Dataset boundary, training run, evaluation, and checkpoint selection |
| P2-I05 | Generalization controls and model evidence card |
| [P2-I06](phase-projects/phase2/P2-I06.json) | Tested reference implementation created during [Engineering Lab A](labs/engineering_lab_a/README.md) |

## Phase 3 — Small Language-Model Explorer

**Lessons:** 11–16  
**Outcome:** Build and inspect tokenization, embeddings, attention, transformer blocks, next-token training, and decoding.  
**Delivery:** [Project C — Small language model](projects/PROJECT_C_SMALL_LANGUAGE_MODEL.md)

Increments `P3-I01` through `P3-I06` correspond to Lessons 11–16 and must preserve intermediate representations, tests, and experiment evidence.

## Phase 4 — Grounded Tool-Using AI Workflow

**Lessons:** 17–23  
**Outcome:** Build an evidence-grounded workflow with structured output, retrieval, bounded tools, explicit state, MCP integration, and controlled handoffs.  
**Delivery:** [Project D — Production-style RAG agent](projects/PROJECT_D_RAG_AGENT.md)

Increments `P4-I01` through `P4-I07` correspond to Lessons 17–23. Each increment must identify a trust boundary and downstream consumer.

## Phase 5 — Evaluated and Operated AI Service

**Lessons:** 24–30  
**Outcome:** Add evaluation gates, adaptation decisions, security controls, multimodal evidence, serving, operational telemetry, and scaling behavior.  
**Delivery:** [Project E — Operated AI service](projects/PROJECT_E_OPERATED_AI_SERVICE.md)

Increments `P5-I01` through `P5-I07` correspond to Lessons 24–30. Every increment requires measurable release or rollback evidence.

## Phase 6 — AI Architecture and Capstone Defense

**Lessons:** 31–35  
**Outcome:** Evaluate advanced architectures and reasoning strategies, reproduce research evidence, define governance, and defend an operable capstone.  
**Delivery:** the production-grade AI delivery advisor defined in [CAPSTONE_PATH.md](CAPSTONE_PATH.md).

Increments `P6-I01` through `P6-I05` correspond to Lessons 31–35 and culminate in the capstone release package.

## Increment flow

Every increment must satisfy this flow:

1. A lesson activity produces observable evidence.
2. The learner uses that evidence to propose or revise a phase capability.
3. Acceptance criteria decide whether the increment is accepted.
4. The next lesson consumes the accepted contract.
5. The phase project integrates and demonstrates all accepted increments.
6. The cumulative capstone reuses the phase result or records why it was replaced.

Use [templates/lesson-activity.md](templates/lesson-activity.md) for step 1 and [templates/phase-project-increment.md](templates/phase-project-increment.md) for steps 2–5.
