# undergrad-taoci-skill

An Agent Skill for **undergraduate research outreach emails**.

Its primary job is not to mass-produce generic emails. It maps a student's real undergraduate experience to a professor's recent research and turns that connection into a concise, truthful, professor-specific outreach email.

## Install: 30-second quick start

### Method 1: `$skill-installer` (recommended)

In Codex, run:

```text
$skill-installer
```

Then ask it to install:

```text
Install the skill from:
https://github.com/agcenn/undergrad-taoci-skill
```

If the skill does not appear immediately, reopen Codex. Then use:

```text
$undergrad-taoci Help me draft an undergraduate research outreach email from my CV and the target professor's page.
```

### Method 2: Git clone

macOS / Linux:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/agcenn/undergrad-taoci-skill.git ~/.agents/skills/undergrad-taoci
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
git clone https://github.com/agcenn/undergrad-taoci-skill.git "$HOME\.agents\skills\undergrad-taoci"
```

### Method 3: Manual copy after downloading ZIP

macOS / Linux:

```bash
mkdir -p ~/.agents/skills
cp -R undergrad-taoci-skill ~/.agents/skills/undergrad-taoci
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse undergrad-taoci-skill "$HOME\.agents\skills\undergrad-taoci"
```

To verify the installation, run `/skills` in Codex or type `$` and confirm that `undergrad-taoci` appears.

Project-level installation is also supported:

```bash
mkdir -p .agents/skills
git clone https://github.com/agcenn/undergrad-taoci-skill.git .agents/skills/undergrad-taoci
```

## Core workflow

```text
Student background
→ mentor research verification
→ fit / research-readiness map
→ outreach angle
→ email draft
→ quality review
→ send-ready version
```

Optional mentor search, follow-up, and reply handling exist only to support this core workflow. Research onboarding is not launched before the outreach task is complete.

## What v0.2.0 adds

- focused scope around undergraduate outreach writing
- progressive-disclosure references instead of one oversized `SKILL.md`
- five modes: Mentor Search, Mentor Analysis, Outreach Draft, Outreach Review, Follow-up / Reply
- Research Readiness Gap analysis
- `agents/openai.yaml`
- behavior eval cases
- privacy and repository validation scripts
- GitHub Actions CI
- optional outreach ledger

## Example

```text
Use $undergrad-taoci.
I am a computer science undergraduate. Here are my CV and the target professor's page.
Find the strongest truthful connection between my background and the professor's recent work,
then draft a concise outreach email. Do not exaggerate my experience.
```

## Principles

- Never fabricate GPA, rank, publications, project results, internships, or recruiting status.
- A professor-specific research anchor is required.
- Course projects, GitHub work, competitions, engineering experience, and learning ability are valid undergraduate evidence.
- The assistant reading a paper does not mean the student has read it.
- Research-readiness analysis supports email positioning; it is not a default long-term research roadmap.

## Testing

```bash
python scripts/run_checks.py
python scripts/run_evals.py --list
```

Behavior cases live in `evals/cases.json`. CI validates the repository and eval specification; actual LLM behavior should be tested by running the prompts with the installed skill.

## Inspiration

- [Kisechan/taoci-skill](https://github.com/Kisechan/taoci-skill)
- [syiibfs-hash/baoyan-skills](https://github.com/syiibfs-hash/baoyan-skills)

The undergraduate workflow, references, rules, and evals in this repository are independently written.

## License

MIT.
