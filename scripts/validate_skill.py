#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
OPENAI_YAML = ROOT / "agents" / "openai.yaml"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def main() -> int:
    errors: list[str] = []

    if not SKILL.exists():
        errors.append("missing SKILL.md")
    else:
        text = SKILL.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(str(exc))
            meta = {}

        name = meta.get("name", "")
        description = meta.get("description", "")
        if not name:
            errors.append("frontmatter missing name")
        elif len(name) > 64 or not NAME_RE.fullmatch(name):
            errors.append("name must be <=64 chars and lower-case hyphen-case")
        if not description:
            errors.append("frontmatter missing description")
        if len(description) < 80:
            errors.append("description is too short to express triggers and boundaries")

        refs = sorted(set(re.findall(r"`(references/[^`]+\.md)`", text)))
        for ref in refs:
            if not (ROOT / ref).exists():
                errors.append(f"missing referenced file: {ref}")

    if not OPENAI_YAML.exists():
        errors.append("missing agents/openai.yaml")
    else:
        yaml_text = OPENAI_YAML.read_text(encoding="utf-8")
        for field in ("interface:", "display_name:", "short_description:", "default_prompt:"):
            if field not in yaml_text:
                errors.append(f"agents/openai.yaml missing {field.rstrip(':')}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    if "YOUR_USERNAME" in readme:
        errors.append("README still contains YOUR_USERNAME placeholder")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Skill structure looks good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
