# Hands-On AI Engineering Curriculum

This is a build-first path from machine-learning fundamentals to advanced AI architecture. It is designed for an experienced software/cloud engineer, so Python syntax, Git, APIs, containers, and basic deployment are treated as existing skills rather than separate courses.

The full path is approximately **140–200 hours**. The time ranges include reading, implementation, experiments, checkpoints, and milestone projects.

## Learning method

Every lesson follows the same loop:

1. **Concept** — understand the primitive and why it exists.
2. **Derivation** — work through the relevant math at an engineering level.
3. **Implementation** — build it with minimal abstraction.
4. **Experiment** — change assumptions and observe failure modes.
5. **Connection** — locate the primitive inside modern AI systems.
6. **Checkpoint** — explain it and pass executable tests.

Frameworks are introduced only after the underlying operation is visible.

## Phase 1 — Mathematical and ML foundations (18–25 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 01 | ML fundamentals | Linear regression and gradient descent from NumPy | 2–3h |
| 02 | Vectors, matrices, tensors | Dense layer, similarity, shape experiments | 3–4h |
| 03 | Loss and optimization | Loss surfaces, finite differences, SGD variants | 3–4h |
| 04 | Probability and statistics | Distributions, sampling, Bayes, confidence experiments | 4–5h |
| 05 | Regression and classification | Linear/logistic regression and decision boundaries | 4–5h |
| Project A | Classical ML benchmark | Compare baseline models on one real dataset | 2–4h |

Exit criteria:

- distinguish training, validation, test, and inference;
- explain parameter, hyperparameter, feature, label, loss, gradient, and generalization;
- recognize data leakage, underfitting, and overfitting;
- choose meaningful regression and classification metrics.

## Phase 2 — Neural networks and PyTorch (22–30 hours)

| Lesson | Subject | Hands-on result | Est. time |
|---:|---|---|---:|
| 06 | Neural-network anatomy | NumPy multilayer network forward pass | 3–4h |
| 07 | Backpropagation | Manual computational graph and backward pass | 4–5h |
| 08 | PyTorch and autograd | Rebuild earlier model with tensors/autograd | 3–4h |
| 09 | First real neural network | Train, validate, save, and load a classifier | 4–6h |
| 10 | Generalization | Regularization, dropout, normalization experiments | 4–5h |
| Project B | Image classifier | Reproducible training and evaluation pipeline | 4–6h |

Exit criteria:

- trace shapes through a network;
- explain activations, capacity, backpropagation, and automatic differentiation;
- write a correct PyTorch training loop;
- diagnose unstable, overfit, and underfit training.

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
| Implement | Working lab and completed exercises |
| Investigate | Recorded experiment observations |
| Explain | Short plain-language and technical explanations |

Completion is based on evidence, not merely reading every page.
