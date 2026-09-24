# Integrated Course Experience — Design Contract

## Status

This document is normative for learner-facing delivery of the retail semantic-search course. It supersedes any earlier requirement that learners read a standalone lesson and later enter a separate phase lab to discover how the topic applies.

The mathematical, model, dataset, artifact, security, and operations requirements in [RETAIL_SEMANTIC_SEARCH_IMPLEMENTATION.md](RETAIL_SEMANTIC_SEARCH_IMPLEMENTATION.md) remain in force. This document changes how those requirements are taught and experienced.

## 1. Design decision

The course and the cumulative retail project are one experience.

The required learner path lives entirely in the course web application. A learner must not have to alternate among lesson Markdown, a separate lesson page, a phase lab, and repository instructions to understand a topic. Markdown remains useful as source material, maintainer documentation, and an accessible export, but it is not a prerequisite for completing the course.

There are no separate phase-ending labs in the learner's mental model. Each lesson teaches concepts by changing, inspecting, or evaluating the same retail semantic-search application. At the end of every five lessons, a **phase integration checkpoint** assembles and verifies capabilities the learner has already built. The checkpoint may compare, break, recover, promote, and export; it must not introduce an unexplained workflow or ask the learner to infer how the preceding lessons connect.

## 2. Learner promise

At every point, the interface must answer five questions without requiring the learner to search another document:

1. What problem are we solving?
2. What concept explains this part of the solution?
3. Where does the concept appear in the retail application?
4. What changed when I interacted with it, and why?
5. How is this mechanism used in modern AI systems?

The learner reads a short explanation, predicts an outcome, manipulates a bounded control, observes a meaningful visual change, receives an interpretation, and applies the idea to the project. Teaching and doing alternate in small units; the course must not front-load a long chapter and postpone all application until the end.

## 3. Information architecture

### 3.1 One course shell

The required path uses one persistent application shell:

- **Course rail** — phase, lesson, concept, completion state, and prerequisites.
- **Learning canvas** — the current explanation, worked example, interaction, and evidence.
- **Project map** — the retail-search pipeline with the current component highlighted.
- **Coach panel** — what to notice, why the result matters, misconceptions, and recovery help.
- **Evidence drawer** — the learner's saved choices, configurations, results, and artifact lineage.
- **Engineer drawer** — optional code, requests, tensor details, tests, performance, and architecture tradeoffs.

The shell persists across all 35 lessons. Navigation may change the current content, but it must not make the learner feel that they have left the course and entered an unrelated tool.

### 3.2 Persistent project map

The project map shows the evolving application:

```text
shopper request
    → data and features
    → models and representations
    → retrieval and ranking
    → grounded generation and tools
    → evaluation, security, and operations
    → verified production architecture
```

For the current concept, the map must show:

- the active component;
- the input entering it;
- the output leaving it;
- the capability that existed before this lesson;
- the capability being added now;
- the next downstream consumer.

A project connection cannot be satisfied by a generic paragraph saying that the topic is “used in AI.” It must name the actual package, model, endpoint, dataset field, UI behavior, metric, or artifact affected in this retail application.

## 4. Concept learning loop

Every major concept is delivered as a short loop. A lesson normally contains several loops.

| Beat | Learner experience | Required UI evidence |
|---|---|---|
| **Learn** | Read the problem, intuition, vocabulary, and—when relevant—math in words, numbers, then symbols | Short content blocks; defined terms; worked numeric example |
| **Locate** | See exactly where the concept exists in the retail project | Highlighted project map, real inputs and outputs, upstream/downstream labels |
| **Predict** | Choose what should happen before running it | Two to four authored choices with no answer leaked in advance |
| **Manipulate** | Change one bounded, meaningful control | Labeled control, safe range or options, sensible default, reset |
| **Observe** | Run the real mechanism and see cause and effect | Animated or stepwise state change, comparison, persistent data equivalent |
| **Interpret** | Select the explanation supported by the evidence | Authored choices with specific feedback and retry; no mandatory free text |
| **Apply** | Use the concept to improve or diagnose the retail application | Saved decision, result, project capability, and downstream reuse |

