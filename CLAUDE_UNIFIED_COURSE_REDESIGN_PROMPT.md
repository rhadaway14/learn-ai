# Claude Prompt — Unified Course and Project Experience

Copy the prompt below into Claude from the root of the latest `learn-ai` repository.

```text
You are redesigning the learner experience of the completed learn-ai retail semantic-search course.

The implementation is technically substantial, but a manual learner review found the Phase 1 and Phase 2 experiences confusing and not sufficiently helpful. The main design defect is structural: lessons and labs are separate experiences. Learners encounter concepts in one place and are then expected to infer how those concepts apply in another. The current labs also provide too little visual cause-and-effect and too little explanation of how each concept changes the cumulative retail project.

The approved change is:

- The course and the cumulative project become one seamless web experience.
- All required lesson content is taught inside the same UI that runs the project.
- Teaching alternates in small units with project interaction: learn, locate, predict, manipulate, observe, interpret, apply.
- The project map continuously shows where the current concept appears in the retail semantic-search system.
- The phase-ending “lab” becomes a phase integration checkpoint. It assembles and verifies work already completed during the five lessons; it does not introduce an unexplained second workflow.
- The core path has no mandatory free-text answers.
- The optional engineer path remains deep and code-aware, but it lives in the same UI and shares project state.
- Existing domain behavior, measured findings, numeric gates, artifact lineage, schema boundaries, security invariants, and deterministic evidence must be preserved.

Before editing, read these files completely:

- AGENTS.md
- COURSE_DESIGN.md
- LESSON_CONTRACT.md
- INTEGRATED_COURSE_EXPERIENCE.md
- RETAIL_SEMANTIC_SEARCH_IMPLEMENTATION.md
- STUDENT_READINESS.md
- docs/adr/0001-retail-semantic-search-capstone.md, if present
- docs/adr/0002-integrated-course-experience.md
- the current Phase 1 and Phase 2 API, web, content, tests, and Playwright flows

Treat INTEGRATED_COURSE_EXPERIENCE.md as normative for learner-facing delivery. Where older documents describe a standalone lesson followed by a separate lab, the integrated experience document wins. Do not weaken any model-quality, provenance, artifact, authorization, security, accessibility, or evaluation requirement from the retail implementation specification.

Do not begin by changing colors or rearranging cards. First identify the instructional and state architecture needed to make teaching and project work inseparable.

## Required work packages

### U0 — Baseline, content inventory, and migration plan

1. Inspect the current repository and worktree; preserve unrelated changes.
2. Run and record the complete current test baseline.
3. Inventory, for Lessons 1–10:
   - every concept and prerequisite;
   - where its explanation currently lives;
   - where its interaction currently lives;
   - the project component it changes or explains;
   - existing visual evidence and accessible equivalents;
   - duplicate, missing, or contradictory content;
   - progress keys, routes, artifacts, and tests affected by migration.
4. Produce a traceability matrix from each required concept to explanation, project location, interaction, visualization, interpretation check, saved evidence, and downstream reuse.
5. Propose the structured content schema and stable identifier strategy.
6. Propose progress migration behavior, including which old completion claims remain valid and which must be invalidated explicitly.
7. Add or update the architecture decision record and governing documents before implementation.

Do not claim a lesson is student-ready from component presence or test passage.

### U1 — Unified shell and content system

Implement the shared course shell and structured content system described in INTEGRATED_COURSE_EXPERIENCE.md:

- course rail with phase, lesson, concept, status, and prerequisites;
- learning canvas;
- persistent retail-project map;
- coach panel;
- evidence drawer;
- optional engineer drawer;
- structured, testable lesson content source;
- stable IDs and explicit progress migration;
- one canonical learner route;
- responsive and keyboard-accessible behavior.

The content system must support purpose, prerequisites, outcomes, explanation blocks, vocabulary, worked numeric math, project connections, interactions, predictions, interpretations, feedback, visuals, accessible equivalents, deep dives, completion requirements, and saved evidence.

Do not copy entire README files into a large scrolling component. Present a short explanation immediately before the interaction that uses it and an interpretation immediately after the evidence.

Add tests that fail if required teaching content, project linkage, feedback, visual alternative, or stable IDs are missing.

### U2 — Phase 1 integrated pilot

Rebuild Lessons 1–5 inside the unified UI. Each lesson must teach and apply its concepts to the actual retail project.

Required visual applications:

1. Lesson 1:
   - raw product, query, judgment, and event explorer;
   - visual distinction among feature, label, parameter, and hyperparameter;
   - training-versus-inference flow;
   - prediction line that visibly changes when weight or bias changes.
2. Lesson 2:
   - record-to-feature-row transformation;
   - named feature-matrix axes;
   - vectors and comparisons tied to real query-product records;
   - a shape-error view that explains why the meaning, not merely the dimensions, is wrong.
3. Lesson 3:
   - one real prediction decomposed into error, loss, gradient, and update;
   - stepwise movement on a loss surface;
   - learning-rate control tied to loss history and a controlled failure.
4. Lesson 4:
   - relevance-grade and click distributions;
   - repeated sample variation and uncertainty;
   - an explicit comparison showing why an observed click is not automatically relevance truth.
5. Lesson 5:
   - regression and classification on the same retail examples;
   - score/probability → threshold → decision flow;
   - confusion matrix and precision/recall consequences tied to review capacity.

For every major concept, implement the learn → locate → predict → manipulate → observe → interpret → apply loop when meaningful. Explanations and feedback must name the evidence on screen.

Replace the separate Phase 1 lab with an integration checkpoint in the same UI. It must recap and connect Lessons 1–5, run an end-to-end shopper-query scenario, compare baselines, perform a previously taught failure and recovery, run the gate, and automatically save/export the artifact. It must introduce no new concept or unfamiliar workflow.

### U3 — Phase 2 integrated pilot

After U2 passes automated checks, rebuild Lessons 6–10 using the same accepted components:

1. Lesson 6: animated feature-vector flow through layers, activations, output, shapes, and selected values.
2. Lesson 7: clearly separated forward and backward paths, local gradients, and one parameter update.
3. Lesson 8: synchronized conceptual graph, tensor state, autograd graph, gradients, and optional PyTorch code highlighting.
4. Lesson 9: train/validate/checkpoint flow, epoch evidence, held-out evaluation, and Phase 1 comparison.
5. Lesson 10: capacity and regularization controls, train/validation gap, fit diagnosis, and selected early-stopping checkpoint.

Replace the separate Phase 2 lab with a same-UI integration checkpoint that assembles the five taught capabilities and preserves the real model results and acceptance behavior.

Stop after U3 for manual learner review. Do not migrate Phases 3–7 until the user approves the Phase 1 and Phase 2 pattern.

## Interaction rules

- One primary action at a time.
- Never ask the learner to act on a concept before teaching it.
- Never begin a required step with a blank text area.
- Predictions and interpretation checks use authored options with misconception-specific feedback and retry.
- Controls expose one meaningful causal factor at a time, use safe ranges, show a default, and provide reset.
- Every result explains: what changed, why, how to tell, where it appears in the project, and where it appears in modern AI.
- Visually distinguish fixture data, learner choices, learned parameters, derived metrics, and acceptance decisions.
- Do not label a deterministic rule or template as model reasoning.
- Do not simulate a successful model, database, tool, or training result.
- Preserve the optional advanced path, but do not make it repair missing core explanations.

## Visualization rules

Every visual must have a teaching purpose, labels, units where applicable, current-state annotation, a plain-language interpretation, and a persistent table or text equivalent. Learner controls must map visibly to changed marks. Status may not depend on color alone. Honor reduced motion and support 320 CSS pixels.

Prefer:

- before/after comparisons;
- input → operation → output views;
- stepwise animations that can also be advanced manually;
- linked highlighting between prose, values, project component, visual, and optional code;
- real project data and real model state.

Avoid:

- decorative metric cards;
- unlabeled charts;
- animations that play without explaining state changes;
- long prose followed by an unrelated dashboard;
- controls that change several causal factors at once;
- a “correct” answer revealed before the learner predicts.

## Acceptance tests

Add automated checks for at least:

- complete concept-to-project traceability for Lessons 1–10;
- no required content available only in README/Markdown;
- stable and unique phase/lesson/concept/interaction IDs;
- explicit progress migration;
- prediction answers withheld until submission;
- specific feedback for every authored choice;
- content appears before the interaction that depends on it;
- every required visual has a data or text equivalent;
- keyboard-only completion;
- reduced-motion behavior;
- 320px viewport without horizontal page overflow;
- reload/resume at concept granularity;
- automatic same-session phase artifact transition;
- Phase 1 and Phase 2 end-to-end completion from a clean state;
- controlled failure and recovery;
- preservation of existing numeric results and acceptance invariants;
- preservation of all existing test suites.

Also provide a manual review script for both a novice engineer and an experienced engineer. It must ask the reviewer to rate, for every lesson:

- clarity of the explanation;
- helpfulness of the interaction;
- whether the visual made cause and effect visible;
- whether the project connection was obvious;
- whether the next action was obvious;
- remaining confusion.

## Engineering discipline

- Use the repository's existing architecture and shared components where they fit; do not rewrite model packages merely to support the new presentation.
- Keep domain logic out of React components.
- Do not scatter lesson prose across component literals; use a structured source of truth.
- Preserve unrelated changes.
- Add tests that fail against the pre-change behavior.
- Work in atomic commits, one work package per commit where practical.
- Run the complete relevant Python, JavaScript, TypeScript, browser, accessibility, schema, and container test suites.
- Report exact commands and results; do not summarize a red suite as passing.
- Do not mark Lessons 1–10 student-ready until manual review is recorded after U3.

Before starting U0, respond with:

1. your understanding of the design defect;
2. the learner journey you will implement;
3. the files and routes you expect U0 and U1 to affect;
4. the exact baseline commands you will run;
5. risks to content, progress, artifact lineage, and existing tests.

Then execute U0 through U3 in order, committing each work package. Stop after U3 and provide:

- commit SHAs;
- learner-visible changes;
- architecture and content-schema changes;
- progress migration behavior;
- traceability matrix location;
- exact automated test results;
- manual review instructions;
- known limitations;
- screenshots or routes for reviewing every Phase 1 and Phase 2 lesson and checkpoint.
```
