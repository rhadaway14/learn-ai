"""Run the installed capstone demonstration from the repository."""

from learn_ai.capstone import run


if __name__ == "__main__":
    import json

    print(json.dumps(run(), indent=2))
