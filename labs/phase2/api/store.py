from __future__ import annotations

import json
import os
import time
from typing import Any


class MemoryStore:
    def __init__(self) -> None:
        self.phase1: list[dict[str, Any]] = []
        self.runs: list[dict[str, Any]] = []
        self.artifacts: list[dict[str, Any]] = []

    def initialize(self) -> None:
        return

    def save_phase1(self, artifact: dict[str, Any]) -> str:
        identifier = f"phase1-attempt-{artifact['attempt_number']}"
        self.phase1.append({"id": identifier, "artifact": artifact})
        return identifier

    def latest_phase1(self) -> dict[str, Any] | None:
        return self.phase1[-1] if self.phase1 else None

    def save_run(self, evidence: dict[str, Any]) -> int:
        identifier = len(self.runs) + 1
        self.runs.append({"id": identifier, "evidence": evidence})
        return identifier

    def list_runs(self) -> list[dict[str, Any]]:
        return list(reversed(self.runs))

    def next_attempt(self) -> int:
        return len(self.artifacts) + 1

    def save_artifact(self, artifact: dict[str, Any]) -> None:
        self.artifacts.append(artifact)


class PostgresStore:
    def __init__(self, dsn: str | None = None) -> None:
        self.dsn = dsn or os.environ.get(
            "PHASE2_DATABASE_URL",
            "postgresql://learn_ai:learn_ai@phase2-db:5432/learn_ai",
        )

    def _connect(self):
        import psycopg

        return psycopg.connect(self.dsn)

    def initialize(self, attempts: int = 30) -> None:
        last_error: Exception | None = None
        for _ in range(attempts):
            try:
                with self._connect() as connection:
                    connection.execute(
                        """CREATE TABLE IF NOT EXISTS phase2_phase1_evidence (
                            id BIGSERIAL PRIMARY KEY,
                            evidence_id TEXT NOT NULL,
                            artifact JSONB NOT NULL,
                            created_at TIMESTAMPTZ NOT NULL DEFAULT now()
                        )"""
                    )
                    connection.execute(
                        """CREATE TABLE IF NOT EXISTS phase2_runs (
                            id BIGSERIAL PRIMARY KEY,
                            evidence JSONB NOT NULL,
                            created_at TIMESTAMPTZ NOT NULL DEFAULT now()
                        )"""
                    )
                    connection.execute(
                        """CREATE TABLE IF NOT EXISTS phase2_artifacts (
                            id BIGSERIAL PRIMARY KEY,
                            attempt_number INTEGER NOT NULL UNIQUE,
                            artifact JSONB NOT NULL,
                            created_at TIMESTAMPTZ NOT NULL DEFAULT now()
                        )"""
                    )
                return
            except Exception as error:  # database container may still be starting
                last_error = error
                time.sleep(1)
        raise RuntimeError(f"database unavailable after {attempts} attempts: {last_error}")

    def save_phase1(self, artifact: dict[str, Any]) -> str:
        evidence_id = f"phase1-attempt-{artifact['attempt_number']}"
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO phase2_phase1_evidence (evidence_id, artifact) VALUES (%s, %s::jsonb)",
                (evidence_id, json.dumps(artifact)),
            )
        return evidence_id

    def latest_phase1(self) -> dict[str, Any] | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT evidence_id, artifact FROM phase2_phase1_evidence ORDER BY id DESC LIMIT 1"
            ).fetchone()
        return {"id": row[0], "artifact": row[1]} if row else None

    def save_run(self, evidence: dict[str, Any]) -> int:
        with self._connect() as connection:
            row = connection.execute(
                "INSERT INTO phase2_runs (evidence) VALUES (%s::jsonb) RETURNING id",
                (json.dumps(evidence),),
            ).fetchone()
        return int(row[0])

    def list_runs(self) -> list[dict[str, Any]]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT id, evidence, created_at FROM phase2_runs ORDER BY id DESC LIMIT 20"
            ).fetchall()
        return [
            {"id": int(row[0]), "evidence": row[1], "created_at": row[2].isoformat()}
            for row in rows
        ]

    def next_attempt(self) -> int:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT COALESCE(MAX(attempt_number), 0) + 1 FROM phase2_artifacts"
            ).fetchone()
        return int(row[0])

    def save_artifact(self, artifact: dict[str, Any]) -> None:
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO phase2_artifacts (attempt_number, artifact) VALUES (%s, %s::jsonb)",
                (artifact["attempt_number"], json.dumps(artifact)),
            )
