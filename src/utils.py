from datetime import datetime
import json
from pathlib import Path


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def pretty(data):
    print(json.dumps(data, indent=4))


def ensure_file(path: Path, default):

    if not path.exists():

        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf8") as file:

            json.dump(default, file, indent=4)


def read_json(path: Path):

    ensure_file(path, [])

    with open(path, encoding="utf8") as file:

        return json.load(file)


def write_json(path: Path, data):

    with open(path, "w", encoding="utf8") as file:

        json.dump(data, file, indent=4)
