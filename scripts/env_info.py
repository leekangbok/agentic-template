#!/usr/bin/env python3
from __future__ import annotations

import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs" / "generated"
OUTPUT_FILE = OUTPUT_DIR / "ENV_INFO.md"


def optional_output(command: list[str]) -> str:
    try:
        result = subprocess.run(
            command,
            text=True,
            capture_output=True,
            check=False,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip().splitlines()[0] if result.stdout else "Installed but returned no output"
        return "Not installed or failed"
    except (subprocess.SubprocessError, FileNotFoundError):
        return "Not installed"


def get_env_info() -> dict[str, str]:
    info = {}
    info["Timestamp (UTC)"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    info["OS"] = f"{platform.system()} {platform.release()} ({platform.machine()})"
    info["Python Version"] = sys.version.split()[0]
    info["Python Executable"] = sys.executable
    info["Go Version"] = optional_output(["go", "version"])
    info["Node.js Version"] = optional_output(["node", "-v"])
    info["Git Version"] = optional_output(["git", "--version"])
    info["Docker Version"] = optional_output(["docker", "--version"])
    
    # Git User Info
    git_user = optional_output(["git", "config", "user.name"])
    git_email = optional_output(["git", "config", "user.email"])
    info["Git User"] = f"{git_user} <{git_email}>" if git_user != "Not installed" else "Not configured"

    return info


def generate_markdown(info: dict[str, str]) -> str:
    lines = [
        "# 개발 환경 정보 (Environment Snapshot)",
        "",
        "> [!NOTE]",
        "> 이 문서는 `scripts/env_info.py`에 의해 자동 생성되었습니다.",
        "> AI 에이전트가 작업을 시작하기 전에 현재 환경을 파악하는 용도로 사용합니다.",
        "",
        "| 항목 | 정보 |",
        "| :--- | :--- |"
    ]
    for key, value in info.items():
        lines.append(f"| {key} | `{value}` |")
    
    lines.append("")
    lines.append("## 가용 도구 상태")
    lines.append("")
    
    tools = {
        "Python": ["python", "--version"],
        "Go": ["go", "version"],
        "Node.js": ["node", "-v"],
        "npm": ["npm", "-v"],
        "Git": ["git", "--version"],
        "Make": ["make", "--version"],
    }
    
    lines.append("| 도구 | 상태/버전 |")
    lines.append("| :--- | :--- |")
    for name, cmd in tools.items():
        lines.append(f"| {name} | `{optional_output(cmd)}` |")

    return "\n".join(lines) + "\n"


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("환경 정보를 수집 중...")
    info = get_env_info()
    content = generate_markdown(info)
    
    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"가 생성되었습니다: {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
