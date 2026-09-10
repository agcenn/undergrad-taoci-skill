#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/agcenn/undergrad-taoci-skill.git"
DEST="${1:-$HOME/.agents/skills/undergrad-taoci}"

mkdir -p "$(dirname "$DEST")"

if [ -e "$DEST" ]; then
  echo "Destination already exists: $DEST" >&2
  echo "Remove it or pass another destination path." >&2
  exit 1
fi

git clone "$REPO_URL" "$DEST"
echo "Installed undergrad-taoci to: $DEST"
echo "Restart/reopen Codex if the skill does not appear immediately."