The learner must be able to pause after **Observe** and answer: “I changed X; Y changed because Z.” If the interface cannot make that sentence concrete, the interaction is not finished.

## 5. Content contract

Every lesson presented in the UI includes:

- purpose and realistic retail problem;
- explicit prerequisites and remediation;
- learning outcomes stated as observable abilities;
- plain-language mental model;
- defined vocabulary before use;
- bounded metaphor where helpful, including where it stops matching reality;
- math in the order: question, words, worked numbers, symbols;
- one fully guided worked example;
- one or more concept learning loops;
- a realistic failure and recovery;
- explicit connection to the live retail project;
- explicit connection to a modern AI use case;
- optional Engineer deep dive;
- comprehension checks with authored feedback;
- saved project evidence and definition of done.

Content must be broken into readable units. Do not reproduce an entire README in a single scrolling panel. A concept explanation should appear immediately before the interaction that uses it, and its interpretation immediately after the evidence appears.

## 6. Visualization contract

Visuals must reveal a mechanism, relationship, comparison, or change. Decorative charts do not count.

Every visual must include:

- a question or claim it helps answer;
- readable title, labels, units, legend, and current-state annotation;
- a clear mapping between learner controls and changed marks;
- a visible before/after, baseline/current, or input/output relationship when applicable;
- a plain-language “What this shows” interpretation;
- a persistent table or textual equivalent;
- keyboard access, non-color status cues, and reduced-motion behavior.

The interface must visually distinguish:

- **data** supplied by the fixture;
- **learner choices** such as a threshold or model width;
- **learned values** such as weights;
- **derived evidence** such as loss or recall;
- **acceptance decisions** such as promote or withhold.

### 6.1 Required Phase 1 visuals

| Lesson | Required visual application |
|---:|---|
| 01 | Raw product/query/judgment explorer; feature vs label vs parameter map; training-versus-inference flow; a prediction line changing as weight and bias change |
| 02 | Named feature-matrix axes; record-to-row transformation; vector comparison; shape mismatch visual that explains the semantic error |
| 03 | One prediction decomposed into error, loss, gradient, and update; stepwise movement on a loss surface; loss history with the selected learning rate |
| 04 | Relevance-grade and click distributions; repeated samples; uncertainty interval; observed click compared with latent relevance |
| 05 | Regression and classification views on the same examples; probability/score to threshold to decision; confusion matrix and precision/recall tradeoff tied to review capacity |

### 6.2 Required Phase 2 visuals

| Lesson | Required visual application |
|---:|---|
| 06 | Feature vector flowing through neurons, layers, activations, and output; shapes and selected numeric values at each boundary |
| 07 | Forward computation followed by a visually distinct backward gradient path; local gradients and one parameter update |
| 08 | Synchronized conceptual graph, tensor state, autograd graph, gradients, and optional PyTorch code drawer |
| 09 | Training/validation loop, epoch metrics, checkpoint selection, held-out results, and Phase 1 baseline comparison |
| 10 | Capacity and regularization controls; train/validation gap; underfit/appropriate/overfit diagnosis; early-stopping checkpoint |

Later phases apply the same standard to tokenization, embeddings, attention, retrieval ranks, RAG evidence, tool traces, evaluation slices, security attacks, multimodal signals, telemetry, scaling, and verification.

## 7. Phase integration checkpoints

After the fifth lesson in each phase, the learner reaches a checkpoint in the same UI. It must:

1. recap the five capabilities already added;
2. show how data flows through them together;
3. run a guided end-to-end scenario;
4. compare against the phase's starting baseline;
5. trigger one controlled failure already taught in the lessons;
6. guide recovery using concepts already taught;
7. run deterministic acceptance checks;
8. promote or withhold the phase capability with a specific explanation;
9. export the versioned evidence artifact automatically;
10. preview what the artifact unlocks next.

