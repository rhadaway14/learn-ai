.PHONY: setup test lesson-01 lesson-02

setup:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest

lesson-01:
	python lessons/01_linear_regression/train.py

lesson-02:
	python lessons/02_vectors_matrices_tensors/lab.py
