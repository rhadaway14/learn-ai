# Persona Validation Protocol

This protocol tests whether the same lesson works for learners with different starting points. Personas are heuristic review lenses, not substitutes for observed sessions with real people.

## Persona N — New-to-AI engineer

**Background:** technically capable, but may not know Python, calculus, machine-learning terminology, or tensor notation.

**Success criteria:**

- can identify the required path without opening optional advanced material;
- understands every required term before it is used in an activity;
- can complete the core activity without source-code editing or Docker;
- can predict, observe, explain, and recover from one failure;
- knows exactly what artifact to save and how it feeds the project;
- can distinguish “I completed the interaction” from “I understand the evidence.”

## Persona E — Experienced engineer

**Background:** strong software, systems, data, or architecture experience and comfortable with technical tradeoffs, but not necessarily an ML specialist.

**Success criteria:**

- can find advanced depth from the lesson entrance;
- receives more than repeated beginner prose;
- encounters derivation or mechanics, scale, production failures, and architecture tradeoffs;
- has an optional implementation or diagnostic extension;
- can connect the primitive to current AI systems;
- produces evidence useful in a design or operational review.

## Walkthrough procedure

For each persona and lesson:

1. Start from `course.html`, without using repository source files.
2. State which route appears required and which appears optional.
3. Complete the prerequisite check and follow one remediation link if available.
4. Read the core explanation and complete every required interaction.
5. Predict before changing activity controls; record observation and interpretation.
6. Trigger the documented failure and follow the recovery path.
7. Locate the AI-story, activity artifact, phase increment, and next consumer.
8. For Persona E, open the Engineer deep dive and perform the extension as far as current prerequisites permit.
9. Score each rubric item and record the first point of hesitation.

## Scoring rubric

Score each dimension from 1 to 5.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Path clarity | Required route is unclear | Route can be inferred | Core and optional routes are explicit at entry |
| Prerequisite safety | Hidden prerequisites block progress | Some bridging exists | Every required prerequisite is taught or remediated |
| Interaction feedback | Result is unexplained | Result is visible | Result, meaning, failure, and recovery are explicit |
| Activity completion | Learner must invent process | Goal exists but evidence is vague | Mission, levels, evidence, artifact, and acceptance are explicit |
| Continuity | Lesson feels isolated | Later relevance is mentioned | Prior, current, next, modern use, and project reuse are visible |
| Advanced value | Repeats introductory prose | Adds selected detail | Adds mechanics, scale, failure diagnosis, tradeoffs, and extension |
| Operational ease | Setup dominates learning | Setup is documented | Required path is zero-setup; optional runtime fails clearly |

A reference lesson passes when neither persona scores below 4 on any applicable dimension. A human pilot may override a heuristic pass when observed behavior contradicts the document review.

## Human pilot capture

Record:

- participant background without personally identifying information;
- start/end time and route chosen;
- first hesitation and first incorrect prediction;
- help or remediation used;
- activity artifact produced;
- rubric scores and direct paraphrased feedback;
- issue severity: blocking, confusing, inefficient, or polish;
- proposed change and retest result.

Do not mark a future lesson persona-validated solely because its HTML contains the expected component names.
