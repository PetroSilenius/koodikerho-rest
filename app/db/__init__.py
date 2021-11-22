import json
from pathlib import Path

with open(Path(__file__).resolve().parent.parent.parent / "initial-data.json") as f:
    data = json.load(f)
