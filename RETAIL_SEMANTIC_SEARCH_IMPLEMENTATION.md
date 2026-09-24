# Retail Semantic Search Course — Implementation Specification

## 1. Purpose

This document is the build contract for replacing the current delivery-risk phase projects with one cumulative retail semantic-search application. It is written for an implementation agent, especially Claude, and is normative unless a later approved architecture decision record supersedes it.

The completed course must teach AI development through one coherent application:

> Given a shopper query and a retail catalog, retrieve and rank the products that best satisfy the shopper's intent, explain the evidence, and operate the system safely.

The application begins with numeric features and models built from primitives. It evolves into neural ranking, dense and hybrid retrieval, RAG, tools, agents, MCP, multimodal retrieval, production operations, and an enterprise architecture defense.

This is not a collection of disconnected demos using retail-themed labels. Every lesson and phase integration checkpoint must change, inspect, test, or explain a real component of the same application.

**Learner-experience amendment:** [INTEGRATED_COURSE_EXPERIENCE.md](INTEGRATED_COURSE_EXPERIENCE.md) is normative for delivery. The lesson and the project interaction are now one seamless course UI. References in this specification to a phase “lab” mean a phase integration checkpoint unless they explicitly discuss legacy routes or implementation packages.

## 2. Approved decisions

These decisions are already approved and are not open implementation questions:

1. The course has **seven phases of five lessons each**.
2. Every lesson teaches through the cumulative application, and every phase ends with an integration checkpoint that assembles already-taught capabilities.
3. The capstone is a retail website semantic-search platform.
4. The required dataset is bundled, deterministic, synthetic, versioned, and legally redistributable.
5. A public retail dataset may be offered only as an optional extension.
6. Search encoders and vector retrieval are taught before GPT-style generation.
7. The required core path is browser-guided in one persistent course UI and does not require blank free-text answers.
8. An optional engineer path exposes implementation code, tests, performance, and architecture tradeoffs.
9. The shared stack is React, TypeScript, FastAPI, PostgreSQL with pgvector, PyTorch, and Docker Compose.
10. No required paid API, cloud account, GPU, or proprietary dataset is permitted.
11. The application evolves cumulatively; a phase may replace an earlier model only after comparing it with the accepted predecessor.
12. Learner evidence is generated from actions, configurations, predictions, run results, and guided decisions. Optional reflection text is never a release gate.

## 3. Definition of finished

The project is finished only when a new learner can:

1. clone or download the repository;
2. launch one canonical course experience using one documented command;
3. learn and apply every required concept through a guided, on-rails browser walkthrough without opening a separate lesson or lab guide;
4. see the data and model state change at each important boundary;
5. trigger and recover from a controlled failure;
6. compare the current phase capability with the previous accepted capability;
7. run automated acceptance checks;
8. export a schema-versioned phase artifact;
9. import that artifact into the next phase;
10. complete Lesson 35 with a working retail semantic-search application and an architecture defense.

The final system must support:

- catalog browsing;
- keyword retrieval;
- dense vector retrieval;
- hybrid retrieval;
- reranking;
- structured filters;
- grounded product recommendations with citations;
- bounded tools exposed through MCP;
- optional single-agent and multi-agent workflows;
- retrieval and answer evaluation;
- image-and-text product search;
- versioned models, prompts, datasets, and evaluation results;
- authentication/authorization examples, security controls, telemetry, recovery, and rollback;
- a documented enterprise reference architecture.

## 4. Curriculum and cumulative outcomes

| Phase | Lessons | Theme | Phase-lab outcome |
|---|---:|---|---|
| 1 | 01–05 | Mathematical and ML foundations | Search using handcrafted features, linear regression, and logistic classification |
| 2 | 06–10 | Neural networks and PyTorch | Neural relevance ranker compared with Phase 1 baselines |
| 3 | 11–15 | Language representation | Keyword, dense, and hybrid semantic-search MVP |
| 4 | 16–20 | Language models and RAG | Grounded conversational shopping assistant |
| 5 | 21–25 | Retrieval systems, agents, MCP, and evaluation | Evaluated tool-using search workflow |
| 6 | 26–30 | Training, security, multimodal, and operations | Secure production-style multimodal search service |
| 7 | 31–35 | Advanced systems and architecture | Scaled, verified, documented capstone release |

### Phase 1 — Mathematical and ML foundations

| Lesson | Required representation in the retail application |
|---:|---|
| 01 How Machines Learn | Inspect raw products, queries, relevance judgments, and behavior events. Distinguish features, labels, parameters, hyperparameters, training, and inference. |
| 02 The Shapes of AI Data | Convert query-product records into a named feature matrix and target vectors. Show every axis and reject semantically incorrect shapes. |
| 03 Loss Functions and Optimization | Step through one relevance prediction, error, loss, gradient, and parameter update with actual values before symbols. |
| 04 Probability and Statistics for ML | Show distributions, prevalence, samples, uncertainty, confidence intervals, and why observed clicks are not automatically relevance truth. |
| 05 Regression and Classification | Predict relevance grade 0–3 with regression and relevant/not-relevant with logistic classification. Explain the ordinal-target simplification. |

