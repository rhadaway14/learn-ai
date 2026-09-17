# Curriculum Artifact Schemas

These JSON Schemas make lesson activities and phase-project increments reviewable and testable without forcing learners to author JSON.

- `lesson-activity.schema.json` defines the instructional activity contract.
- `phase-project-increment.schema.json` defines the cumulative project contract.
- Learners normally fill in the corresponding Markdown files in `templates/`.
- Authors and future lab services may serialize the same fields as JSON for validation, progress tracking, downloads, or API storage.

Schema version `1.0` is intentionally independent of the course-progress browser-storage version. Breaking contract changes require a new schema version and a migration note.
