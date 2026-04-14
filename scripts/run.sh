#!/usr/bin/env sh
set -eu

ROOT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

echo "[agentic-template] CONTEXT.md 갱신 중"
python "$ROOT_DIR/scripts/auto_context.py"

echo "[agentic-template] 준비 완료"
echo "작업 시작 전에 README.md, AI_RULES.md, CONTEXT.md, TASKS.md를 읽으세요."
