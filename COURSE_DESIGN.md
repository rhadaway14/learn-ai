# Course Teaching and Readiness Standard

This curriculum is designed for engineers with uneven backgrounds. A learner may be strong in infrastructure, application development, databases, or architecture while having little experience with Python, statistics, calculus, or machine learning.

The course must teach the knowledge needed for its examples and capstone. Prior exposure may accelerate a learner, but it must not be required silently.

## The no-surprise rule

A graded exercise, lab, project, or capstone requirement may use a concept only after the course has:

1. introduced it in plain language;
2. defined its vocabulary and notation;
3. demonstrated it with a complete guided example;
4. given the learner supported practice;
5. checked the prerequisite understanding.

If a lesson needs knowledge that the course has not taught, the lesson must provide a bridge or link to an explicit prerequisite module. “The learner can look it up” is not an acceptable dependency.

## Required teaching sequence

Every student-ready lesson follows this sequence.

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

## Accessibility and ease-of-use standard

- The primary learning path must be obvious from the repository landing page.
- Setup appears only when it becomes necessary.
- Commands must be copyable and include Windows, macOS, and Linux differences where relevant.
- Learners should change documented controls before editing implementation code.
- Interfaces must label outputs and explain what a successful result means.
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
| Operations | Does the lab run through a documented, affordable path? |

“Implemented” means materials exist. “Student-ready” means the lesson passes this gate. Those statuses must not be conflated.

## Instructor review questions

When reviewing a lesson, ask:

1. Where would a capable engineer new to this topic first become lost?
2. Did we explain the reason before the mechanism?
3. Did we introduce any symbol, command, library, or metric without teaching it?
4. Does the learner receive evidence that their work is correct?
5. Does the exercise test the stated outcome rather than unrelated setup skill?
6. What artifact survives and contributes to a later project or capstone?
