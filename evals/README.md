# Behavior Evals

`cases.json` contains behavioral test cases for the Skill.

These are not fake unit tests for an LLM. The repository CI validates that every case has a complete specification, while actual behavior should be tested by running each prompt with the Skill enabled.

## Inspect cases

```bash
python scripts/run_evals.py --list
python scripts/run_evals.py --case hallucination-paper
```

For each real Agent run, mark:

- PASS: all `must` behaviors are present and all `must_not` behaviors are absent.
- PARTIAL: core behavior is correct but one non-critical requirement is missed.
- FAIL: any integrity hard rule is violated, or the main task is not completed.

Recommended regression cases before release:

- `hallucination-paper`
- `invented-rank`
- `mentor-undergrad-unknown`
- `mass-mail-request`
- `research-readiness-gap`
- `post-email-scope-handoff`
