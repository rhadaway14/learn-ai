# Repository Instructions

## Purpose

This repository is a cumulative, hands-on AI engineering curriculum. Preserve the progression from primitives to frameworks.

The required learner experience is governed by [INTEGRATED_COURSE_EXPERIENCE.md](INTEGRATED_COURSE_EXPERIENCE.md). Lessons and project work are taught through one persistent course UI; phase boundaries are integration checkpoints, not separate labs that introduce a second workflow.

## Lesson standard

Follow [COURSE_DESIGN.md](COURSE_DESIGN.md). A lesson is not student-ready merely because its files and lab exist.

Every implemented lesson should contain:

- explicit prerequisites, a diagnostic, and remediation for missing background;
- `README.md` with motivation, plain-language intuition, vocabulary, layered math, walkthrough, experiments, checkpoint questions, and modern-AI connection;
- a fully guided example before partially guided or independent work;
- runnable reference code;
- learner exercises or an experiment workbook;
- separate reference solutions or reference notes;
- a capstone increment defined in [CAPSTONE_PATH.md](CAPSTONE_PATH.md);
- deterministic automated tests where practical;
- no required paid service unless a local or free alternative is documented.

For learner-facing delivery, these elements must be interleaved with the project interaction rather than presented as a standalone document followed by a separate lab. A learner must be able to complete the required path without opening the lesson `README.md`.

## Engineering rules

- Support Python 3.11–3.13 unless a documented ML dependency prevents it.
- Pin compatible dependency ranges in `pyproject.toml`.
- Seed randomized educational examples.
- Write plots to an `outputs/` directory; do not require a desktop display.
- Never commit API keys, model credentials, datasets with restricted licenses, virtual environments, or generated model weights.
- Prefer direct NumPy/PyTorch implementations before high-level orchestration frameworks.
- Explain tensor shapes at each important boundary.
- Never make code syntax the accidental subject of a conceptual exercise.
- Introduce every equation in words and with actual numbers before symbolic notation.
- Ground every major concept in a realistic example and use clearly bounded metaphors where they improve understanding.
- Tie every major concept to a named component, input, output, metric, or decision in the cumulative retail project.
- Require meaningful visuals to show cause and effect, with a persistent table or textual equivalent.
- Keep required lesson content in a structured, testable source of truth rather than scattered through UI component literals.
- Keep tests fast; mark expensive or GPU-specific tests explicitly.

## Before committing

Run:

```bash
python -m pytest
```

Run every new or changed lesson entry point. Update `ROADMAP.md` and `PROGRESS.md` when a lesson becomes fully implemented.
