#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REQUIRED = ("school", "major", "year")
RECOMMENDED = ("courses", "skills", "projects", "research_interests")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python scripts/validate_profile.py <profile.json>")
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read profile: {exc}")
        return 1

    missing = [key for key in REQUIRED if not data.get(key)]
    if missing:
        print("ERROR: missing required fields: " + ", ".join(missing))
        return 1

    warnings = [key for key in RECOMMENDED if key not in data]
    if warnings:
        print("WARN: recommended fields not present: " + ", ".join(warnings))
    else:
        print("Profile looks good: all recommended fields are present.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
