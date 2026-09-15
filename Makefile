PYTHON ?= python

.PHONY: setup test labs lesson-01 lesson-02

setup:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest

labs:
	$(PYTHON) -c "from learn_ai.course_labs import LABS, run_lesson; [run_lesson(n) for n in LABS]"

lesson-01:
	$(PYTHON) lessons/01_linear_regression/train.py

lesson-02:
	$(PYTHON) lessons/02_vectors_matrices_tensors/lab.py
