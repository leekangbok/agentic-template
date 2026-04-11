#!/usr/bin/env sh
set -eu

ROOT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

echo "[codex-template] CONTEXT.md 갱신 중"
python "$ROOT_DIR/scripts/auto_codex_context.py"

echo "[codex-template] 준비 완료"
echo "작업 시작 전에 README.md, AI_RULES.md, CONTEXT.md, TASKS.md를 읽으세요."
