#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-}"
if [ -z "$REPO_URL" ]; then
  echo "Usage: ./scripts/push_to_github.sh <github-repo-url>"
  exit 1
fi

if [ ! -d .git ]; then
  git init
fi

git add .
git commit -m "chore: initialize EDU AI Quiz & Q&A project" || true
git branch -M main

git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"
git push -u origin main
