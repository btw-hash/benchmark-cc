#!/usr/bin/env bash
# PreToolUse hook: blocks Edit/Write if content contains a known secret pattern.
INPUT=$(cat)
CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // .tool_input.new_string // ""')
[ -z "$CONTENT" ] && exit 0
PATTERNS='sk-ant-[A-Za-z0-9_-]{20,}|sk-proj-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|-----BEGIN[A-Z ]*PRIVATE KEY-----'
MATCH=$(echo "$CONTENT" | grep -oE "$PATTERNS" | head -1)
if [ -n "$MATCH" ]; then
  echo "BLOCKED: secret-like pattern detected" >&2
  exit 2
fi
exit 0
