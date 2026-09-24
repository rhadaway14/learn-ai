# Course Teaching and Readiness Standard

This curriculum is designed for engineers with uneven backgrounds. A learner may be strong in infrastructure, application development, databases, or architecture while having little experience with Python, statistics, calculus, or machine learning.

The course must teach the knowledge needed for its examples and capstone. Prior exposure may accelerate a learner, but it must not be required silently.

The required delivery model is defined in [INTEGRATED_COURSE_EXPERIENCE.md](INTEGRATED_COURSE_EXPERIENCE.md): lesson content and cumulative project work are one browser experience. A phase checkpoint assembles already-taught capabilities; it is not a separate lab in which the learner must infer how the lessons apply.

## The no-surprise rule

A graded exercise, lab, project, or capstone requirement may use a concept only after the course has:

1. introduced it in plain language;
2. defined its vocabulary and notation;
3. demonstrated it with a complete guided example;
4. given the learner supported practice;
5. checked the prerequisite understanding.

If a lesson needs knowledge that the course has not taught, the lesson must provide a bridge or link to an explicit prerequisite module. “The learner can look it up” is not an acceptable dependency.

## Required teaching sequence

The normative component and artifact structure is defined in [LESSON_CONTRACT.md](LESSON_CONTRACT.md). This document governs teaching quality; the contract governs how that quality appears consistently in every lesson.

Every student-ready lesson follows this sequence.

In the course UI, this sequence is delivered in short concept loops rather than as one long reading followed by a lab. Each major concept proceeds through **learn → locate → predict → manipulate → observe → interpret → apply**. “Locate” means showing the actual place where the concept changes or explains the retail semantic-search project.

### 1. Purpose before terminology

Begin with the problem and why it matters. Do not begin with framework names, equations, or implementation details.

### 2. Prior-knowledge check

State what the lesson assumes. Provide a short diagnostic and remediation links for any required math, programming, or system concept.

### 3. Plain-language mental model

Explain the mechanism without notation. Use one concrete example consistently rather than switching domains repeatedly.

### 3a. Concrete examples and responsible metaphors

Every major concept must include at least one realistic use and one familiar mental model when a metaphor genuinely improves understanding.

- State the concrete situation before abstracting it into variables or shapes.
- Explain exactly how the concept appears in an AI system or engineering workflow.
- Label metaphors as metaphors and state where each metaphor stops matching reality.
- Reuse a coherent scenario long enough for the learner to reason with it.
- Do not replace the mechanism with an analogy; return to the actual inputs, operation, output, and failure mode.

### 4. Vocabulary

Define every new term before using it. Distinguish terms that are commonly confused.

### 5. Math in three layers

Present mathematics in this order:

1. the question the equation answers;
2. the operation written in words with actual numbers;
3. the compact symbolic notation, with every symbol explained.

An equation must compress an idea the learner already understands. It must not be the first explanation of that idea.

### 6. Fully guided example

Demonstrate one complete example and explain why each action exists, what should happen, and how to interpret the result.

The example must use the same project data, component, and evidence the learner will manipulate next. A thematically similar toy example does not establish the project connection by itself.

### 7. Scaffolded practice

Practice progresses through four levels:

1. observe a completed example;
2. change controlled inputs and predict the result;
3. complete a partially guided task;
4. solve an independent challenge.

Early lessons may use a browser UI. When code becomes essential, the lesson must first teach the minimum code literacy required to run and modify the example.

### 8. Failure and diagnosis

Show at least one realistic failure. Teach the learner how to recognize it, explain its cause, and choose a response.

### 9. Understanding check

Include recall, interpretation, prediction, and application questions. A learner should not pass solely by recognizing vocabulary.

### 10. Capstone increment

State which capstone capability the lesson unlocks. The learner adds or improves a small capstone artifact before moving on.

The increment is performed in the same course UI and saved as part of the learner's project state. At the end of five lessons, the phase integration checkpoint verifies these increments together and introduces no untaught concept.

### 11. Two depths, one lesson

The required core path remains approachable to a learner with only the stated prerequisites. Each topic also provides an optional **Engineer deep dive** covering derivation, implementation mechanics, performance, production failure modes, and architecture tradeoffs. Advanced material must deepen the topic without becoming a hidden prerequisite for the required activity.

