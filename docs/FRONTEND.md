# 프런트엔드 상세 가이드

이 문서는 프로젝트의 프런트엔드 아키텍처, 기술 스택 및 개발 원칙을 기록합니다.

## 1. 기술 스택 (Technology Stack)

- **Core**: React 19
- **Build Tool**: Vite 8
- **Language**: TypeScript
- **State Management**: React Hooks (useState, useEffect) - 필요시 전역 상태 라이브러리 추가 가능
- **Styling**: Vanilla CSS (Premium Dark Theme 적용)
- **API Client**: Axios

## 2. 프로젝트 구조 (Directory Structure)

`frontend/` 디렉터리는 다음과 같은 구조를 가집니다.

- `src/App.tsx`: 메인 대시보드 UI 및 API 연동 샘플
- `src/App.css`: 다크 모드 기반의 프리미엄 디자인 시스템
- `public/`: 정적 애셋
- `package.json`: 빌드 및 린트 스크립트 정의

## 3. 개발 및 검증 명령

- **개발 대기**: `npm run dev`
- **빌드 및 타입 체크**: `npm run build`
- **린트**: `npm run lint`
- **통합 검증**: `npm run check` (Lint + Build)

## 4. 디자인 시스템 가이드

- **색상**:深색 배경과 조화로운 그라데이션 사용
- **타이포그래피**: 현대적인 산세리프 글꼴 프로젝트 기본값 사용
- **컴포넌트**: 재사용 가능한 함수형 컴포넌트 지향

## 5. AI 에이전트 협업 규칙

- 새 컴포넌트 추가 시 `frontend/src/components/` 폴더를 생성하여 관리하세요.
- 스타일 수정 시 `App.css`에 직접 정의하거나 컴포넌트별 CSS 모듈을 사용하세요.
- API 연동 시 백엔드의 Swagger 명세를 먼저 확인하고 인터페이스를 정의하세요.