**Lab 1: Relevance ranking from primitives**

- Browse raw catalog and labeled query-product pairs.
- Select valid prediction-time features.
- Reject leakage and post-outcome features.
- Watch the selected fields become a matrix.
- Calculate one forward pass and one update with visible numbers.
- Train a linear regressor and logistic classifier from NumPy-style primitives, not scikit-learn.
- Compare both models with a keyword and popularity baseline.
- Move the decision threshold and show review volume, precision, recall, and missed relevant products.
- Enter a shopper query and see ranked products.
- Export the Phase 1 artifact.

### Phase 2 — Neural networks and PyTorch

| Lesson | Required representation in the retail application |
|---:|---|
| 06 Neural Network Anatomy | Show the handcrafted feature vector moving through input, hidden, activation, and output layers. |
| 07 Backpropagation | Trace one selected prediction backward to gradients and parameter updates, with numeric and symbolic views. |
| 08 PyTorch and Autograd | Show the equivalent PyTorch tensors, forward pass, loss, `backward`, gradients, and optimizer step in an optional code drawer. |
| 09 Train and Evaluate a Neural Network | Train/validate/checkpoint a neural relevance ranker on the same Phase 1 split. |
| 10 Regularization and Generalization | Compare capacity, weight decay, dropout, early stopping, train/validation gaps, and held-out performance. |

**Lab 2: Neural relevance ranker**

- Import the accepted Phase 1 artifact.
- Build an MLP through guided controls.
- Show tensor shapes and example values at every layer.
- Animate a bounded forward and backward pass.
- Train with PyTorch using deterministic defaults.
- Trigger one unstable or overfit run and fail closed.
- Recover by changing one control.
- Compare the neural ranker with Phase 1 regression, classification, and baseline results.
- Promote only when the numeric gate passes.
- Run the same shopper queries against both model versions.
- Export the Phase 2 artifact.

### Phase 3 — Language representation

| Lesson | Required representation in the retail application |
|---:|---|
| 11 Tokenization | Tokenize product titles, descriptions, attributes, and shopper queries. Show IDs, unknowns, subwords, padding, masks, and sequence length. |
| 12 Embeddings | Show token and text embeddings, cosine similarity, dot product, normalization, and neighborhoods. |
| 13 Similarity and Vector Search | Build/query an exact vector index, then introduce approximate search, recall/latency tradeoffs, and metadata filters. |
| 14 Attention | Contrast bidirectional encoder attention with causal decoder attention. Use product-query tokens for both masks. |
| 15 Transformer Encoders and Dual Encoders | Encode queries and products separately, train with positives/negatives, and retrieve by vector similarity. |

**Lab 3: Semantic-search MVP**

- Import the Phase 2 artifact and data contract.
- Tokenize a shopper query and selected product documents.
- Inspect embeddings and nearest neighbors.
- Build a pgvector index.
- Configure or train a small dual encoder.
- Compare lexical, dense, and hybrid retrieval for the same queries.
- Visualize rank changes and failure cases.
- Measure Recall@k, MRR, and nDCG on held-out queries.
- Promote the selected retrieval configuration.
- Export the Phase 3 artifact.

### Phase 4 — Language models and RAG

| Lesson | Required representation in the retail application |
|---:|---|
| 16 Autoregressive Language Models and Tiny GPT | Train a bounded next-token model and explain why decoder generation is a different branch from search encoding. |
| 17 LLM Inference | Demonstrate temperature, top-k, top-p, context limits, batching, latency, and KV caching. |
| 18 Prompt and Context Engineering | Compare versioned instructions and retrieved catalog context without changing the underlying retrieval result. |
| 19 Structured Output and Tools | Parse shopper intent into a schema and invoke bounded catalog/filter tools. |
| 20 RAG Fundamentals | Retrieve catalog evidence, construct context, generate a response, and cite exact products. |

**Lab 4: Grounded retail assistant**

- Import the accepted Phase 3 retrieval configuration.
- Parse a shopper request into structured intent and filters.
- Inspect the exact retrieval request and returned evidence.
- Compare prompts and context windows.
- Generate grounded recommendations with catalog citations.
- Refuse unsupported product claims.
- Demonstrate one context-overflow or grounding failure.
- Recover through a documented retrieval/context change.
- Compare answer evidence with raw search results.
- Export the Phase 4 artifact.

### Phase 5 — Retrieval systems, agents, MCP, and evaluation

