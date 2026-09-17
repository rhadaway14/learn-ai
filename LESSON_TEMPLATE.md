# Lesson NN — Title

This template implements [LESSON_CONTRACT.md](LESSON_CONTRACT.md). The core path is required; the Engineer deep dive is optional.

## Outcomes

After this lesson, you can:

- explain the primitive in plain language;
- implement its essential operation;
- recognize important tradeoffs and failure modes;
- connect it to a modern AI system.

## Prerequisites

- Prior concepts and lessons
- Required math and programming knowledge
- Required environment, account, or data

## Readiness check and bridge

Give a short diagnostic. For every missed prerequisite, point to the exact explanation or bridge exercise that repairs it.

## Mental model

Introduce the problem first, then the mechanism that solves it.

Include:

- one realistic scenario that remains consistent through the explanation;
- a familiar metaphor when it materially improves understanding;
- a short “where the metaphor stops” note;
- a return to the actual AI inputs, operation, output, and engineering use.

## Vocabulary

Define every new term before using it. Contrast easily confused terms.

## Math in layers

For every equation:

1. state the question it answers;
2. write the operation in plain language;
3. work an example with actual numbers;
4. show the symbolic form and define every symbol.

## Fully guided example

Complete one example for the learner. Explain why each action exists, what result to expect, and how to interpret it. Annotate every important tensor shape or state boundary.

## Scaffolded walkthrough

Progress from observing, to controlled changes, to partially guided work, to an independent challenge.

## Lab

Document the entry point, expected behavior, and generated artifacts.

```bash
python lessons/NN_topic/lab.py
```

## Exercises

Include implementation, prediction, and debugging exercises—not only recall questions.

## Experiments

Change one independent variable at a time. Record the hypothesis and observed result.

## Failure modes

Show how the technique fails, how that failure appears, and how to diagnose it.

## Connection to modern AI

Locate this primitive inside neural networks, transformers, retrieval, agents, training, or inference.

Give at least two concrete real-world applications and explain what role the primitive plays in each one.

## Where this fits in the AI story

Name the capability available before this lesson, the capability added now, the next limitation, and one modern AI use case. Use the shared `.ai-story` component in interactive lessons.

## Engineer deep dive

State additional prerequisites, then deepen the same topic through derivation, implementation mechanics, performance, production failure diagnosis, and architecture tradeoffs. End with a design or diagnostic task. Use the shared `.advanced-section` component.

## Hands-on activity

Use [templates/lesson-activity.md](templates/lesson-activity.md) and the `lesson-activity.schema.json` contract. Include guided, challenge, and optional engineer-extension levels, a failure experiment, saved evidence, recovery instructions, and explicit acceptance criteria.

## Capstone increment

Name the artifact this lesson adds or improves, its acceptance evidence, and where the learner will reuse it.

Also create or update the current phase-project increment using [templates/phase-project-increment.md](templates/phase-project-increment.md). Name its downstream consumer.

## Knowledge checkpoint

Include questions that require explanation and application.

## Definition of done

- [ ] Lab runs
- [ ] Exercises pass
- [ ] Experiments recorded
- [ ] Checkpoint answered in `PROGRESS.md`
- [ ] Plain-language and technical explanations completed
- [ ] Capstone increment produced and verified
- [ ] Student-ready acceptance gate in `COURSE_DESIGN.md` passed
