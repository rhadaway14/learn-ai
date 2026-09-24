# Hands-On AI Engineering Curriculum

This is an evidence-first path from machine-learning fundamentals to advanced AI architecture. It is designed for engineers with uneven backgrounds. **Lessons 1–10 are browser-first and require no Python knowledge.** Programming becomes part of the learner path only after the required Engineering Lab A readiness bridge.

The full path is approximately **135–185 hours**. For Lessons 1–10, the estimates below are the sum of the core and engineer lanes displayed in the browser; milestone projects are listed separately. Later-phase estimates include reading, implementation, experiments, and checkpoints.

## Learning method

Every lesson follows the same loop:

1. **Learn** — understand the problem, primitive, vocabulary, and relevant math.
2. **Locate** — highlight the primitive inside the cumulative retail semantic-search project.
3. **Predict** — choose what should happen before the evidence is revealed.
4. **Manipulate** — change one bounded, meaningful input or decision.
5. **Observe** — see the mechanism and project state change visually.
6. **Interpret** — explain the evidence through an authored check with specific feedback.
7. **Apply** — save the capability or decision into the cumulative project.

All seven beats occur in one persistent course UI. Frameworks are introduced only after the underlying operation is visible. Every five lessons end in an integration checkpoint that connects and verifies work the learner has already completed; it is not a separate lab with a new workflow.

## Phase 1 — Mathematical and ML foundations (11–14 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 01 | How Machines Learn | Interactive linear-regression investigation and evidence record | 80–90m |
| 02 | The Shapes of AI Data | Guided similarity, shape, and transformation experiments | 100–110m |
| 03 | Loss Functions and Optimization | Interactive loss surfaces, finite differences, and optimizer diagnosis | 100–110m |
| 04 | Probability and Statistics for ML | Distributions, sampling, Bayes, confidence experiments | 120–130m |
| 05 | Regression and Classification | Linear/logistic regression and decision boundaries | 135–145m |
| Project A | Classical ML benchmark specification | Compare model evidence and define a reproducible benchmark protocol | 2–4h |

Exit criteria:

- distinguish training, validation, test, and inference;
- explain parameter, hyperparameter, feature, label, loss, gradient, and generalization;
- recognize data leakage, underfitting, and overfitting;
- choose meaningful regression and classification metrics.

## Phase 2 — Neural networks and PyTorch (15–18 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 06 | Neural Network Anatomy | Trace a multilayer forward pass and its shapes | 115–125m |
| 07 | Backpropagation From Scratch | Trace a computational graph and parameter-update evidence | 125–135m |
| 08 | PyTorch and Autograd | Specify tensor, gradient, and optimizer behavior | 125–135m |
| 09 | Train and Evaluate a Neural Network | Design a reproducible train/validate/checkpoint protocol | 130–140m |
| 10 | Regularization and Generalization | Investigate capacity, regularization, and validation evidence | 130–140m |
| Project B | Model-training specification | Reproducible training specification and model evidence card | 4–6h |

Exit criteria:

- trace shapes through a network;
- explain activations, capacity, backpropagation, and automatic differentiation;
- specify the lifecycle and evidence required for a correct training loop;
- diagnose unstable, overfit, and underfit training.

## [Required Engineering Lab A — Python and PyTorch readiness](labs/engineering_lab_a/README.md) (6–10 hours)

This bridge occurs **after Lesson 10 and before any learner is asked to read, run, or modify Python**. It teaches how to run a program and interpret an error; values, variables, collections, functions, loops, packages, and virtual environments; tensor shapes and structured output; safe configuration changes; and tests with pass/fail evidence.

Experienced Python developers may pass a diagnostic and skip supported practice. Everyone must demonstrate the same readiness evidence before programming labs in later phases. Maintainer reference implementations do not count as learner tasks before this gate.

The lab produces [P2-I06](phase-projects/phase2/P2-I06.json), a tested PyTorch reference implementation and reproducible evidence record.

