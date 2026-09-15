# AI Engineering Learning

A hands-on curriculum that starts with machine-learning fundamentals and builds toward production AI systems, transformers, RAG, agents, evaluation, security, and advanced model architecture.

The complete path covers **35 lessons, five milestone projects, and one production-grade capstone**. See [CURRICULUM.md](CURRICULUM.md) for the phase-by-phase syllabus and estimated time commitment.

The governing rule is simple: **learn the primitive before using the framework that automates it**.

## Implemented curriculum

| Phase | Lessons | Major outcome |
|---|---:|---|
| Mathematical and ML foundations | 01–05 | Train and evaluate classical models from primitives |
| Neural networks and PyTorch | 06–10 | Understand backpropagation and complete training systems |
| Language-model mechanics | 11–16 | Build tokenization, attention, transformer, and decoding primitives |
| LLM application engineering | 17–23 | Build RAG, tools, agents, MCP, and multi-agent workflows |
| Quality and production | 24–30 | Evaluate, tune, secure, serve, and operate AI systems |
| Advanced systems and architecture | 31–35 | Analyze advanced models and deliver the capstone |

All 35 lessons are implemented. Browse the [lesson index](lessons/README.md) or read the detailed [curriculum](CURRICULUM.md).

## Quick start

Python 3.11–3.13 is supported.

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

Run the labs:

```bash
python lessons/01_linear_regression/train.py
python lessons/02_vectors_matrices_tensors/lab.py
python lessons/03_loss_functions_and_optimization/lab.py
python -m learn_ai.course_labs 35
```

Plots are written to each lesson's `outputs/` directory, so the labs also work in terminals without a desktop display.

## How to use each lesson

1. Read the lesson's `README.md`.
2. Run the reference lab and predict the output before inspecting it.
3. Complete `exercises.py` without reading `solutions.py`.
4. Run that lesson's tests.
5. Perform the experiments and answer the checkpoint questions in your own words.
6. Update [PROGRESS.md](PROGRESS.md).

## Repository map

```text
learn-ai/
├── README.md
├── ROADMAP.md
├── PROGRESS.md
├── CURRICULUM.md
├── STUDY_GUIDE.md
├── AGENTS.md
├── LESSON_TEMPLATE.md
├── projects/
├── capstone/
├── resources/
├── pyproject.toml
├── .gitignore
├── .github/workflows/tests.yml
├── lessons/
│   ├── 01_linear_regression/
│   │   ├── README.md
│   │   └── train.py
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
