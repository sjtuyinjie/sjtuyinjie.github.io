#!/usr/bin/env bash
# Unlock GitHub "Quickdraw" achievement: close an issue within 5 minutes of opening.
# Must run while logged in as yourself (not a bot token).
set -euo pipefail

REPO="sjtuyinjie/sjtuyinjie.github.io"
GH_BIN="${GH_BIN:-gh}"

if ! command -v "$GH_BIN" >/dev/null 2>&1; then
  echo "GitHub CLI (gh) not found."
  echo "Install: https://cli.github.com/  or: snap install gh"
  exit 1
fi

if ! "$GH_BIN" auth status >/dev/null 2>&1; then
  echo "Not logged in. Run first:"
  echo "  gh auth login"
  exit 1
fi

echo "Creating issue on $REPO ..."
START=$(date +%s)
ISSUE_URL=$("$GH_BIN" issue create \
  --repo "$REPO" \
  --title "chore: quickdraw achievement (auto-close)" \
  --body "Temporary issue for GitHub Quickdraw achievement. This will be closed within 5 minutes.")

ISSUE_NUM=$(echo "$ISSUE_URL" | grep -oE '[0-9]+$')
echo "Opened issue #${ISSUE_NUM}: ${ISSUE_URL}"
echo "Waiting 3 seconds ..."
sleep 3

"$GH_BIN" issue close "$ISSUE_NUM" \
  --repo "$REPO" \
  --comment "Closed within 5 minutes for Quickdraw achievement."

END=$(date +%s)
ELAPSED=$((END - START))
echo "Closed issue #${ISSUE_NUM} in ${ELAPSED}s."
echo "Quickdraw should appear on your profile within a few hours."
echo "Check: https://github.com/sjtuyinjie"