| Lesson | Required representation in the retail application |
|---:|---|
| 21 Retrieval Quality | Compare BM25/lexical, dense, hybrid weighting, reranking, filters, hard negatives, and retrieval metrics. |
| 22 Agents | Implement an explicit model-tool loop with state, limits, stop conditions, and human approval. |
| 23 MCP | Expose catalog capabilities as tools/resources through a small MCP server and use them from a client. |
| 24 Multi-Agent Systems | Compare a deterministic workflow, one agent, and supervisor/specialists. Measure added latency and failure surface. |
| 25 Evaluation | Build golden queries, deterministic checks, retrieval evaluation, groundedness checks, and regression gates. |

**Lab 5: Evaluated tool-using search**

- Expose `search_products`, `get_product`, `compare_products`, and `check_inventory` through MCP.
- Run a deterministic workflow first.
- Enable a bounded single-agent workflow.
- Optionally enable query-understanding, retrieval-analysis, and merchandising-policy specialists.
- Inspect every state transition and tool call.
- Demonstrate timeout, invalid-tool-input, and excessive-loop containment.
- Run the golden evaluation set against all three workflow designs.
- Promote only if quality improves enough to justify latency and complexity.
- Export the Phase 5 artifact.

### Phase 6 — Training, security, multimodal, and operations

| Lesson | Required representation in the retail application |
|---:|---|
| 26 Fine-Tuning | Fine-tune a bounded component such as the relevance reranker or intent classifier. Include a no-fine-tune baseline. |
| 27 AI Security | Test prompt injection, poisoned catalog content, data leakage, unsafe tools, authorization boundaries, and excessive agency. |
| 28 Multimodal AI | Add product-image and text embeddings, cross-modal queries, and modality-specific evaluation. |
| 29 Production Serving | Add versioned APIs, batching, caching, queues, timeouts, fallbacks, rate limits, health checks, and tracing. |
| 30 MLOps and LLMOps | Version datasets, features, models, embeddings, indexes, prompts, evaluations, deployments, and rollbacks. |

**Lab 6: Secure production-style multimodal search**

- Import the Phase 5 release.
- Fine-tune and compare one bounded component.
- Add image-and-text search.
- Red-team untrusted query and catalog content.
- Apply tool authorization and approval controls.
- Serve versioned endpoints.
- Display latency, cache, failure, retrieval, and answer-quality telemetry.
- Promote and roll back a release through the UI.
- Export the Phase 6 artifact.

### Phase 7 — Advanced systems and architecture

| Lesson | Required representation in the retail application |
|---:|---|
| 31 Advanced and Distributed Architectures | Demonstrate distributed indexing/inference and compare MoE, sparse attention, SSM, and routing concepts without requiring large-model training. |
| 32 Reasoning and Verification | Add bounded search/planning, independent verification, evidence checks, and confidence/abstention rules. |
| 33 Research Literacy | Reproduce one bounded result, preferably the effect of hard negatives or reranking on retrieval quality. |
| 34 Enterprise AI Architecture | Produce data, model, security, deployment, governance, and operational reference views. |
| 35 Capstone | Run, evaluate, break, recover, defend, and release the complete platform. |

**Lab 7: Capstone release**

- Run the complete application from a clean clone.
- Reproduce the final evaluation.
- Demonstrate a contained failure and recovery.
- Compare the final platform with every previous accepted baseline.
- Show trust boundaries, authorization, lineage, telemetry, rollback, and scale strategy.
- Present the research reproduction and architecture decisions.
- Export a final manifest containing all seven artifact IDs.

## 5. Dataset contract

### 5.1 Required bundled dataset

Create a deterministic dataset generator and commit a small generated fixture. Do not commit restricted third-party data.

Use:

- dataset ID: `retail-search-teaching`;
- initial dataset version: `1.0.0`;
- random seed: `17`;
- core fixture: approximately 2,500 products;
- approximately 300 query intents;
- approximately 15,000 graded query-product judgments;
- enough events and image fixtures for later lessons without replacing product IDs.

The generator must reproduce byte-stable normalized records or document any fields that cannot be byte-stable.

### 5.2 Product record

Required fields:

| Field | Type | Notes |
|---|---|---|
| `product_id` | string | Stable and opaque |
| `title` | string | Searchable text |
| `description` | string | Searchable text with controlled ambiguity |
| `category` | string | Hierarchical top-level category |
| `subcategory` | string | Lower-level category |
| `brand` | string | Includes seen and held-out brands |
| `attributes` | object | Color, material, size, compatibility, use case |
| `price` | number | USD teaching value; not a live price |
| `rating` | number | 1–5 with realistic missingness |
| `review_count` | integer | Long-tailed |
| `inventory` | integer | Mutable serving field; never embedded as permanent truth |
| `popularity` | number | Historical signal with documented bias |
| `image_id` | string/null | Links to a bundled or generated fixture |
| `available_from` | timestamp | Enables time-aware splits |

### 5.3 Query and judgment records

Queries must include:

- exact product requests;
- category requests;
- attribute combinations;
- use-case intent;
- compatibility constraints;
- price constraints;
- ambiguous and underspecified requests;
- paraphrases;
- spelling variations;
- queries with no supported answer.

