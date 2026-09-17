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

Stop containers with `Ctrl+C`, then run:

```bash
docker compose --profile foundations down
```

To deliberately remove saved experiment history:

```bash
docker compose --profile foundations down --volumes
```

The volume-removal command is destructive and is never required for normal lesson use.
