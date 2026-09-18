# Foundations Lab Runtime

The Foundations runtime is optional. Lessons 1–3 continue to work by opening `course.html` directly. This profile adds a served course UI, a small evidence API, and persistent SQLite experiment history.

## Start

```bash
docker compose --profile foundations up --build
```

Open:

- Course: <http://localhost:8080/course.html>
- Workbench: <http://localhost:8080/labs/foundations/>
- API health: <http://localhost:8081/health>

The API is intentionally a local teaching service. Compose restricts browser access to `http://localhost:8080`, limits request bodies to 64 KiB, and persists only learner-entered experiment notes. Port `8081` is published for local inspection; do not expose it to an untrusted network or treat it as a production service.

Stop containers with `Ctrl+C`, then run:

```bash
docker compose --profile foundations down
```

To deliberately remove saved experiment history:

```bash
docker compose --profile foundations down --volumes
```

The volume-removal command is destructive and is never required for normal lesson use.
