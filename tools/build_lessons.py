"""Scaffold missing Lesson 03–35 files from lesson_catalog.tsv.

The generator never overwrites authored course material. Student-ready lessons
require human review against COURSE_DESIGN.md; catalog metadata is not enough to
generate an adequate explanation automatically.
"""

from __future__ import annotations

import re
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).parents[1]
CATALOG = Path(__file__).with_name("lesson_catalog.tsv")


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def slugify(title: str) -> str:
    return "_".join(re.findall(r"[a-z0-9]+", title.lower()))


def build() -> None:
    rows = CATALOG.read_text(encoding="utf-8").splitlines()
    index_rows = [
        "# Lesson Index",
        "",
        "Use this page to navigate the implemented curriculum.",
        "",
        "| Lesson | Topic | Materials |",
        "|---:|---|---|",
    ]
    progress_rows = [
        "# Progress Log",
        "",
        "Record checkpoint answers and experiment observations here or in separate journal files.",
        "",
    ]
    for row in rows:
        if not row or row.startswith("#"):
            continue
        fields = row.split("|")
        if len(fields) != 10:
            raise ValueError(f"Expected 10 fields, found {len(fields)}: {row[:80]}")
        number_text, title, why, concepts_text, experiment, failure, challenge, answer, questions_text, connection = fields
        number = int(number_text)
        concepts = concepts_text.split(";")
        questions = questions_text.split(";")
        slug = slugify(title)
        directory = ROOT / "lessons" / f"{number:02d}_{slug}"
        directory.mkdir(parents=True, exist_ok=True)

        outcomes = "\n".join(f"- Explain and apply {concept}." for concept in concepts)
        concept_lines = "\n".join(
            f"{index}. **{concept.capitalize()}** — identify its inputs, outputs, assumptions, and role."
            for index, concept in enumerate(concepts, 1)
        )
        question_lines = "\n".join(
            f"{index}. {question}" for index, question in enumerate(questions, 1)
        )
        readme = f"""# Lesson {number:02d} — {title}

## Why this matters

{why}

## Learning outcomes

{outcomes}

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

{concept_lines}

## Guided lab

From the repository root:

~~~bash
python lessons/{number:02d}_{slug}/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

{experiment}

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

{failure}

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

{challenge}

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

{question_lines}

## Connection to modern AI

{connection}

## Explain it at two levels

- **Plain language:** explain the purpose without equations or framework names.
- **Technical:** explain the mechanism, shapes or state, assumptions, metric, and failure mode.

## Definition of done

- [ ] Lab executed and output understood
- [ ] Primary experiment recorded
- [ ] Exercise completed before reviewing the solution
- [ ] Failure mode reproduced or analyzed
- [ ] Checkpoint answered in your own words
- [ ] Plain-language and technical explanations written
"""
        write_if_missing(directory / "README.md", readme)

        lab = dedent(
            f'''\
            """Lesson {number:02d}: {title}."""

            from learn_ai.course_labs import main


            if __name__ == "__main__":
                main({number})
            '''
        )
        write_if_missing(directory / "lab.py", lab)

        exercises = f"""# Lesson {number:02d} Exercises — {title}

## Implementation challenge

{challenge}

## Prediction

Before running the lab, predict its important output, state transition, tensor shape, or metric.

## Experiment record

{experiment}

| Field | Your notes |
|---|---|
| Hypothesis | |
| Independent variable | |
| Controlled variables | |
| Expected result | |
| Actual result | |
| Explanation | |

## Failure analysis

Reproduce or reason through this failure: {failure}

Document the detection signal, containment, and corrective action.
"""
        write_if_missing(directory / "EXERCISES.md", exercises)

        solutions = f"""# Lesson {number:02d} Reference Notes — {title}

Review this only after completing an attempt.

## Exercise approach

{answer}

## What a strong answer includes

- the mechanism rather than a memorized label;
- explicit inputs, outputs, state, or tensor shapes;
- a measurement or verification method;
- the important failure mode and mitigation;
- the connection to the larger AI system.

The reference is a minimum viable explanation, not the only valid solution.
"""
        write_if_missing(directory / "SOLUTIONS.md", solutions)
        relative = directory.relative_to(ROOT).as_posix()
        index_rows.append(
            f"| {number:02d} | {title} | [Lesson]({relative}/README.md) · "
            f"[Exercises]({relative}/EXERCISES.md) · [Reference]({relative}/SOLUTIONS.md) |"
        )
        progress_rows.extend(
            [
                f"## Lesson {number:02d} — {title}",
                "",
                "- [ ] Read the lesson and predict the lab result",
                "- [ ] Run the lab",
                "- [ ] Complete the exercise",
                "- [ ] Perform and record the experiment",
                "- [ ] Analyze the failure mode",
                "- [ ] Answer the checkpoint questions",
                "- [ ] Write plain-language and technical explanations",
                "",
                "Notes:",
                "",
            ]
        )

    lessons_root = ROOT / "lessons"
    existing = [
        "| 01 | Machine Learning and Linear Regression | "
        "[Lesson](01_linear_regression/README.md) |",
        "| 02 | Vectors, Matrices, and Tensors | "
        "[Lesson](02_vectors_matrices_tensors/README.md) · "
        "[Exercises](02_vectors_matrices_tensors/exercises.py) · "
        "[Reference](02_vectors_matrices_tensors/solutions.py) |",
    ]
    index_rows[6:6] = existing
    write_if_missing(lessons_root / "README.md", "\n".join(index_rows) + "\n")

    first_two = [
        "## Lesson 01 — Linear Regression",
        "",
        "- [ ] Run the lab and learning-rate experiments",
        "- [ ] Explain parameters, hyperparameters, training, inference, and generalization",
        "",
        "Notes:",
        "",
        "## Lesson 02 — Vectors, Matrices, and Tensors",
        "",
        "- [ ] Run the lab and complete exercises.py",
        "- [ ] Explain shapes, dot products, matrix multiplication, batching, and embeddings",
        "",
        "Notes:",
        "",
    ]
    progress_rows[4:4] = first_two
    write_if_missing(ROOT / "PROGRESS.md", "\n".join(progress_rows))


if __name__ == "__main__":
    build()
