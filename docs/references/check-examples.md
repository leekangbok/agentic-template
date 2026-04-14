# 스택별 검증 스크립트 예시

이 문서는 `scripts/check.py`를 다양한 기술 스택에 맞춰 커스터마이징할 때 참고할 수 있는 예시들을 제공합니다.

---

## 1. Go (Gin/GORM) - 현재 프로젝트 표준

현재 템플릿의 `scripts/check.py`에 적용된 표준 구성입니다.

```python
# Go 기반 검증 단계 예시
steps = [
    ("backend", "go-fmt", ["go", "fmt", "./..."]),
    ("backend", "go-vet", ["go", "vet", "./..."]),
    ("backend", "go-test", ["go", "test", "./..."]),
    ("backend", "go-build", ["go", "build", "-o", "main.exe", "."]),
    # API 명세 최신화 확인 (선택 사항)
    ("backend", "swag-init", ["swag", "init"]),
]
```

---

## 2. React (Vite/TS) - 현재 프로젝트 표준

프런트엔드 프로젝트 폴더(`frontend/`)에 대한 검증 구성입니다.

```python
# React 기반 검증 단계 예시
steps = [
    ("frontend", "npm-lint", ["npm", "run", "lint"]),
    ("frontend", "npm-build", ["npm", "run", "build"]),
]
```

---

## 3. Python (FastAPI/Pytest) - 기타 스택 참고용

다른 프로젝트에서 Python 스택을 사용할 경우 참고하세요.

```python
# Python 기반 검증 단계 예시
steps = [
    ("backend", "ruff", ["ruff", "check", "."]),
    ("backend", "mypy", ["mypy", "src"]),
    ("backend", "pytest", ["pytest", "tests"]),
]
```

---

## 4. 기타 도구 예시

- **Docker**: `["docker-compose", "config"]`
- **SQL Lint**: `["sqlfluff", "lint", "db/migrations"]`
- **OpenAPI Validation**: `["openapi-spec-validator", "docs/swagger.json"]`

---

## AI 에이전트 주의 사항

- 프로젝트 초기 설정(`project-intake`) 시 선택한 스택에 맞춰 `scripts/check.py`를 반드시 수동으로 검토하세요.
- 모든 검증 단계는 `scripts/check.py`를 통해 통합 관리되는 것을 권장합니다.
