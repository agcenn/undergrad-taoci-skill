# Contributing

Contributions should preserve the project's scope: **undergraduate research outreach quality first**.

## Before opening a PR

Run:

```bash
python scripts/run_checks.py
```

If you change behavior in `SKILL.md` or `references/`, add or update a regression case in `evals/cases.json`.

## Good changes

- better mentor-research verification
- better undergraduate-specific email positioning
- stronger anti-hallucination / anti-mass-mail rules
- clearer Chinese or English outreach style
- better behavior evals
- compatibility improvements for Agent Skills hosts

## Avoid

- turning the core Skill into a general life/career/research planner
- adding fake acceptance/reply probabilities
- rules that encourage fabricated achievements or paper-reading claims
- unnecessary scripts when instructions are sufficient

## Privacy

Do not commit real CVs, private emails, phone numbers, student IDs, API keys, or other personal data to examples or eval fixtures.
