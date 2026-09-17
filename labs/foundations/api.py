"""Small dependency-free API for persisting Foundations activity evidence."""

from __future__ import annotations

import json
import os
import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Experiment:
    lesson: int
    activity_id: str
    hypothesis: str
    observation: str
    conclusion: str

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Experiment":
        lesson = payload.get("lesson")
        if lesson not in (1, 2, 3):
            raise ValueError("lesson must be 1, 2, or 3")
        expected = f"L{lesson:02d}-A1"
        if payload.get("activity_id") != expected:
            raise ValueError(f"activity_id must be {expected}")
        values = {key: str(payload.get(key, "")).strip() for key in ("hypothesis", "observation", "conclusion")}
        if any(len(value) < 3 for value in values.values()):
            raise ValueError("hypothesis, observation, and conclusion are required")
        return cls(lesson=lesson, activity_id=expected, **values)


class ExperimentStore:
    def __init__(self, path: str | Path):
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute("""CREATE TABLE IF NOT EXISTS experiments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson INTEGER NOT NULL,
                activity_id TEXT NOT NULL,
                hypothesis TEXT NOT NULL,
                observation TEXT NOT NULL,
                conclusion TEXT NOT NULL,
                created_at TEXT NOT NULL
            )""")

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        return connection

    def add(self, experiment: Experiment) -> dict[str, Any]:
        created_at = datetime.now(timezone.utc).isoformat()
        with self._connect() as connection:
            cursor = connection.execute(
                "INSERT INTO experiments (lesson, activity_id, hypothesis, observation, conclusion, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                (*asdict(experiment).values(), created_at),
            )
            identifier = cursor.lastrowid
        return {"id": identifier, **asdict(experiment), "created_at": created_at}

    def list(self) -> list[dict[str, Any]]:
        with self._connect() as connection:
            rows = connection.execute("SELECT * FROM experiments ORDER BY id DESC").fetchall()
        return [dict(row) for row in rows]


class FoundationsHandler(BaseHTTPRequestHandler):
    store: ExperimentStore

    def _send(self, status: HTTPStatus, payload: Any) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:  # noqa: N802
        self._send(HTTPStatus.NO_CONTENT, {})

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/health":
            self._send(HTTPStatus.OK, {"status": "ok", "service": "foundations-api"})
        elif self.path == "/api/experiments":
            self._send(HTTPStatus.OK, {"experiments": self.store.list()})
        else:
            self._send(HTTPStatus.NOT_FOUND, {"error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/api/experiments":
            self._send(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length) or b"{}")
            created = self.store.add(Experiment.from_payload(payload))
        except (ValueError, json.JSONDecodeError) as error:
            self._send(HTTPStatus.BAD_REQUEST, {"error": str(error)})
            return
        self._send(HTTPStatus.CREATED, created)

    def log_message(self, format: str, *args: Any) -> None:
        return


def run() -> None:
    path = os.environ.get("FOUNDATIONS_DB_PATH", "/data/experiments.db")
    port = int(os.environ.get("FOUNDATIONS_PORT", "8080"))
    FoundationsHandler.store = ExperimentStore(path)
    ThreadingHTTPServer(("0.0.0.0", port), FoundationsHandler).serve_forever()


if __name__ == "__main__":
    run()