## Phase 3 — Language models from primitives (30–40 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 11 | Tokenization | Character, word, BPE-style tokenizer experiments | 3–4h |
| 12 | Embeddings | Train/query embeddings and semantic search | 4–5h |
| 13 | Attention | Scaled dot-product and causal attention from scratch | 5–6h |
| 14 | Transformer blocks | Multi-head attention, residuals, normalization, FFN | 5–6h |
| 15 | Tiny GPT | Train an autoregressive transformer on a small corpus | 6–8h |
| 16 | LLM inference | Sampling, temperature, top-k/top-p, KV-cache study | 4–5h |
| Project C | Small language model | Train, evaluate, and serve a tiny text model | 4–6h |

Exit criteria:

- explain tokenization and its tradeoffs;
- derive attention tensor shapes and masking behavior;
- describe pretraining as next-token prediction;
- explain context windows, autoregression, sampling, and KV caching.

## Phase 4 — LLM application engineering (26–36 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 17 | Prompt/context engineering | Versioned prompt tests and context-budget experiments | 3–4h |
| 18 | Structured output and tools | Schema-constrained output and safe tool dispatcher | 4–5h |
| 19 | RAG fundamentals | Ingestion, chunking, retrieval, citation pipeline | 5–6h |
| 20 | Retrieval quality | Hybrid search, reranking, filters, retrieval evaluation | 5–6h |
| 21 | Agents | Explicit model-tool loop with bounded state | 4–5h |
| 22 | MCP | Implement a small MCP server and client | 3–5h |
| 23 | Multi-agent systems | Supervisor/specialist workflow and failure analysis | 4–5h |
| Project D | Production-style RAG agent | Grounded assistant with tools, state, and citations | 6–8h |

Exit criteria:

- choose prompting, retrieval, tool use, or fine-tuning for the right reason;
- measure retrieval separately from answer generation;
- explain why an agent is an execution loop, not merely a chatbot;
- design bounded tools, state transitions, timeouts, and human approvals.

## Phase 5 — Quality, training, security, and operations (28–38 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 24 | Evaluation | Golden dataset, deterministic checks, model judges | 4–5h |
| 25 | Fine-tuning | SFT plus LoRA/QLoRA on a small open model | 5–7h |
| 26 | AI security | Prompt-injection and excessive-agency red-team lab | 4–5h |
| 27 | Multimodal AI | Vision-and-text extraction/reasoning workflow | 4–5h |
| 28 | Production serving | API, batching, caching, queues, fallbacks, tracing | 5–6h |
| 29 | MLOps/LLMOps | Dataset/model/prompt versioning and CI evaluation | 4–5h |
| 30 | Distributed AI | Parallelism simulations and distributed training lab | 4–5h |
| Project E | Operated AI service | Deploy with eval gates, telemetry, and security controls | 6–8h |

Exit criteria:

- build evaluation into CI instead of relying on demos;
- explain when parameter-efficient fine-tuning is justified;
- threat-model untrusted instructions and tool access;
- design observable, cost-aware, resilient inference services.

## Phase 6 — Advanced systems and architecture (20–30 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 31 | Advanced architectures | MoE, sparse attention, SSM, diffusion experiments | 4–5h |
| 32 | Reasoning and verification | Search, self-consistency, verifier experiments | 4–5h |
| 33 | Research literacy | Read and reproduce one bounded paper result | 4–6h |
| 34 | Enterprise architecture | Reference architectures and governance decisions | 4–5h |
| 35 | Capstone | Production-grade agentic AI platform | 8–12h |

Exit criteria:

- compare model architectures from first principles;
- distinguish capability claims from benchmark evidence;
- critique a paper's experiment design and ablations;
- defend an enterprise AI architecture across quality, security, cost, and operations.

## Assessment model

Each lesson is assessed across four dimensions:

| Dimension | Evidence |
|---|---|
| Understand | Written checkpoint answers in `PROGRESS.md` |
| Apply | Completed interaction or specification; working implementation only after Engineering Lab A |
| Investigate | Recorded experiment observations |
| Explain | Short plain-language and technical explanations |

Completion is based on evidence, not merely reading every page.
