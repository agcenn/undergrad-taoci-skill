#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = ("examples", "evals", "templates")
PATTERNS = {
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-like secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "Chinese ID-like number": re.compile(r"(?<!\d)\d{17}[0-9Xx](?!\d)"),
    "Mainland China phone-like number": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
}
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@([A-Z0-9.-]+\.[A-Z]{2,})\b", re.I)
ALLOWED_EMAIL_DOMAINS = {"example.com", "example.org", "example.edu"}


def main() -> int:
    findings: list[str] = []
    files: list[Path] = []
    for directory in SCAN_DIRS:
        base = ROOT / directory
        if base.exists():
            files.extend(p for p in base.rglob("*") if p.is_file())

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(ROOT)
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{rel}: possible {label}")
        for match in EMAIL_RE.finditer(text):
            if match.group(1).lower() not in ALLOWED_EMAIL_DOMAINS:
                findings.append(f"{rel}: possible real email address")

    if findings:
        for finding in findings:
            print("ERROR:", finding)
        return 1

    print("Privacy audit passed: no obvious secrets or personal identifiers in examples/evals/templates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