Judgments use grades:

| Grade | Meaning |
|---:|---|
| 0 | Irrelevant |
| 1 | Marginally related |
| 2 | Relevant |
| 3 | Highly relevant |

Phase 1 uses grade as a deliberately simplified regression target and `grade >= 2` as the binary classification target. The lesson must explicitly explain why relevance is ordinal and why later ranking metrics are more appropriate.

### 5.4 Behavior events

Generate impressions, clicks, add-to-cart events, and purchases. Include position bias, popularity bias, and missing feedback. Lessons must never describe clicks as unbiased ground truth.

### 5.5 Splits and leakage rules

- Keep a sealed test query set.
- Prevent paraphrases of the same intent from crossing protected boundaries.
- Keep exact product duplicates and near-duplicates in one split.
- Use time-aware product availability where relevant.
- Fit normalization, vocabularies, tokenizers, and learned preprocessing on training data only.
- Record dataset and split hashes in every phase artifact.
- The sealed test may be evaluated only by the release-gate operation.

### 5.6 Optional public-data extension

An optional extension may download a public retail-search dataset only when it includes:

- license and attribution documentation;
- a pinned source version and checksum;
- a small sampling script;
- no requirement for completing the core course;
- the same normalized schema as the bundled dataset.

## 6. Learner experience contract

The concept-level experience is governed by [INTEGRATED_COURSE_EXPERIENCE.md](INTEGRATED_COURSE_EXPERIENCE.md). Each lesson interleaves explanation and project interaction through **learn → locate → predict → manipulate → observe → interpret → apply** loops.

At the end of each phase, the integration checkpoint uses this macro step model:

1. **Goal** — preview the capability being added.
2. **Import** — validate the previous phase artifact.
3. **Inspect** — show the exact data entering the component.
4. **Predict** — choose an expected outcome from two or three meaningful options.
5. **Build** — make one guided decision at a time.
6. **Run** — execute the real implementation.
7. **Observe** — show persistent visual and tabular evidence.
8. **Explain** — choose the explanation best supported by the evidence.
9. **Break** — trigger one controlled failure.
10. **Recover** — change one factor and verify recovery.
11. **Compare** — compare with the previous accepted capability.
12. **Promote** — run deterministic numeric and contract gates.
13. **Save** — export a versioned artifact.

### 6.1 On-rails behavior

- Present one primary action per step.
- Keep later steps visible but locked, with an explanation of the prerequisite.
- Never begin with a blank text area.
- Predictions use selectable cards or bounded controls.
- Explanation checks use authored options with specific feedback.
- Optional reflection is available only after the evidence-backed choice.
- A wrong choice explains the misconception and permits another attempt.
- A learner can reset only the current experiment or the whole phase explicitly.
- Progress and attempts persist locally and, when the stack is running, in the lab database.
- The interface always shows the current phase, step, accepted predecessor, and unsaved evidence.
- The interface also shows the current lesson, concept, and highlighted retail-project component.
- Required explanations appear in the course UI immediately before the interaction that uses them.
- Phase checkpoints introduce no concept or interaction pattern that the preceding five lessons did not teach.
- Artifact transition is automatic on the normal same-session path; manual import/export remains available for provenance and recovery instruction.

### 6.2 Visual evidence requirements

Use a visual only when it teaches a mechanism or comparison. Every chart requires a table equivalent.

Every visual must state the question it answers, map learner controls to changed marks, annotate the current state, and include a plain-language “What this shows” interpretation. Visually distinguish fixture data, learner choices, learned parameters, derived evidence, and acceptance decisions.

| Concept | Required visual evidence |
|---|---|
| Raw data | Sortable product, query, and judgment records |
| Shapes | Named axes, tensor grid, and element inspection |
| Optimization | Prediction, error, loss, gradient, update, and loss curve |
| Probability | Distribution, sample variation, uncertainty interval |
| Classification | Confusion matrix, threshold curve, capacity indicator |
| Neural network | Layer flow, activations, shapes, gradient direction |
| Generalization | Train/validation curves and selected checkpoint |
| Tokenization | Text-to-token alignment and IDs |
| Embeddings | Vector components, similarity, neighbor map |
| Attention | Query-key scores, mask, normalized weights, output mix |
| Retrieval | Side-by-side result ranks and rank changes |
| RAG | Query, retrieved context, prompt, response, citations |
| Agents | State timeline and tool-call trace |
| Evaluation | Per-query results, aggregates, slices, regressions |
| Operations | Latency, throughput, errors, cache, versions, rollback |

### 6.3 Core and engineer paths

The core path uses the browser and documented controls. The engineer path may expose:

- code drawers tied to the current visual state;
- exact API request/response payloads;
- database queries;
- model and tensor inspection;
- TODO exercises after a complete reference walkthrough;
- tests, profiling, failure injection, and architecture tradeoffs.

