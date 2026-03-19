# Multi-Agent Development Automation System

> Claude Code 기반 9개 전문 에이전트 오케스트레이션 — 브리프 하나로 기획서·코드·인프라·보안보고서 자동 산출

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Claude](https://img.shields.io/badge/Claude-claude--sonnet--4--20250514-purple)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 개요

프로젝트 브리프(자연어 설명) 하나를 입력하면, PM 에이전트가 8개 전문 에이전트를 오케스트레이션하여 실제 개발에 즉시 사용 가능한 산출물을 자동 생성합니다.

```
[브리프 입력]
    │
    ▼
[PM 에이전트] ── 브리프 분석, 역할 배분
    │
    ▼
[기획자 에이전트] ── 기능명세서 F-코드 + WBS 작성
    │
    ├── [디자이너] ── UI/디자인 시스템 + 와이어프레임
    ├── [UX 전문가] ── 사용자 여정 + 개선 제안
    ├── [프론트엔드] ── React/TypeScript 컴포넌트 코드
    ├── [백엔드] ── FastAPI + Claude API 연동 코드
    ├── [AWS SA] ── 서버리스 아키텍처 + CDK IaC
    └── [보안담당자] ── STRIDE 위협모델 + 취약점 리포트
    │
    ▼
[QA/기술검토 에이전트] ── 정합성 검증 + 테스트 케이스
    │
    ▼
[PM 최종 통합] ── Executive Summary + 액션 아이템
```

## 빠른 시작

```bash
git clone https://github.com/nambbong/multi-agent-system
cd multi-agent-system

pip install -r requirements.txt

cp .env.example .env
# .env에 ANTHROPIC_API_KEY 입력

# 브리프 직접 입력
python orchestrator.py --brief "사내 보고서 자동화 시스템 구축"

# 파일로 입력
python orchestrator.py --brief-file brief.txt --output ./outputs
```

## 산출물 예시

브리프: *"사내 AI 자동화 보고서 시스템 — 매일 오전 7시 매출/재고/고객 데이터를 Claude API로 분석, 경영진 Slack 브리핑"*

| 파일 | 내용 |
|------|------|
| `01_pm_analysis.md` | 요구사항 분석, 기술 스택 확정, 에이전트별 작업 지시 |
| `02_plan_wbs.md` | 기능 F-01~06 명세, 8주 개발 로드맵 |
| `03_design_spec.md` | 디자인 토큰, 컴포넌트 명세, ASCII 와이어프레임 |
| `04_ux_report.md` | 페르소나 2개, As-Is/To-Be 여정, KPI |
| `05_frontend_code.md` | React/TS 컴포넌트 코드, hooks, package.json |
| `06_backend_code.md` | FastAPI 코드, Claude API 프롬프트, scheduler |
| `07_aws_architecture.md` | 아키텍처 다이어그램, CDK 코드, 월 비용 시나리오 |
| `08_security_report.md` | STRIDE 위협모델, 취약점 테이블, 보안 체크리스트 |
| `09_qa_report.md` | 정합성 검증, 테스트 케이스 10개, 배포 준비도 |
| `10_FINAL_REPORT.md` | Executive Summary, 액션 아이템, 리스크 대응 |

## 에이전트 구성

| 에이전트 | 역할 | 주요 출력 |
|----------|------|-----------|
| PM (Orchestrator) | 브리프 분석, 역할 배분, 최종 통합 | 분석 보고서, 통합 보고서 |
| 기획자 | 기능명세서, WBS, API 명세 개요 | F-코드 + 로드맵 |
| 디자이너 | UI 시스템, 컴포넌트 명세, 와이어프레임 | 디자인 토큰 + ASCII 레이아웃 |
| UX 전문가 | 페르소나, 사용자 여정, KPI 정의 | As-Is/To-Be 분석 |
| 프론트엔드 | React/TS 컴포넌트 코드 | 실행 가능한 소스코드 |
| 백엔드 | FastAPI + Claude API 연동 코드 | API 서버 + 스케줄러 |
| AWS SA | 서버리스 아키텍처 + CDK IaC | 인프라 코드 + 비용 산정 |
| 보안담당자 | STRIDE 위협모델, 취약점 분석 | 보안 리포트 + 체크리스트 |
| QA/기술검토 | 정합성 검증, 통합 테스트 | 품질 보고서 + 배포 준비도 |

## 프로젝트 구조

```
multi-agent-system/
├── orchestrator.py          # 메인 실행 파일 (PM 오케스트레이터)
├── demo_run.py              # API 없이 산출물 구조 확인용 데모
├── agents/
│   ├── __init__.py
│   ├── pm_agent.py          # PM 에이전트
│   ├── planner_agent.py     # 기획자 에이전트
│   ├── designer_agent.py    # 디자이너 에이전트
│   ├── ux_agent.py          # UX 전문가 에이전트
│   ├── frontend_agent.py    # 프론트엔드 에이전트
│   ├── backend_agent.py     # 백엔드 에이전트
│   ├── aws_sa_agent.py      # AWS SA 에이전트
│   ├── security_agent.py    # 보안담당자 에이전트
│   └── qa_agent.py          # QA/기술검토 에이전트
├── outputs/                 # 세션별 산출물 저장
├── requirements.txt
├── .env.example
└── README.md
```

## 적용 사례

이 시스템은 실제 블루엠텍 사내 AI 자동화 보고서 시스템 기획 과정에서 개발되었습니다.

- **브리프 입력**: "매출/재고/고객 데이터 Claude AI 분석 → 경영진 Slack 자동 브리핑"
- **자동 생성된 산출물**: 기능명세 6개, 8주 WBS, React 컴포넌트 코드, FastAPI 서버, AWS CDK IaC, 보안 리포트
- **효과**: 기획~설계 착수 소요 시간 단축 (기존 2주 → 1일 내 초안 완성)

## 확장 가능성

- `agents/` 디렉토리에 새 에이전트 추가 가능 (데이터 엔지니어, ML 엔지니어 등)
- `orchestrator.py`의 파이프라인에 새 단계 삽입
- 출력 형식 변경 가능 (마크다운 → JSON / HTML / DOCX)
- GitHub Actions 연동으로 PR 생성 시 자동 실행

## 기술 스택

- **AI**: Anthropic Claude claude-sonnet-4-20250514
- **언어**: Python 3.11
- **의존성**: `anthropic>=0.40.0`, `python-dotenv>=1.0.0`

## 라이선스

MIT License — 자유롭게 사용, 수정, 배포 가능합니다.

---
---

## 실제 실행 결과 — 라이브 데모

### 실행 환경
- 브리프: "블루팜코리아 VectorDB 기반 의약품 추천 시스템 고도화"
- 총 소요 시간: **317.9초**
- 생성 파일: **11개**
- 사용 모델: Claude claude-sonnet-4-20250514

### 실행 화면

![에이전트 실행 화면1](스크린샷_2026-03-19_114418.png)
![에이전트 실행 화면2](스크린샷_2026-03-19_114432.png)
![산출물 목록](스크린샷_2026-03-19_114549.png)

### 실제 산출물 — 10_FINAL_REPORT.md (Claude 작성)

> PM 에이전트가 8개 전문 에이전트 결과를 통합하여 자동 생성한 경영진 보고서입니다.

---

#### Executive Summary

프로젝트는 **전체 완성도 83.3%** 로 상업적 출시 가능 수준에 도달했습니다.
AWS 인프라(88점)와 보안 아키텍처(92점)는 엔터프라이즈급 완성도를 보이며,
**6주 내 정식 출시** 가능하나 개발팀 3주 추가 투입이 필요합니다.

#### 프로젝트 완성도 평가

| 영역 | 완성도 | 상태 |
|------|--------|------|
| 기획/WBS | 85% | ✅ 완료 |
| UI/UX 디자인 | 82% | ✅ 완료 |
| 프론트엔드 | 78% | ⚠️ 보완 |
| 백엔드 | 75% | ⚠️ 보완 |
| AWS 인프라 | 88% | ✅ 완료 |
| 보안 | 92% | ✅ 완료 |

#### 핵심 리스크 및 대응

| 위험도 | 리스크 | 대응 방안 |
|--------|--------|-----------|
| HIGH | 의료정보 보안 (PIPA 위반 시 과징금 3%) | ISMS-P 인증, 정기 보안 감사 |
| HIGH | 추천 정확도 미달 (목표 85% vs 현재 78%) | A/B 테스트, 약사 피드백 반영 |
| MEDIUM | 대량 트래픽 시 안정성 | Auto Scaling, 장애 대응 매뉴얼 |

#### Next Action Items

| 항목 | 담당 | 기한 | 예산 |
|------|------|------|------|
| 프론트엔드 타입 정의 보완 | 개발팀 | D+5 | - |
| 백엔드 에러 핸들링 강화 | 개발팀 | D+3 | - |
| 파일럿 약국 10곳 선정 | 사업팀 | D+7 | - |
| 추가 개발 인력 2명 투입 | 경영진 승인 | D+1 | ₩2,700만 |
| ISMS-P 인증 추진 | 경영진 승인 | D+1 | ₩1,000만 |

---

> 위 보고서는 사람이 작성한 것이 아닙니다.  
> 브리프 입력 후 **317.9초** 만에 PM 에이전트가 8개 전문 에이전트 결과를 통합하여 자동 생성했습니다.
```

---
<img width="595" height="417" alt="스크린샷 2026-03-19 114418" src="https://github.com/user-attachments/assets/14e219eb-5867-4bfb-854f-5dba8e28aef8" />
<img width="626" height="257" alt="스크린샷 2026-03-19 114432" src="https://github.com/user-attachments/assets/85f05c90-039c-44d5-9689-90008575b5f2" />
<img width="759" height="309" alt="스크린샷 2026-03-19 114549" src="https://github.com/user-attachments/assets/78b99603-3c53-4db5-abbb-d0b6d59d3c21" />


*Made with Claude Code · nambbong/multi-agent-system*
