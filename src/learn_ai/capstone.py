"""Deterministic capstone control-flow demonstration."""

from learn_ai.course_labs import run_lesson


def run() -> dict:
    """Run the capstone's retrieval, evaluation, security, and approval gates."""
    retrieval = run_lesson(19)
    evaluation = run_lesson(24)
    security = run_lesson(26)
    workflow = run_lesson(35)
    return {
        "retrieval": retrieval,
        "evaluation": evaluation,
        "security": security,
        "workflow": workflow,
        "release_allowed": bool(
            retrieval["grounded"]
            and evaluation["passes"]
            and workflow["status"] != "executed"
        ),
    }