Code syntax must never become an accidental prerequisite for understanding the concept.

Both paths live in the same course shell and share project state. The Engineer drawer may deepen the current visual with code, requests, tensors, schemas, tests, and architecture details; it must not repair missing teaching in the core path.

## 7. Shared architecture

### 7.1 Logical components

```text
Browser UI
  -> API gateway / FastAPI application
      -> catalog and evidence repositories
      -> feature and training services
      -> retrieval and reranking services
      -> generation provider
      -> agent runtime
      -> MCP client/server boundary
      -> evaluation service
  -> PostgreSQL + pgvector
  -> versioned artifact storage
  -> telemetry and trace store
```

### 7.2 Required technologies

- React + TypeScript + Vite for the cumulative lab UI;
- FastAPI and Pydantic for APIs and contracts;
- PostgreSQL with pgvector for catalog, runs, artifacts, and vectors;
- NumPy-style direct implementations for Phase 1;
- PyTorch for Phase 2 onward;
- Docker Compose for learner runtime;
- JSON Schema for exported artifacts;
- pytest for Python tests;
- Vitest or Node test runner for UI logic;
- Playwright for critical browser flows;
- axe-core or equivalent automated accessibility checks.

Do not introduce a high-level agent framework until the lessons have implemented the underlying loop directly. Framework comparisons may be optional later.

### 7.3 LLM provider contract

Provide one interface with three modes:

1. `deterministic-test` — fixed local provider for CI and contract tests;
2. `local` — OpenAI-compatible local runtime using a pinned, permissively licensed, CPU-capable instruct model;
3. `external` — optional OpenAI-compatible endpoint configured through environment variables.

The required course path must work in local mode without a paid account. Pin the local model revision, quantization, license, expected memory, and checksum in `config/models.lock.json`. Do not silently download a model when the learner starts an earlier phase.

### 7.4 Proposed repository layout

```text
apps/
  retail-search-web/
  retail-search-api/
  retail-search-mcp/
packages/
  retail_contracts/
  retail_data/
  retail_ml/
  retail_retrieval/
  retail_eval/
data/
  retail-search-teaching/
    manifest.json
    fixtures/
    images/
labs/
  retail-search/
    phase1/
    phase2/
    phase3/
    phase4/
    phase5/
    phase6/
    phase7/
schemas/
  retail-search/
config/
  models.lock.json
  prompts/
  evals/
docs/
  architecture/
  adr/
```

Keep current lessons and tests in place during migration. Do not delete the legacy delivery-risk labs until the retail replacements pass their acceptance gates and navigation has moved to the new routes.

## 8. Runtime and Docker Compose contract

### 8.1 Learner commands

Each phase must start through a stable command:

```bash
make phase1-start
make phase2-start
make phase3-start
make phase4-start
make phase5-start
make phase6-start
make phase7-start
```

Also provide `status`, `test`, `reset`, and `clean` variants for every phase.

### 8.2 Compose services

Use cumulative profiles and stable service names:

| Service | First required | Responsibility |
|---|---:|---|
| `retail-web` | Phase 1 | Guided UI |
| `retail-api` | Phase 1 | Domain, training, search, artifacts |
| `retail-db` | Phase 1 | PostgreSQL; enable pgvector before Phase 3 |
| `retail-model` | Phase 2 | Optional separate training/inference worker |
| `retail-llm` | Phase 4 | Local OpenAI-compatible model runtime |
| `retail-mcp` | Phase 5 | MCP tools/resources |
| `retail-telemetry` | Phase 6 | Local metrics/traces suitable for the teaching UI |

Use health checks and explicit dependency conditions. Volumes must have stable names and cleanup commands must remove only course-owned volumes.

### 8.3 Resource budgets

- Phases 1–3 must run on CPU with 8 GB system RAM.
- Phases 4–7 should target 16 GB RAM in local mode.
- GPU acceleration is optional.
- The learner must be warned before a model download larger than 500 MB.
- Provide a low-resource dataset/model profile.
- CI uses tiny deterministic fixtures and never downloads the learner LLM.

## 9. API contract

Version learner-facing APIs under `/api/v1`.

Minimum cumulative surface:

| Method and path | Purpose |
|---|---|
| `GET /health` | Service health and dependency readiness |
| `GET /api/v1/course/state` | Phase, step, predecessor, progress |
| `POST /api/v1/artifacts/import` | Validate previous phase artifact |
| `GET /api/v1/catalog/products` | Browse product fixtures |
| `GET /api/v1/catalog/queries` | Browse query fixtures |
| `GET /api/v1/catalog/judgments` | Inspect labels with split controls |
| `POST /api/v1/features/preview` | Convert selected rows to named features/tensors |
| `POST /api/v1/train/primitive` | Phase 1 models |
| `POST /api/v1/train/neural` | Phase 2 model |
| `POST /api/v1/index/build` | Lexical/vector index builds |
| `POST /api/v1/search` | Keyword, dense, hybrid, reranked search |
| `POST /api/v1/assistant/query` | Grounded response generation |
| `POST /api/v1/agents/run` | Bounded agent workflow |
| `POST /api/v1/evaluations/run` | Evaluation suite |
| `GET /api/v1/runs/{run_id}` | Run configuration, evidence, state |
| `POST /api/v1/failures/{scenario}` | Explicit controlled failure only |
| `POST /api/v1/releases/promote` | Execute acceptance gate and promote |
| `POST /api/v1/releases/rollback` | Restore an accepted predecessor |
| `POST /api/v1/artifacts/export` | Create versioned phase artifact |

