# Student-Readiness Review

This tracker distinguishes existing lesson files from lessons that have passed the teaching gate in [COURSE_DESIGN.md](COURSE_DESIGN.md).

The original repository scaffold implemented runnable topic demonstrations for all 35 lessons. It did not prove that every lesson contained enough instruction for a learner with an unknown background. Lessons 1–10 have now passed the internal teaching, artifact-contract, automated accessibility, and repository-consistency gates. An external learner pilot and real assistive-technology walkthrough remain required before claiming production-course validation. Lessons 11–35 still require individual instructional review.

| Lesson | Topic | Material exists | Student-ready | Capstone increment verified |
|---:|---|:---:|:---:|:---:|
| 01 | How machines learn | Yes | Yes | Yes |
| 02 | Vectors, matrices, and tensors | Yes | Yes | Yes |
| 03 | Loss functions and optimization | Yes | Yes | Yes |
| 04 | Probability and statistics | Yes | Yes | Yes |
| 05 | Regression and classification | Yes | Yes | Yes |
| 06 | Neural-network anatomy | Yes | Yes | Yes |
| 07 | Backpropagation from scratch | Yes | Yes | Yes |
| 08 | PyTorch and autograd | Yes | Yes | Yes |
| 09 | Train and evaluate a neural network | Yes | Yes | Yes |
| 10 | Regularization and generalization | Yes | Yes | Yes |
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

Lessons 1–10 are the approved browser-first pattern: approachable entry, explicit vocabulary, layered explanation, controlled interaction, visible feedback, a 500-word-or-greater advanced engineering section, real prerequisite declarations, and no required Python. Engineering Lab A is the explicit programming-readiness gate after Lesson 10. Later lessons must meet or deliberately adapt this pattern and must not be marked student-ready solely because scaffold files exist.
