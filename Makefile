PYTHON ?= python

.PHONY: setup test labs foundations foundations-down phase2-start phase2-status phase2-test phase2-reset phase2-clean lesson-01 lesson-02

setup:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest

labs:
	$(PYTHON) -c "from learn_ai.course_labs import LABS, run_lesson; [run_lesson(n) for n in LABS]"

foundations:
	docker compose --profile foundations up --build

foundations-down:
	docker compose --profile foundations down

phase2-start:
	docker compose --profile phase2 up --build

phase2-status:
	docker compose --profile phase2 ps

phase2-test:
	docker compose --profile phase2 run --rm --no-deps phase2-api python -m labs.phase2.api.verify

phase2-reset:
	docker compose --profile phase2 stop phase2-web phase2-api phase2-db
	docker compose --profile phase2 rm --force phase2-web phase2-api phase2-db
	docker volume rm --force learn-ai-phase2-data learn-ai-phase2-artifacts
	docker compose --profile phase2 up --build

phase2-clean:
	docker compose --profile phase2 stop phase2-web phase2-api phase2-db
	docker compose --profile phase2 rm --force phase2-web phase2-api phase2-db
	docker volume rm --force learn-ai-phase2-data learn-ai-phase2-artifacts

lesson-01:
	$(PYTHON) lessons/01_linear_regression/train.py

lesson-02:
	$(PYTHON) lessons/02_vectors_matrices_tensors/lab.py