Long-running operations return a run ID and observable status. Do not hold an HTTP request open for an unbounded training, indexing, or evaluation job.

## 10. Artifact chain

Use schema version `2.0` for the retail project. Do not overload the legacy delivery-risk schema.

Every artifact contains:

```json
{
  "schema_version": "2.0",
  "artifact_type": "retail-search-phase",
  "phase": 1,
  "attempt_number": 1,
  "artifact_id": "...",
  "previous_artifact_id": null,
  "created_at": "...",
  "dataset": {
    "id": "retail-search-teaching",
    "version": "1.0.0",
    "manifest_sha256": "...",
    "split_sha256": "..."
  },
  "prediction_choices": [],
  "configuration": {},
  "runs": [],
  "metrics": {},
  "controlled_failure": {},
  "recovery": {},
  "comparison": {},
  "guided_decisions": [],
  "acceptance": {
    "passed": true,
    "checks": {}
  },
  "versions": {}
}
```

Rules:

- attempt numbers are monotonic;
- filenames do not overwrite prior attempts;
- schema and phase transitions validate fail-closed;
- artifacts record configuration and evidence, not only a pass boolean;
- Phase N imports only an accepted Phase N-1 artifact;
- optional reflection is stored separately and never determines acceptance;
- migration from legacy artifacts is explicit; do not pretend they are retail artifacts.

## 11. Acceptance gates

Thresholds must be established empirically from the deterministic fixture and then frozen in tests. Do not choose thresholds that the default run barely passes.

### Phase 1

- feature matrix names and ordering match the contract;
- leakage features are excluded;
- regression beats the target-mean baseline on the designated regression metric;
- classification beats the majority baseline and has nonzero precision and recall;
- threshold respects the illustrated capacity constraint;
- one primitive gradient update matches a known-answer calculation.

### Phase 2

- deterministic training reproduces selected epoch and metrics within tolerance;
- neural ranker beats or clearly characterizes failure to beat Phase 1;
- every trainable parameter receives a finite gradient;
- checkpoint precedes the final epoch in the known-good run;
- sealed test is evaluated once;
- controlled instability or overfitting fails closed.

### Phase 3

- tokenization and embedding shapes match contracts;
- vector normalization and similarity known-answer tests pass;
- dense or hybrid retrieval improves a frozen retrieval metric over the lexical baseline on the intended query slice;
- filters do not corrupt rank or leak test labels;
- index rebuild is deterministic for the fixture.

### Phase 4

- every product claim is supported by a cited retrieved record;
- structured intent validates against schema;
- unsupported requests abstain or clarify;
- prompt/context changes are versioned;
- retrieval and generation evidence remain separable.

### Phase 5

- MCP tools validate input and authorization;
- agent runs have maximum steps, timeout, and stop reason;
- deterministic workflow remains available as a baseline;
- evaluation reports retrieval, answer, latency, and tool metrics separately;
- multi-agent promotion requires measured benefit, not architectural novelty.

### Phase 6

- fine-tuned component beats its unfine-tuned baseline on protected evaluation without unacceptable regression slices;
- injection and excessive-agency cases are contained;
- image/text retrieval has modality-specific evaluation;
- version, health, latency, error, and trace evidence is observable;
- rollback restores a known accepted release.

### Phase 7

- clean-start instructions reproduce the system;
- the full evaluation passes;
- one failure and recovery are demonstrated;
- research result is reproducible;
- architecture views agree with deployed components;
- final manifest links all seven accepted phase artifacts.

## 12. Accessibility, clarity, and presentation

- WCAG 2.2 AA is the target.
- Complete keyboard operation is required.
- Focus must be visible.
- Status cannot depend on color alone.
- Charts require persistent accessible tables.
- Canvas requires `role="img"`, a meaningful label, and a data equivalent.
- Reduced motion must be honored.
- The lab must remain usable at 320 CSS pixels.
- Every acronym is expanded on first use.
- Every metric includes a plain-language interpretation.
- Every equation follows words, actual numbers, and then symbols.
- Every step answers: what changed, why it changed, how to tell, and where it appears in modern AI.
- Avoid decorative dashboards whose numbers do not affect the lesson decision.

## 13. Testing and CI

