#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "cases.json"


def load_cases() -> list[dict]:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise ValueError("evals/cases.json must be a JSON list")
    return cases


def validate(cases: list[dict]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for index, case in enumerate(cases, 1):
        if not isinstance(case, dict):
            errors.append(f"case #{index} must be an object")
            continue
        for field in ("id", "mode", "prompt", "must", "must_not"):
            if field not in case:
                errors.append(f"case #{index} missing {field}")
        case_id = case.get("id")
        if case_id:
            if case_id in seen:
                errors.append(f"duplicate case id: {case_id}")
            seen.add(case_id)
        if not isinstance(case.get("must", []), list) or not case.get("must", []):
            errors.append(f"{case_id or index}: must must be a non-empty list")
        if not isinstance(case.get("must_not", []), list):
            errors.append(f"{case_id or index}: must_not must be a list")
    if len(cases) < 8:
        errors.append("expected at least 8 regression cases")
    return errors


def print_case(case: dict) -> None:
    print(f"ID: {case['id']}")
    print(f"Mode: {case['mode']}")
    print("\nPrompt:\n" + case["prompt"])
    print("\nMUST:")
    for item in case["must"]:
        print(f"  - {item}")
    print("\nMUST NOT:")
    for item in case["must_not"]:
        print(f"  - {item}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect and validate undergrad-taoci behavior eval cases")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", action="store_true", help="list all eval cases")
    group.add_argument("--case", help="print one eval case")
    args = parser.parse_args()

    try:
        cases = load_cases()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1

    errors = validate(cases)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1

    if args.case:
        match = next((case for case in cases if case["id"] == args.case), None)
        if match is None:
            print(f"ERROR: unknown case: {args.case}")
            return 1
        print_case(match)
    elif args.list:
        for case in cases:
            print(f"{case['id']:<30} {case['mode']}")
    else:
        print(f"Eval specification looks good: {len(cases)} cases.")
        print("Note: this validates the eval specification, not live LLM behavior.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
