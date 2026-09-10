#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    [sys.executable, str(ROOT / "scripts" / "validate_skill.py")],
    [sys.executable, str(ROOT / "scripts" / "validate_profile.py"), str(ROOT / "examples" / "student-profile.example.json")],
    [sys.executable, str(ROOT / "scripts" / "run_evals.py")],
    [sys.executable, str(ROOT / "scripts" / "audit_privacy.py")],
]


def main() -> int:
    for command in CHECKS:
        print("\n$ " + " ".join(command), flush=True)
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode != 0:
            print("\nChecks failed.")
            return result.returncode
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