In addition to the tests below, validate the integrated content contract: stable concept identifiers, concept-to-project traceability, explanation-before-interaction ordering, authored feedback, visual data equivalents, concept-level resume, automatic phase transition, and absence of required content that exists only in Markdown.

### 13.1 Fast required checks

Run on every change:

- Python unit and contract tests;
- TypeScript type check;
- JavaScript/TypeScript unit tests;
- JSON Schema validation;
- dataset determinism and leakage checks;
- artifact transition tests;
- syntax checks for every learner-facing script;
- lesson/catalog consistency tests;
- accessibility static checks.

### 13.2 Browser checks

Use Playwright for at least:

- clean Phase 1 completion;
- progress resume after reload;
- wrong-choice feedback and retry;
- controlled failure and recovery;
- artifact download/import chain;
- keyboard-only completion of one phase;
- small-viewport completion;
- Phase 3 search comparison;
- Phase 4 cited answer;
- Phase 5 bounded tool run;
- Phase 6 rollback.

### 13.3 Container checks

CI must build the Compose images and run smoke tests for the currently implemented phase. Model-heavy paths use tiny fixtures or deterministic providers. Maintain a scheduled or explicitly triggered full local-model workflow separately.

### 13.4 Numerical tests

Include known-answer cases for:

- feature transformations;
- regression and logistic loss;
- gradient calculations;
- backpropagation;
- autograd parity;
- cosine similarity and dot product;
- attention and masks;
- retrieval metrics;
- ranking changes;
- calibration where taught;
- evaluation aggregation and slice counts.

## 14. Migration from the current repository

The repository currently presents a six-phase delivery-risk capstone and contains Phase 1 and Phase 2 delivery-risk labs. Migrate safely:

1. Add this implementation document and an ADR approving the retail capstone.
2. Add the dataset and contracts without changing current navigation.
3. Build the new retail application shell under new paths.
4. Implement and validate the new Phase 1 lab.
5. Switch Phase 1 navigation only after its acceptance suite passes.
6. Repeat for Phase 2.
7. Update curriculum, capstone, phase-project, roadmap, progress, study-guide, README, dashboard, and lesson-catalog documents to seven phases.
8. Preserve lesson completion IDs where lesson numbers are unchanged.
9. Introduce new milestone IDs without erasing legacy browser progress.
10. Archive legacy delivery-risk labs under a clearly marked legacy path only after replacement; do not leave two apparent canonical paths.
11. Remove legacy code only in a later cleanup change after verifying no links, tests, schemas, or documentation reference it.

Required documentation updates include at least:

- `README.md`;
- `CURRICULUM.md`;
- `CAPSTONE_PATH.md`;
- `PHASE_PROJECTS.md`;
- `ROADMAP.md`;
- `PROGRESS.md`;
- `STUDY_GUIDE.md`;
- `course.js` and dashboard content;
- lesson 01–35 “AI story” and capstone-increment sections;
- schemas and sample artifacts;
- `Makefile`, `compose.yaml`, and CI workflows.

## 15. Implementation work packages for Claude

Do not implement all phases in one change. Use the following ordered work packages. Each package ends with tests, documentation, and an atomic commit.

### WP0 — Baseline and migration guardrails

- Record the current passing test counts and environment.
- Add the retail-capstone ADR.
- Add migration flags and legacy-path rules.
- Add contract tests that protect existing learner progress.
- No UI replacement yet.

### WP1 — Retail domain and deterministic data

- Implement normalized domain models.
- Implement dataset generator, manifest, hashes, fixture, split rules, and leakage tests.
- Add a data-inspection CLI for maintainers.
- Add licenses/attribution manifest.

### WP2 — Shared application shell

- Create React/TypeScript web app, FastAPI API, PostgreSQL/pgvector database, migrations, health checks, and Compose profile.
- Implement phase/step navigation, progress, attempts, artifact shell, accessibility primitives, error recovery, and reset.
- Use fixture data only; no Phase 1 model yet.

### WP3 — Phase 1 lab

- Implement raw-data explorer, feature builder, tensor/shape viewer, one-update optimizer walkthrough, primitive regression/classification, threshold explorer, search results, acceptance gate, and artifact.
- Retheme Lessons 1–5 interactions and capstone increments to the retail task.
- Add Playwright completion flow.
- Switch Phase 1 navigation after acceptance passes.

### WP4 — Phase 2 lab

- Implement neural-network visualizer, backpropagation evidence, PyTorch training, controlled failure, regularization comparison, search comparison, promotion, and artifact.
- Retheme Lessons 6–10.
- Preserve Engineering Lab A as the code-readiness bridge, but retheme its example to retail relevance where practical.
- Switch Phase 2 navigation after acceptance passes.

### WP5 — Curriculum migration

- Update all governing documents to the approved seven-phase map.
- Renumber or retitle Lessons 11–35 where required.
- Update lesson catalog and generated pages.
- Add all seven lab cards to the course dashboard in locked/progressive states.

### WP6 — Phase 3 lab