Artifact import/export remains part of the engineering model, but it should be automatic on the normal path. Manual download and import may exist in the Engineer drawer for teaching provenance and recovery. A learner should not be blocked by file handling between adjacent phases in the same browser session.

## 8. Progress and assessment

Progress is recorded at the concept, lesson, and phase levels.

A concept is complete only after the learner has:

- viewed its essential explanation;
- made the prediction where required;
- run the interaction;
- viewed the evidence;
- completed the interpretation check;
- applied or saved the project decision.

Completion is based on observable actions and evidence, not scrolling time, confidence, or prose length. Required assessment uses bounded controls, ordering, matching, multiple choice, or direct manipulation. Optional reflection may be saved but is never graded mechanically.

Wrong answers must return misconception-specific feedback and point the learner back to the exact evidence needed. They must not merely say “incorrect.”

## 9. Core and engineer paths

Both paths use the same UI and the same project state.

The core path teaches enough to understand and complete the project without reading source code. The Engineer drawer deepens the current concept with code-to-visual highlighting, exact requests and responses, tensor shapes, schema and database views, performance, tests, failure injection, and architecture tradeoffs.

After the programming-readiness bridge, engineer activities may ask the learner to modify code, but the UI must still explain the concept and show the result. Code does not replace teaching.

## 10. Technical content architecture

Lesson content must have a structured, testable source of truth rather than being scattered across React component strings.

At minimum, the content model represents:

- phase, lesson, concept, ordering, prerequisites, and outcomes;
- explanation blocks, vocabulary, worked examples, and math notation;
- project component and data-flow connections;
- interaction type, controls, defaults, and expected evidence;
- prediction and interpretation choices with feedback;
- visualization contract and accessible equivalent;
- optional Engineer deep dive;
- completion requirements and evidence keys.

The API and web application must agree on stable identifiers. Progress migration must preserve any evidence that still maps unambiguously; incompatible completion claims must be invalidated explicitly rather than silently marked complete.

Markdown lesson files should be generated from, synchronized with, or validated against the structured source. Two independent, drifting versions of the lesson are not acceptable.

## 11. Acceptance criteria

The unified design is accepted only when all of the following are true:

- A learner can start at Lesson 1 and complete the required course path without opening a README.
- There is one canonical course URL and one persistent navigation model.
- Every required concept in Lessons 1–10 is taught inside the UI before it is used.
- Every concept in Lessons 1–10 identifies and visibly highlights its retail-project location.
- Phase 1 and Phase 2 checkpoints contain no new unexplained concept or workflow.
- Every interaction provides prediction, visible cause and effect, interpretation, and project application where those beats are meaningful.
- The required Phase 1 and Phase 2 visuals in this document exist and have accessible equivalents.
- No mandatory free-text answer or source-code edit exists before its prerequisite is taught.
- Existing numeric, provenance, artifact-chain, security, and model-integrity tests remain valid.
- Automated tests verify content completeness, stable IDs, progress migration, feedback, accessibility, small viewport behavior, and end-to-end checkpoint completion.
- A novice-engineer walkthrough and an experienced-engineer walkthrough are recorded separately.
- Manual learner review explicitly rates clarity, helpfulness, visual explanation, project connection, and confidence about the next action.

## 12. Migration sequence

Do not restyle all seven phases at once.

1. Record the current behavior and test baseline.
2. Add the structured content model and persistent shell without changing model results.
3. Rebuild Phase 1 lessons and checkpoint in the unified experience.
4. Conduct a manual learner review and resolve blocking confusion.
5. Rebuild Phase 2 lessons and checkpoint using the validated pattern.
6. Conduct a second manual learner review.
7. Generalize the accepted components and migrate Phases 3–7.
8. Remove or redirect obsolete standalone learner routes only after parity, progress migration, and accessibility checks pass.

The Phase 1 and Phase 2 redesign is the pattern-setting pilot. Passing unit tests alone is insufficient authorization to copy the pattern into later phases.
