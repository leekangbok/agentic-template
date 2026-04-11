#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
TASKS = ROOT / "TASKS.md"
ARCH = ROOT / "docs" / "architecture.md"
CONTEXT = ROOT / "CONTEXT.md"
SRC = ROOT / "src"
TESTS = ROOT / "tests"
START_MARKER = "<!-- AUTO-GENERATED-START -->"
END_MARKER = "<!-- AUTO-GENERATED-END -->"


def count_entries(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob("*") if item.is_file())


def summarize_tasks() -> tuple[int, int]:
    if not TASKS.exists():
        return (0, 0)

    total = 0
    done = 0
    for line in TASKS.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ]") or stripped.startswith("- [x]") or stripped.startswith("- [X]"):
            total += 1
            if stripped.startswith("- [x]") or stripped.startswith("- [X]"):
                done += 1
    return done, total


def build_auto_block() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    done_tasks, total_tasks = summarize_tasks()
    src_files = count_entries(SRC)
    test_files = count_entries(TESTS)

    return f"""{START_MARKER}
이 블록은 `python scripts/auto_codex_context.py` 실행 시 갱신됩니다.

- 마지막 갱신 시각: {timestamp}
- `README.md` 존재 여부: {"yes" if README.exists() else "no"}
- `docs/architecture.md` 존재 여부: {"yes" if ARCH.exists() else "no"}
- `src/` 파일 수: {src_files}
- `tests/` 파일 수: {test_files}
- 완료된 작업 수: {done_tasks}/{total_tasks}
{END_MARKER}"""


def default_context() -> str:
    auto_block = build_auto_block()
    return f"""# 프로젝트 문맥

이 문서는 다음 세션이 2분 안에 현재 프로젝트 상태를 이해할 수 있도록 유지하는 문서입니다.

## 프로젝트 요약

- 프로젝트 유형: Codex CLI 개발 템플릿
- 현재 단계: 초기 템플릿 구성 완료
- 목표: Codex 기반 새 프로젝트를 시작할 때 재사용 가능한 기준 구조 제공
- 상태: 문서와 헬퍼 스크립트는 준비되었지만 실제 제품 코드는 아직 없음

## 현재 존재하는 것

- 핵심 문서: `README.md`, `AI_RULES.md`, `CONTEXT.md`, `TASKS.md`
- 세션 시작 프롬프트: `.codex-start.txt`
- 아키텍처 문서: `docs/architecture.md`
- 컨텍스트 갱신 스크립트: `scripts/auto_codex_context.py`
- 실행 헬퍼 스크립트: `scripts/run.sh`, `scripts/run.bat`
- 플레이스홀더 코드 및 테스트 디렉터리: `src/`, `tests/`

## 아직 비어 있는 정보

- 실제 프로젝트명
- 제품 목표
- 대상 사용자
- 기술 스택
- 표준 실행 및 테스트 명령
- MVP 범위

## 현재 리스크

- 실제 프로젝트 메타데이터가 아직 채워지지 않았음
- `src/`, `tests/`는 아직 플레이스홀더 상태임
- 표준 명령이 아직 확정되지 않았음

## 다음 권장 작업

1. `README.md`에 실제 프로젝트 정보를 채웁니다.
2. 기본 아키텍처 메모를 실제 스택과 경계로 교체합니다.
3. `TASKS.md`의 예시 작업을 실제 우선순위로 교체합니다.
4. 첫 구현 파일과 첫 테스트 파일을 추가합니다.

## 자동 생성 상태

{auto_block}

## 세션 메모

- 위 요약은 가능한 한 빨리 실제 프로젝트 정보로 교체합니다.
- 구조나 상태가 바뀌면 자동 생성 블록을 다시 갱신합니다.
"""


def update_existing_context(text: str) -> str:
    auto_block = build_auto_block()
    if START_MARKER in text and END_MARKER in text:
        start = text.index(START_MARKER)
        end = text.index(END_MARKER) + len(END_MARKER)
        return text[:start] + auto_block + text[end:]
    return default_context()


def main() -> None:
    if CONTEXT.exists():
        current = CONTEXT.read_text(encoding="utf-8")
        updated = update_existing_context(current)
    else:
        updated = default_context()

    CONTEXT.write_text(updated, encoding="utf-8")
    print(f"Updated {CONTEXT}")


if __name__ == "__main__":
    main()
