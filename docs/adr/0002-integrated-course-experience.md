# ADR 0002: Integrate Lessons and Project Work in One Course UI

- **Status:** Accepted
- **Date:** 2026-09-24
- **Supersedes:** The learner-facing separation between standalone lessons and phase-ending labs
- **Preserves:** The cumulative retail semantic-search architecture and technical acceptance requirements

## Context

Manual learner review of the Phase 1 and Phase 2 experiences found them confusing and not sufficiently helpful. Although the technical implementations and tests were substantial, learners had to move between lesson material and a separate lab, infer how concepts applied to the retail project, and interpret visuals that did not expose enough cause and effect.

The defect is not limited to wording or styling. The delivery model separates explanation from application.

## Decision

The required course path will be taught through one persistent web application.

Every major concept will use a short **learn → locate → predict → manipulate → observe → interpret → apply** loop tied to the live retail semantic-search project. The UI will continuously show where the concept appears in the project, what data enters it, what it produces, what changed, and why the result matters.

The former phase-ending lab becomes a **phase integration checkpoint**. It combines, compares, breaks, recovers, verifies, promotes, and exports capabilities already taught during the five lessons. It may not introduce unexplained concepts or a new interaction model.

Lesson Markdown remains maintainer/reference material and an accessible export. It is not part of the required navigation path. The optional Engineer path remains available inside the same UI and shares the same project state.

The detailed learner, visualization, content, progress, migration, and acceptance requirements are defined in [../../INTEGRATED_COURSE_EXPERIENCE.md](../../INTEGRATED_COURSE_EXPERIENCE.md).

## Consequences

### Positive

- Explanation and application occur together.
- Every topic is visibly connected to the cumulative project.
- Phase checkpoints validate integration instead of testing a learner's ability to infer the lab workflow.
- Progress can be measured at concept granularity.
- Core and advanced learners use one project state and one navigation model.
- Visualizations can be tested against an explicit teaching purpose.

### Costs and risks

- Lesson content needs a structured, testable source of truth.
- Existing completion records require explicit migration.
- Duplicated lesson and lab routes cannot be removed until parity is verified.
- The first two phases must be rebuilt and manually reviewed before the pattern is generalized.
- More UI integration increases the importance of browser, accessibility, and content-contract tests.

## Rejected alternatives

### Improve the labs while retaining separate lesson pages

Rejected because the learner would still need to perform the conceptual mapping between two experiences.

### Embed complete lesson documents above the existing labs

Rejected because this would create long reading blocks followed by disconnected interaction rather than interleaving explanation and evidence.

### Add more charts without changing the journey

Rejected because visualization quantity does not guarantee understanding. Each visual must expose a mechanism or comparison and be tied to a learner-controlled cause.

### Rebuild all seven phases immediately

Rejected because the Phase 1 and Phase 2 learner experience must be validated before it becomes the pattern for the remaining course.

## Validation

Acceptance requires automated contract, progress, accessibility, responsive, browser, and existing domain tests, followed by separate novice-engineer and experienced-engineer manual reviews of Phases 1 and 2. Automated test passage alone does not restore student-ready status.
