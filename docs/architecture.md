# 아키텍처 메모

이 문서는 구조, 모듈 경계, 중요한 기술 결정을 기록하기 위한 문서입니다.
구현 변경이 설계에 영향을 주는 경우에는 같은 작업 안에서 이 문서도 함께 수정합니다.

## 1. 시스템 요약

- 프로젝트명: Agentic Full-stack Template
- 프로젝트 유형: AI 에이전트 협업용 표준 템플릿
- 핵심 목표: AI 에이전트와 인간의 협업 효율을 극대화하는 표준 구조 및 하네스 제공
- 주요 사용자: 소프트웨어 개발자 및 AI 코딩 에이전트

## 2. 현재 구조

- `backend/`
  Go (Gin) 기반의 백엔드 애플리케이션 및 API 서버
- `frontend/`
  React (Vite + TypeScript) 기반의 프런트엔드 애플리케이션
- `scripts/`
  프로젝트 관리, 초기화, 검증을 위한 자동화 스크립트 (Python/Bash/Bat)
- `docs/`
  아키텍처, 제품 명세, 기술 참고 자료 및 실행 계획

## 3. 권장 모듈 경계

실제 프로젝트가 시작되면, 필요에 따라 최소한 아래 계층을 정의합니다.

- 진입 계층 (Entry Points)
  API 엔드포인트, Swagger UI, 프런트엔드 라우트
- 도메인 계층 (Domain & Logic)
  GORM 모델, 비즈니스 유스케이스 및 서비스 로직
- 인프라 계층 (Infrastructure)
  MySQL 데이터베이스 연동, Docker Compose 구성
- 공통 계층 (Cross-cutting)
  로깅, 에러 핸들링, 환경 변수(.env) 관리

## 4. 의사결정 기록

### Decision 001: Default Technology Stack

- Status: Accepted
- Context: 범용적이고 AI 에이전트가 이해하기 쉬운 정적 타입 언어와 인기 있는 프레임워크 선택 필요
- Decision: Backend: Go/Gin/GORM, Frontend: React/Vite/TS, DB: MySQL
- Consequence: 컴파일 타임 검증과 강력한 타입 시스템으로 AI의 코드 생성 오류율을 현저히 낮춤

## 5. 데이터 및 흐름 메모

- 백엔드와 프런트엔드는 RESTful API로 통신 (Swagger로 명세 관리)
- 데이터 저장소는 MySQL 8.0 사용 (Docker 컨테이너화)
- 환경 설정은 `.env` 파일을 통해 주입받으며, `backend/.env.example` 형식을 따름

## 6. 테스트 및 검증 전략

- **Harness**: `scripts/check.py`를 통합 검증 게이트로 사용
- **Backend**: `go test`, `go vet`, `go fmt`
- **Frontend**: `npm run lint`, `npm run build`
- **API**: `swag init`을 통한 명세 최신화 검증

## 7. 변경 규칙

- 프로젝트 구조나 기술 스택 변경 시 이 문서를 최우선으로 업데이트합니다.
- 새 의존성이나 서드파티 서비스 추가 시 '의사결정 기록' 섹션에 추가합니다.