- Implement tokenization, embedding inspection, pgvector indexing, lexical/dense/hybrid comparison, dual-encoder path, retrieval evaluation, controlled failures, promotion, and artifact.
- Teach similarity/vector search explicitly before attention.

### WP7 — Phase 4 lab

- Add provider interface, pinned local model configuration, Tiny GPT lesson path, inference controls, prompts, schemas, tools, RAG, citations, grounding/abstention, evaluation, and artifact.

### WP8 — Phase 5 lab

- Add retrieval-quality experiments, direct agent loop, MCP server/client, optional multi-agent topology, traces, bounded failures, evaluation dashboard, promotion, and artifact.

### WP9 — Phase 6 lab

- Add bounded fine-tuning, security lab, multimodal retrieval, production APIs, telemetry, lineage, deployment records, rollback, and artifact.

### WP10 — Phase 7 and capstone

- Add distributed/advanced demonstrations, reasoning verification, research reproduction, architecture views, final evaluation, clean-start runbook, capstone defense, and final manifest.

### WP11 — Final hardening

- Run all fast, browser, container, accessibility, security, and clean-clone checks.
- Audit prerequisites against the no-surprise rule.
- Audit every metric, equation, and code drawer.
- Remove obsolete legacy code only after reference checks pass.
- Produce instructor and learner release notes.

## 16. Claude execution protocol

Claude must follow these rules while implementing:

1. Read `AGENTS.md`, `COURSE_DESIGN.md`, `LESSON_CONTRACT.md`, and this document before editing.
2. Inspect the current worktree and preserve unrelated user changes.
3. Work on one work package at a time.
4. Before each package, state the acceptance criteria and files expected to change.
5. Prefer primitives before frameworks, matching the course progression.
6. Do not add mandatory free-text gates.
7. Do not hide a missing implementation behind a simulated success result.
8. Deterministic teaching providers may exist for CI, but learner documentation must distinguish them from actual models.
9. Do not access the sealed test during tuning.
10. Do not commit generated model weights, credentials, unrestricted caches, or unlicensed data.
11. Keep Docker cleanup narrowly scoped to course-owned services and volumes.
12. Run the repository-required test commands before every commit.
13. Add tests that would fail before the implemented behavior exists.
14. Keep commits atomic and use descriptive messages.
15. Stop and report when a requested dependency, model, license, or architecture decision violates this specification.

For every completed work package, report:

- learner-visible outcome;
- architecture changes;
- files changed;
- tests and exact results;
- known limitations;
- next package;
- commit SHA.

## 17. Non-goals

The first complete course release does not require:

- production-scale retail traffic;
- training a foundation model from scratch;
- a managed cloud deployment;
- paid LLM APIs;
- GPU-only exercises;
- real customer or personal data;
- autonomous purchasing;
- dynamic price changes;
- claims that agents or multi-agent systems are inherently superior;
- mathematical proofs beyond the lesson's stated engineering depth.

## 18. Final handoff checklist

Before declaring the migration complete, verify:

- [ ] Seven phases and seven integration checkpoints appear in the course rail.
- [ ] One persistent course UI teaches and applies all required lesson content.
- [ ] Phase-ending labs are presented as integration checkpoints and introduce no untaught workflow.
- [ ] Lessons 1–35 tell one retail semantic-search story.
- [ ] Every lab imports the previous accepted artifact.
- [ ] Every lab has a guided core path and optional engineer path.
- [ ] No required blank free-text answer remains.
- [ ] Dataset generation and splits are deterministic and tested.
- [ ] Search baselines, neural ranking, vector retrieval, RAG, agents, MCP, evaluation, multimodal retrieval, security, operations, and architecture are all demonstrated in the live application.
- [ ] Every phase includes prediction, visible evidence, controlled failure, recovery, comparison, promotion, and export.
- [ ] Every major concept is visibly mapped to its input, operation, output, and downstream use in the retail project.
- [ ] Manual novice-engineer and experienced-engineer reviews approve Phase 1 and Phase 2 before the pattern is copied to later phases.
- [ ] The core path requires no paid service or GPU.
- [ ] Accessibility and small-screen checks pass.
- [ ] CI covers syntax, unit, contracts, schemas, browser flows, containers, and artifact transitions.
- [ ] A clean clone can run the documented capstone path.
- [ ] The final manifest links seven accepted phase artifacts.
- [ ] Legacy delivery-risk navigation and references are removed or explicitly archived.

## Appendix A — Claude redesign prompt

The original implementation prompt is complete and has been superseded for learner-experience work. Use [CLAUDE_UNIFIED_COURSE_REDESIGN_PROMPT.md](CLAUDE_UNIFIED_COURSE_REDESIGN_PROMPT.md) to implement the integrated course and project experience. It preserves the technical requirements in this specification, rebuilds Phase 1 and Phase 2 as the pattern-setting pilot, and requires manual approval before that pattern is generalized to later phases.