### 12. AI story and phase-project continuity

Every lesson identifies the capability available before the lesson, the capability added now, a modern AI use case, and the next capability it unlocks. Its hands-on activity produces evidence used by a named phase-project increment rather than ending as an isolated demonstration.

## Accessibility and ease-of-use standard

- The primary learning path must be obvious from the repository landing page.
- The required path must use one canonical course URL and a persistent navigation model.
- A learner must be able to complete the required path without opening a lesson README or a separate lab guide.
- Setup appears only when it becomes necessary.
- Commands must be copyable and include Windows, macOS, and Linux differences where relevant.
- Learners should change documented controls before editing implementation code.
- Interfaces must label outputs and explain what a successful result means.
- Every meaningful interaction must show what changed, why it changed, how to tell, where it appears in the project, and how the mechanism is used in modern AI.
- Visuals must expose cause and effect, respond visibly to learner controls, and include a persistent table or textual equivalent.
- Mathematical notation must render in GitHub and remain understandable as nearby prose.
- Every lab must include expected behavior and a recovery path for common errors.
- Required paid APIs, cloud accounts, and GPUs are prohibited unless a free/local path is provided.

## Code-readiness bridge

Lessons 1–10 are deliberately browser-first and require no Python knowledge. They may discuss what a program or framework does, but learner artifacts are observations, calculations, diagrams, protocols, specifications, and evidence cards—not runnable Python components.

**Engineering Lab A: Python and PyTorch Readiness** occurs after Lesson 10 and is a required release gate before any later lesson asks a learner to read, run, debug, or modify Python. It teaches:

- how to run a program and read an error;
- values, variables, lists, dictionaries, functions, and loops;
- package installation and virtual environments;
- reading shapes and printed structured output;
- changing documented configuration safely;
- running tests and interpreting pass/fail results.

Experienced Python developers may pass the diagnostic and skip the bridge exercises. Engineers from other languages can focus on syntax mapping rather than learning programming from scratch.

Maintainer reference programs may exist beside early lessons for validation and future development. They must be labeled as reference material and must not be presented as required learner work before Engineering Lab A. Course language must distinguish a **specification** (what a system must do and how its evidence is judged) from an **implementation** (runnable code that satisfies that contract).

## Student-ready acceptance gate

A lesson is student-ready only when all answers are yes.

| Area | Acceptance question |
|---|---|
| Purpose | Does the learner know why the topic exists before meeting its terminology? |
| Prerequisites | Are assumptions explicit, diagnosable, and remediable? |
| Concepts | Is every new term explained in plain language? |
| Examples | Does every major concept include a concrete use, and are metaphors useful and explicitly bounded? |
| Math | Is each equation motivated, worked numerically, and symbol-by-symbol defined? |
| Guidance | Is there a complete example before independent work? |
| Practice | Does support fade gradually instead of disappearing at once? |
| Feedback | Can the learner tell whether the result is correct and why? |
| Failure | Is at least one failure taught diagnostically? |
| Assessment | Do checks require explanation and application? |
| Continuity | Does the lesson identify prior dependencies and the next capability? |
| Capstone | Does the learner produce a small artifact reused later? |
| Integration | Is the concept taught and applied to the cumulative project in the same UI sequence? |
| Visualization | Does the interaction make cause and effect visible and explain the evidence? |
| Operations | Does the lab run through a documented, affordable path? |

“Implemented” means materials exist. “Student-ready” means the lesson passes this gate. Those statuses must not be conflated.

Automated checks alone cannot establish student readiness. Phase 1 and Phase 2 require recorded novice-engineer and experienced-engineer walkthroughs after the integrated redesign because manual review found the previous separated experience confusing.

## Instructor review questions

When reviewing a lesson, ask:

1. Where would a capable engineer new to this topic first become lost?
2. Did we explain the reason before the mechanism?
3. Did we introduce any symbol, command, library, or metric without teaching it?
4. Does the learner receive evidence that their work is correct?
5. Does the exercise test the stated outcome rather than unrelated setup skill?
6. What artifact survives and contributes to a later project or capstone?
