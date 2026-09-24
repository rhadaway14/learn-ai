# Student-Readiness Review

This tracker distinguishes existing lesson files from lessons that have passed the teaching gate in [COURSE_DESIGN.md](COURSE_DESIGN.md).

The original repository scaffold implemented runnable topic demonstrations for all 35 lessons. It did not prove that every lesson contained enough instruction for a learner with an unknown background. Lessons 1–10 previously passed component, artifact-contract, automated accessibility, and repository-consistency gates. A subsequent manual learner review found the separated Phase 1 and Phase 2 lesson/lab experiences confusing and not sufficiently helpful. Their **student-ready status is therefore withdrawn** until they are rebuilt and manually revalidated under [INTEGRATED_COURSE_EXPERIENCE.md](INTEGRATED_COURSE_EXPERIENCE.md). Lessons 11–35 also require review in the integrated delivery model.

| Lesson | Topic | Material exists | Student-ready | Capstone increment verified |
|---:|---|:---:|:---:|:---:|
| 01 | How machines learn | Yes | Redesign required | Revalidation required |
| 02 | Vectors, matrices, and tensors | Yes | Redesign required | Revalidation required |
| 03 | Loss functions and optimization | Yes | Redesign required | Revalidation required |
| 04 | Probability and statistics | Yes | Redesign required | Revalidation required |
| 05 | Regression and classification | Yes | Redesign required | Revalidation required |
| 06 | Neural-network anatomy | Yes | Redesign required | Revalidation required |
| 07 | Backpropagation from scratch | Yes | Redesign required | Revalidation required |
| 08 | PyTorch and autograd | Yes | Redesign required | Revalidation required |
| 09 | Train and evaluate a neural network | Yes | Redesign required | Revalidation required |
| 10 | Regularization and generalization | Yes | Redesign required | Revalidation required |
| 11–16 | Language-model mechanics | Yes | Review required | Review required |
| 17–23 | LLM application engineering | Yes | Review required | Review required |
| 24–30 | Evaluation, security, and operations | Yes | Review required | Review required |
| 31–34 | Advanced systems and architecture | Yes | Review required | Review required |
| 35 | Capstone integration | Yes | Review required | Final gate |

## Review evidence required

For each lesson, record:

- reviewer and date;
- assumed learner background;
- prerequisite diagnostic results;
- explanation gaps found and resolved;
- guided example completed;
- lab run through the learner-facing path;
- knowledge-check coverage;
- capstone artifact and acceptance evidence;
- accessibility and setup issues;
- final student-ready decision.

For lessons using the reusable contract, also apply [PERSONA_TESTING.md](PERSONA_TESTING.md). Component presence is not sufficient: record both novice and experienced-engineer walkthrough evidence. The current reference result is [the Lessons 1–3 pre-pilot review](evaluations/persona-review-foundations-reference.md).

## Current course promise

Lessons 1–10 remain browser-first and require no Python, but the previous separated lesson/lab pattern is not approved for reuse. The replacement pattern is one continuous UI with concept-level teaching, visible project mapping, causal visualization, bounded interaction, authored interpretation feedback, and saved cumulative project state. Engineering Lab A remains the programming-readiness gate after Lesson 10. No lesson may be marked student-ready solely because content, components, or automated tests exist.
