#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_step(name: str, command: list[str]) -> bool:
    print(f"[check] {name}: {' '.join(command)}")
    try:
        subprocess.run(command, cwd=ROOT, check=True)
    except FileNotFoundError:
        print(f"[check] skipped: command not found for '{name}'")
        return False
    except subprocess.CalledProcessError as exc:
        print(f"[check] failed: {name} (exit code {exc.returncode})")
        raise
    else:
        print(f"[check] passed: {name}")
        return True


def main() -> int:
    print("표준 검증 하네스를 시작합니다.")
    print("현재 프로젝트 모드: Full Stack (Go + React)")
    
    # (이동 경로, 명칭, 명령어)
    steps: list[tuple[str, str, list[str]]] = [
        # Backend (Go)
        ("backend", "go-fmt", ["go", "fmt", "./..."]),
        ("backend", "go-vet", ["go", "vet", "./..."]),
        ("backend", "go-test", ["go", "test", "./..."]),
        ("backend", "go-build", ["go", "build", "-o", "main.exe", "."]),
        
        # Frontend (React)
        ("frontend", "npm-lint", ["npm", "run", "lint"]),
        ("frontend", "npm-build", ["npm", "run", "build"]),
    ]

    any_executed = False
    for folder, name, command in steps:
        target_dir = ROOT / folder
        if not target_dir.exists():
            continue
            
        executable = shutil.which(command[0])
        if executable:
            any_executed = True
            print(f"[check] {name}: {' '.join(command)} (in {folder})")
            try:
                # Use absolute path for executable to be safer
                command[0] = executable
                subprocess.run(command, cwd=target_dir, check=True)
            except subprocess.CalledProcessError as exc:
                print(f"[check] failed: {name} (exit code {exc.returncode})")
                raise
            else:
                print(f"[check] passed: {name}")

    if not any_executed:
        print("[check] warning: no executable commands were found in the current environment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
