# AI Engineering Learning

A hands-on curriculum that starts with machine-learning fundamentals and builds toward production AI systems, transformers, RAG, agents, evaluation, security, and advanced model architecture.

The complete path covers **35 lessons, seven phase integration checkpoints, and one production-grade capstone**. See [CURRICULUM.md](CURRICULUM.md) for the phase-by-phase syllabus and estimated time commitment.

The governing rules are simple: **learn the primitive before using the framework that automates it**, and never require knowledge the course has not taught. See the [course teaching standard](COURSE_DESIGN.md) and [cumulative capstone path](CAPSTONE_PATH.md).

Every lesson follows the [reusable lesson contract](LESSON_CONTRACT.md) inside one [integrated course experience](INTEGRATED_COURSE_EXPERIENCE.md): the learner reads a short explanation, locates the concept in the retail project, predicts, manipulates, observes, interprets, and applies it without leaving the course UI. Every five lessons end in an integration checkpoint rather than a separate lab.

The cumulative retail semantic-search application is defined in the [retail semantic-search implementation specification](RETAIL_SEMANTIC_SEARCH_IMPLEMENTATION.md). [ADR 0002](docs/adr/0002-integrated-course-experience.md) records the approved decision to teach all lesson and project content through one seamless UI.

## Implemented curriculum

| Phase | Lessons | Major outcome |
|---|---:|---|
| Mathematical and ML foundations | 01–05 | Investigate classical models and evaluation from primitives |
| Neural networks and PyTorch concepts | 06–10 | Specify a reproducible training system and its evidence |
| Language-model mechanics | 11–16 | Build tokenization, attention, transformer, and decoding primitives |
| LLM application engineering | 17–23 | Build RAG, tools, agents, MCP, and multi-agent workflows |
| Quality and production | 24–30 | Evaluate, tune, secure, serve, and operate AI systems |
| Advanced systems and architecture | 31–35 | Analyze advanced models and deliver the capstone |

All 35 lessons have learning material, and each is reviewed individually against the stricter [student-readiness gate](STUDENT_READINESS.md). Lessons 1–10 are browser-first and require no Python. After Lesson 10, [**Engineering Lab A**](labs/engineering_lab_a/README.md) establishes Python, testing, and PyTorch readiness before programming becomes required. Browse the [lesson index](lessons/README.md) or read the detailed [curriculum](CURRICULUM.md).

## Quick start

### Learners starting Lesson 1

No programming environment is required.

1. Download the repository using GitHub's **Code → Download ZIP** option.
2. Extract the ZIP file.
3. Open `course.html` in Chrome, Edge, Firefox, or Safari.

The course dashboard launches interactive lessons, resumes the next unfinished lesson, and shows completed lessons. Progress is stored locally in the browser and requires no account.

The complete lesson and interactive lab run locally in the browser without an account, terminal, installation, or internet connection.

### Optional Foundations runtime

Lessons 1–3 also have an optional containerized Experiment Evidence Notebook that stores experiment evidence across sessions:

```bash
docker compose --profile foundations up --build
```

Open `http://localhost:8080/labs/foundations/`. Docker is not required for the core learning path. See [the Foundations runtime guide](labs/foundations/README.md).

### Engineering environment for later lessons

Python 3.11–3.13 is supported after the learner passes Engineering Lab A and reaches programming labs.

### Windows PowerShell

```powershell
git clone https://github.com/rhadaway14/learn-ai.git
cd learn-ai
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
```

### macOS/Linux

```bash
git clone https://github.com/rhadaway14/learn-ai.git
cd learn-ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e '.[dev]'
pytest
```

The course introduces programming only after teaching the required code literacy. Early learner-facing lessons use the browser; deterministic Python references remain available for maintainers and automated verification.

## How to use each lesson

1. Launch the canonical course UI.
2. Follow the course rail to the next lesson and concept.
3. Read the explanation beside the highlighted retail-project component.
4. Predict the result, change the bounded control, and observe the visual evidence.
5. Interpret the result with authored feedback and apply the decision to the project.
6. After five lessons, complete the integration checkpoint using only concepts already taught.
7. When a later lesson explicitly introduces programming, open the Engineer drawer for code, tests, and implementation exercises tied to the same state.

## Repository map

```text
learn-ai/
├── README.md
├── ROADMAP.md
├── PROGRESS.md
├── CURRICULUM.md
├── LESSON_CONTRACT.md
├── PHASE_PROJECTS.md
├── STUDY_GUIDE.md
├── AGENTS.md
├── LESSON_TEMPLATE.md
├── projects/
├── schemas/
├── templates/
├── activities/
├── phase-projects/
├── labs/
│   └── foundations/
├── compose.yaml
├── capstone/
├── resources/
├── pyproject.toml
├── .gitignore
├── .github/workflows/tests.yml
├── lessons/
│   ├── 01_linear_regression/
│   │   ├── README.md
│   │   ├── index.html
│   │   ├── styles.css
│   │   ├── app.js
│   │   └── train.py (maintainer reference)
│   ├── 02_vectors_matrices_tensors/
│   ├── 03_loss_functions_optimization/
│   └── ... through 35_capstone_production_grade_agentic_ai_platform/
├── src/learn_ai/
│   └── course_labs.py
├── tools/
│   ├── build_lessons.py
│   └── lesson_catalog.tsv
└── tests/
    ├── test_linear_regression.py
    └── test_linear_algebra.py
```

## Learning standard

A lesson is complete when you can:

- explain the concept without relying on unexplained jargon;
- implement the core operation;
- predict how changing inputs or hyperparameters affects the result;
- connect the primitive to modern AI systems;
- pass the automated tests.

## License

This learning repository is intended for personal and educational use.
