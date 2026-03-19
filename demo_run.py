"""
Multi-Agent System — 데모 실행기
실제 API 없이 각 에이전트 산출물 샘플을 출력합니다
"""

import time
import os
from pathlib import Path
from datetime import datetime

SESSION = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(f"outputs/{SESSION}")
OUT.mkdir(parents=True, exist_ok=True)

BRIEF = """사내 AI 자동화 보고서 시스템 구축 — 매일 오전 7시, 전날의 매출·재고·고객 데이터를
Claude API로 분석하여 경영진에게 Slack 자동 브리핑. 웹 대시보드(React) +
REST API(Python FastAPI) + AWS 서버리스 아키텍처. 사용자: 경영진 5명, 월 처리량 50만 건."""

OUTPUTS = {
"01_pm_analysis.md": """# PM 에이전트 — 브리프 분석 및 역할 배분

## 핵심 요구사항 분석

| 구분 | 내용 |
|------|------|
| 기능 | 데이터 자동 수집 → Claude AI 분석 → Slack 전송 → 웹 대시보드 |
| 비기능 | 가용성 99.9% / 응답시간 3초 이내 / 동시 사용자 20명 |
| 보안 | API Key 암호화 / RBAC 접근제어 / 감사 로그 |
| 운영 | 서버리스 우선 / 월 $200 이하 / 무중단 배포 |

## 기술 스택 확정

- **AI**: Claude claude-sonnet-4-20250514 (Anthropic)
- **Backend**: Python 3.11 + FastAPI + APScheduler
- **Frontend**: React 18 + TypeScript + Recharts
- **DB**: AWS Aurora Serverless v2 (MySQL)
- **인프라**: AWS Lambda + EventBridge + S3 + CloudFront
- **알림**: Slack Webhook API
- **IaC**: AWS CDK (Python)

## 각 에이전트 작업 지시

### 기획자
- 기능 F-01~F-06 상세 명세 및 8주 WBS 작성
- 데이터 흐름도 및 API 명세 개요

### 디자이너
- 다크 테마 경영진 대시보드 UI 시스템
- KPI 카드 + 트렌드 차트 + 이상치 하이라이트 컴포넌트

### UX 전문가
- 경영진 페르소나 분석 (모바일 우선)
- 기존 보고서 수작업 Pain Point 해소 방안

### 프론트엔드
- React/TypeScript 컴포넌트 구현 (Dashboard, KpiCard, TrendChart)
- Vercel 배포 설정

### 백엔드
- FastAPI 엔드포인트 7개 구현
- Claude API 프롬프트 엔지니어링 모듈

### AWS SA
- 서버리스 아키텍처 설계 및 CDK 코드
- 월 예상 비용 3개 시나리오

### 보안담당자
- STRIDE 위협 모델링
- Secrets Manager + TLS 1.3 + IAM 최소권한

## 예상 리스크 TOP 3

1. **Claude API Latency**: 분석 시간 5~15초 → 비동기 처리 + 캐시로 해결
2. **데이터 정합성**: 소스 DB 스키마 변경 시 파이프라인 중단 → 스키마 버전 관리
3. **Slack 메시지 길이 제한**: 4000자 초과 시 분할 전송 로직 필요

## 성공 기준(KPI)
- 보고서 생성 시간: 수작업 3시간 → 자동 0분 (100% 절감)
- 오전 7시 브리핑 성공률: 99% 이상
- 경영진 만족도: 80점 이상 (분기 설문)
""",

"02_plan_wbs.md": """# 기획자 에이전트 — 기능명세서 & WBS

## 기능 목록

| 코드 | 기능명 | 설명 | 우선순위 | SP |
|------|--------|------|----------|-----|
| F-01 | 데이터 수집 파이프라인 | 매출/재고/고객 DB 연동 자동 수집 | P0 | 8 |
| F-02 | Claude AI 분석 모듈 | 4파트 구조화 프롬프트 분석 | P0 | 13 |
| F-03 | Slack 자동 브리핑 | 오전 7시 경영진 채널 자동 전송 | P0 | 5 |
| F-04 | 웹 대시보드 | React KPI 대시보드 (실시간) | P1 | 13 |
| F-05 | 이상치 알림 | 임계값 초과 시 즉시 Push 알림 | P1 | 8 |
| F-06 | 히스토리 조회 | 과거 브리핑 검색 및 비교 | P2 | 5 |

## 비기능 요구사항

| 항목 | 요건 | 측정 방법 |
|------|------|-----------|
| 가용성 | 99.9% (월 43분 이하 장애) | CloudWatch |
| 응답시간 | 대시보드 3초 이내 | Lighthouse |
| 분석 시간 | Claude 응답 15초 이내 | Lambda duration |
| 보안 | API Key 환경변수 분리, HTTPS 필수 | Security Hub |

## WBS — 8주 개발 로드맵

| 주차 | 개발팀 | 인프라팀 | 산출물 |
|------|--------|----------|--------|
| 1주 | 요구사항 확정, DB 스키마 설계 | AWS 계정 셋업, VPC 구성 | ERD, 아키텍처 다이어그램 |
| 2주 | 데이터 수집 모듈 (F-01) | Lambda + EventBridge 구성 | 수집 파이프라인 PoC |
| 3주 | Claude API 연동 (F-02) | Aurora Serverless 구성 | AI 분석 모듈 |
| 4주 | Slack 연동 (F-03) | S3 + CloudFront CDN | Slack 브리핑 자동화 |
| 5주 | React 대시보드 (F-04) | CloudWatch 모니터링 | 웹 대시보드 Beta |
| 6주 | 이상치 알림 (F-05) | 보안 강화 (GuardDuty) | 알림 시스템 |
| 7주 | 히스토리 기능 (F-06) | 부하 테스트 | 전체 기능 통합 |
| 8주 | QA / 버그픽스 | DR 테스트 | Production 배포 |

## 외부 연동 목록

| 시스템 | 연동 방식 | 담당 |
|--------|-----------|------|
| 매출 DB | MySQL Read Replica 직접 쿼리 | BE팀 |
| Claude API | Anthropic Python SDK | BE팀 |
| Slack | Incoming Webhook | BE팀 |
| 이메일 | AWS SES | BE팀 |
""",

"03_design_spec.md": """# 디자이너 에이전트 — UI 디자인 시스템

## 디자인 토큰

```css
/* 색상 팔레트 — 다크 프리미엄 테마 */
--color-bg-primary: #0D1117;
--color-bg-secondary: #161B22;
--color-bg-card: #21262D;
--color-accent-blue: #2E75B6;
--color-accent-green: #3FB950;
--color-accent-amber: #F0883E;
--color-accent-red: #F85149;
--color-text-primary: #E6EDF3;
--color-text-secondary: #8B949E;

/* 타이포그래피 */
--font-sans: 'Pretendard', -apple-system, sans-serif;
--font-mono: 'JetBrains Mono', monospace;  /* 숫자 데이터용 */
--text-display: 28px / 500;
--text-heading: 20px / 600;
--text-body: 14px / 400;
--text-caption: 12px / 400;
```

## 핵심 컴포넌트 목록

| 컴포넌트 | 용도 | 상태 |
|----------|------|------|
| KpiCard | 핵심 지표 표시 | default / up / down / alert |
| TrendChart | 7일 추이 라인차트 | loading / data / empty |
| AnomalyBadge | 이상치 하이라이트 | warning / critical |
| SlackPreview | 브리핑 미리보기 | sent / pending / error |
| DateRangePicker | 기간 선택 | — |

## 핵심 화면 — 메인 대시보드 (ASCII 와이어프레임)

```
┌─────────────────────────────────────────────────────────┐
│  AI 경영 브리핑 대시보드        [오늘 2026-03-19 07:02] │
├──────────┬──────────┬──────────┬──────────────────────── │
│ 일 매출  │  재고율  │ 신규고객 │  이상치 알림           │
│ ₩4.2억  │  87.3%  │  142명  │  ⚠ 재고 임박 3건       │
│ ▲ +12%  │ ▼ -3%   │ ▲ +8%   │  → 상세보기           │
├──────────┴──────────┴──────────┴──────────────────────── │
│  7일 매출 추이                      카테고리별 비중      │
│  ████████████████████               ■ 의약품  62%       │
│  ▁▃▅▇█▇█                           ■ 소비재  28%       │
│  M  T  W  T  F  S  S               ■ 기타    10%       │
├──────────────────────────────────────────────────────── │
│  오늘의 AI 브리핑 요약 (Claude 분석)                    │
│  "전일 대비 매출 12% 증가. 위고비 품목 급등 주요 원인.  │
│   재고 3종 임박, 발주 권고..."   [전문보기] [Slack재전송]│
└─────────────────────────────────────────────────────────┘
```

## 모바일 반응형 전략
- 768px 이하: 2열 그리드 → 1열 스택
- KPI 카드: 스와이프 캐러셀로 전환
- 차트: 터치 줌 지원 (Recharts responsive)

## 접근성 체크리스트
- [x] 색상 대비 4.5:1 이상 (WCAG AA)
- [x] 포커스 링 명확히 표시
- [x] 스크린리더 aria-label 모든 차트에 적용
- [x] 키보드 탐색 가능
""",

"05_frontend_code.md": """# 프론트엔드 에이전트 — React/TypeScript 코드

## 프로젝트 구조

```
src/
├── components/
│   ├── KpiCard.tsx          # 핵심 지표 카드
│   ├── TrendChart.tsx       # 트렌드 라인 차트
│   ├── AnomalyAlert.tsx     # 이상치 알림
│   └── SlackPreview.tsx     # 브리핑 미리보기
├── pages/
│   ├── Dashboard.tsx        # 메인 대시보드
│   └── History.tsx          # 브리핑 히스토리
├── hooks/
│   ├── useReportData.ts     # 보고서 데이터 fetch
│   └── useAnomalies.ts      # 이상치 감지
├── api/
│   └── client.ts            # Axios 인스턴스
└── types/
    └── report.ts            # TypeScript 타입 정의
```

## KpiCard 컴포넌트

```tsx
// components/KpiCard.tsx
interface KpiCardProps {
  title: string;
  value: string;
  change: number;      // 전일 대비 %
  status: 'up' | 'down' | 'alert' | 'neutral';
}

export const KpiCard = ({ title, value, change, status }: KpiCardProps) => {
  const statusColor = {
    up: 'var(--color-accent-green)',
    down: 'var(--color-accent-red)',
    alert: 'var(--color-accent-amber)',
    neutral: 'var(--color-text-secondary)',
  }[status];

  return (
    <div className="kpi-card" style={{ borderLeft: `3px solid ${statusColor}` }}>
      <p className="kpi-title">{title}</p>
      <p className="kpi-value">{value}</p>
      <p className="kpi-change" style={{ color: statusColor }}>
        {change > 0 ? '▲' : '▼'} {Math.abs(change).toFixed(1)}%
      </p>
    </div>
  );
};
```

## useReportData 훅

```ts
// hooks/useReportData.ts
import { useQuery } from '@tanstack/react-query';
import { apiClient } from '../api/client';

export const useReportData = (date?: string) => {
  return useQuery({
    queryKey: ['report', date ?? 'latest'],
    queryFn: () => apiClient.get(`/api/reports/${date ?? 'latest'}`).then(r => r.data),
    staleTime: 1000 * 60 * 5,  // 5분 캐시
    refetchInterval: 1000 * 60 * 10,  // 10분마다 자동 갱신
  });
};
```

## package.json 주요 의존성

```json
{
  "dependencies": {
    "react": "^18.3.0",
    "typescript": "^5.4.0",
    "@tanstack/react-query": "^5.0.0",
    "recharts": "^2.12.0",
    "axios": "^1.7.0",
    "react-router-dom": "^6.23.0"
  }
}
```
""",

"06_backend_code.md": """# 백엔드 에이전트 — FastAPI + Claude API 코드

## FastAPI 메인 앱

```python
# app/main.py
from fastapi import FastAPI
from app.api import reports, slack, health
from app.scheduler import start_scheduler

app = FastAPI(title="AI Report API", version="1.0.0")
app.include_router(reports.router, prefix="/api/reports")
app.include_router(slack.router, prefix="/api/slack")
app.include_router(health.router, prefix="/health")

@app.on_event("startup")
async def startup():
    start_scheduler()  # 오전 7시 cron 시작
```

## Claude API 분석 모듈 — 핵심

```python
# app/services/claude_analyzer.py
import anthropic
from app.models import DailyData

client = anthropic.Anthropic()

ANALYSIS_PROMPT = \"\"\"
당신은 기업 경영 데이터 분석 전문가입니다.
아래 전일 데이터를 분석하여 4파트 보고서를 작성하세요.

[데이터]
{data_json}

[출력 형식]
## PART 1: 핵심 이상치 감지
## PART 2: 크로스 도메인 연관 분석  
## PART 3: 경영진 액션 아이템 (우선순위 3개)
## PART 4: 리스크 & 기회
\"\"\"

async def analyze_daily_data(data: DailyData) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": ANALYSIS_PROMPT.format(data_json=data.to_json())
        }]
    )
    return message.content[0].text
```

## 스케줄러 — 매일 오전 7시 실행

```python
# app/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.claude_analyzer import analyze_daily_data
from app.services.slack_sender import send_briefing
from app.services.data_collector import collect_yesterday

scheduler = AsyncIOScheduler(timezone="Asia/Seoul")

@scheduler.scheduled_job("cron", hour=7, minute=0)
async def daily_briefing():
    data = await collect_yesterday()      # 1. 데이터 수집
    analysis = await analyze_daily_data(data)  # 2. Claude 분석
    await send_briefing(analysis)         # 3. Slack 전송

def start_scheduler():
    scheduler.start()
```

## Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
""",

"07_aws_architecture.md": """# AWS SA 에이전트 — 서버리스 아키텍처 설계

## 아키텍처 다이어그램

```
[EventBridge Scheduler]
    매일 07:00 KST
         │
         ▼
[Lambda: Data Collector]  ──→  [Aurora Serverless v2]
         │                      (매출/재고/고객 DB)
         ▼
[Lambda: Claude Analyzer] ──→  [Secrets Manager]
    Claude API 호출              (API Key 관리)
         │
         ├──→ [S3]  (리포트 원본 저장)
         │
         ▼
[Lambda: Notifier]
    ├──→ [Slack Webhook]  (경영진 채널)
    └──→ [SES]           (이메일 백업)

[CloudFront + S3]  ◄──  [React 대시보드]
    정적 호스팅                  Vercel 또는 S3
         │
         ▼
[API Gateway + Lambda]  (REST API)
```

## AWS CDK 핵심 코드 (Python)

```python
# infrastructure/app_stack.py
from aws_cdk import (
    Stack, Duration,
    aws_lambda as lambda_,
    aws_events as events,
    aws_events_targets as targets,
    aws_rds as rds,
    aws_secretsmanager as sm,
)
from constructs import Construct

class AiReportStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Claude API Key → Secrets Manager
        api_secret = sm.Secret(self, "ClaudeApiKey",
            secret_name="ai-report/claude-api-key")

        # Lambda: Claude 분석기
        analyzer_fn = lambda_.Function(self, "AnalyzerFn",
            runtime=lambda_.Runtime.PYTHON_3_11,
            code=lambda_.Code.from_asset("lambda/analyzer"),
            handler="handler.main",
            timeout=Duration.seconds(60),
            memory_size=512,
            environment={"SECRET_ARN": api_secret.secret_arn})
        api_secret.grant_read(analyzer_fn)

        # EventBridge: 매일 오전 7시 KST (22:00 UTC)
        rule = events.Rule(self, "DailyBriefing",
            schedule=events.Schedule.cron(hour="22", minute="0"))
        rule.add_target(targets.LambdaFunction(analyzer_fn))
```

## 월 예상 비용

| 시나리오 | Lambda | Aurora | S3 | 합계 |
|----------|--------|--------|-----|------|
| 소형 (5명) | $2 | $15 | $1 | **$18** |
| 중형 (30명) | $8 | $30 | $3 | **$41** |
| 대형 (100명) | $25 | $80 | $10 | **$115** |

## CloudWatch 알람

- Lambda 오류율 > 1% → SNS → 담당자 SMS
- Lambda 실행시간 > 30초 → 알림
- Aurora CPU > 80% → 스케일업 트리거
""",

"08_security_report.md": """# 보안담당자 에이전트 — 보안 리뷰 보고서

## STRIDE 위협 모델링

| 위협 | 대상 | 현재 상태 | 대응 방안 |
|------|------|-----------|-----------|
| Spoofing | API 인증 | 미적용 | JWT + AWS Cognito |
| Tampering | 보고서 데이터 | 부분 적용 | S3 Object Lock |
| Repudiation | 브리핑 전송 | 미적용 | CloudTrail 감사 로그 |
| Info Disclosure | API Key 노출 | 위험 | Secrets Manager 필수 |
| DoS | Lambda 과부하 | 부분 | 동시실행 제한 설정 |
| Elevation | IAM 권한 | 위험 | 최소 권한 원칙 적용 |

## 취약점 분석

| 심각도 | 항목 | 설명 | 즉시 조치 |
|--------|------|------|-----------|
| 🔴 Critical | API Key 하드코딩 | 코드에 직접 포함 위험 | Secrets Manager 이전 |
| 🟠 High | Slack Webhook URL | 유출 시 스팸 전송 가능 | 환경변수 분리 |
| 🟠 High | DB 직접 접근 | 개발환경에서 외부 노출 | VPC 내부로 격리 |
| 🟡 Medium | 인증 없는 API | 대시보드 인증 미적용 | Cognito 추가 |
| 🟡 Medium | 로그에 PII 포함 | 고객 이름/연락처 노출 | 마스킹 처리 |

## 필수 보안 조치 체크리스트

### 즉시 (Day 0)
- [ ] ANTHROPIC_API_KEY → AWS Secrets Manager
- [ ] Slack Webhook URL → 환경변수
- [ ] .env 파일 .gitignore 추가

### 단기 (1주 이내)
- [ ] AWS Cognito 사용자 인증 구성
- [ ] Lambda IAM Role 최소 권한 적용
- [ ] VPC 격리 + DB 보안 그룹 설정
- [ ] CloudTrail 감사 로그 활성화

### 중기 (1개월)
- [ ] ISMS 준비: 정보자산 목록 작성
- [ ] 개인정보처리방침 작성 (PIPA 준수)
- [ ] 취약점 점검 (외부 보안 업체)
- [ ] 인시던트 대응 매뉴얼 작성
""",

"09_qa_report.md": """# QA/기술검토 에이전트 — 통합 검증 보고서

## 전체 완성도 평가

| 에이전트 | 완성도 | 코멘트 |
|----------|--------|--------|
| 기획자 (WBS) | 95점 | 기능명세 매우 구체적. Story Point 기준 명확 |
| 디자이너 | 88점 | 다크 테마 일관성 우수. 에러 상태 UX 보강 필요 |
| UX 전문가 | 90점 | 페르소나 현실적. 모바일 여정 더 상세화 권고 |
| 프론트엔드 | 85점 | 타입 안전성 우수. 에러 바운더리 추가 필요 |
| 백엔드 | 92점 | Claude 프롬프트 설계 매우 좋음. 재시도 로직 추가 |
| AWS SA | 90점 | 서버리스 최적화 적절. 멀티 AZ 설정 확인 필요 |
| 보안 | 88점 | Critical 항목 명확히 도출. 즉시 조치 리스트 실용적 |

**종합 완성도: 90/100점**

## 정합성 검증

| 검증 항목 | 결과 | 비고 |
|-----------|------|------|
| 기획 F-01 ↔ BE 수집 모듈 | ✅ PASS | 완전 일치 |
| 디자인 컴포넌트 ↔ FE 코드 | ✅ PASS | KpiCard 명세 일치 |
| BE API ↔ FE 훅 | ⚠️ WARN | 엔드포인트 URL 형식 통일 필요 |
| AWS 아키텍처 ↔ BE Dockerfile | ✅ PASS | Lambda + Container 양쪽 지원 |
| 보안 요건 ↔ 코드 | ⚠️ WARN | Secrets Manager 연동 코드 미포함 |

## 주요 테스트 케이스 10개

| TC | 시나리오 | 예측 결과 |
|----|---------|----------|
| TC-01 | 오전 7시 스케줄러 정상 실행 | ✅ PASS |
| TC-02 | Claude API 응답 15초 이내 | ✅ PASS |
| TC-03 | Slack 메시지 4000자 초과 시 분할 | ⚠️ WARN — 로직 미구현 |
| TC-04 | DB 연결 실패 시 알림 | ✅ PASS |
| TC-05 | Claude API 오류 시 재시도 | ⚠️ WARN — retry 로직 없음 |
| TC-06 | 대시보드 100건 데이터 렌더링 | ✅ PASS |
| TC-07 | 모바일 375px 레이아웃 | ✅ PASS |
| TC-08 | API Key 노출 없이 배포 | ✅ PASS |
| TC-09 | 동시 사용자 20명 부하 | ✅ PASS |
| TC-10 | 이전 날짜 브리핑 히스토리 조회 | ✅ PASS |

## Quick Win 개선사항 (1주 이내)

1. **Slack 메시지 분할**: 4000자 초과 시 chunk 처리 (30분 작업)
2. **Claude API 재시도**: exponential backoff 3회 (1시간 작업)
3. **FE-BE URL 통일**: api/v1 prefix 정렬 (30분 작업)

## 최종 배포 준비도

```
⚠️  CONDITIONAL READY

보안 Critical 항목 해결 후 배포 권고:
  □ API Key → Secrets Manager 이전
  □ Slack URL 환경변수 분리
  □ API 인증 (Cognito) 최소 구성

위 3개 항목 완료 시 → READY
예상 소요: 1~2일
```
""",

"10_FINAL_REPORT.md": """# PM 최종 통합 보고서

**생성 일시**: {datetime}  
**총 소요 시간**: 시뮬레이션 완료  
**참여 에이전트**: 9개 (PM · 기획 · 디자인 · UX · FE · BE · SA · 보안 · QA)

---

## Executive Summary

사내 AI 자동화 보고서 시스템의 기획→설계→코드→인프라→보안 전 영역 산출물이 완성되었습니다.
종합 완성도 **90/100점**, 보안 Critical 2건 해결 후 즉시 배포 가능합니다.
예상 효과: 경영진 보고서 수작업 3시간 → **완전 자동화**, 오전 7시 브리핑 성공률 목표 99%.

---

## 프로젝트 완성도 요약

| 영역 | 산출물 | 완성도 | 즉시 사용 |
|------|--------|--------|-----------|
| 기획 | 기능명세서 F-01~06 + 8주 WBS | 95점 | ✅ |
| 디자인 | 다크 테마 UI 시스템 + 와이어프레임 | 88점 | ✅ |
| 프론트엔드 | React/TS 컴포넌트 코드 | 85점 | ✅ (경미한 수정) |
| 백엔드 | FastAPI + Claude API 연동 코드 | 92점 | ✅ |
| 인프라 | AWS CDK IaC + 비용 시나리오 | 90점 | ✅ |
| 보안 | STRIDE 위협모델 + 취약점 리포트 | 88점 | ⚠️ Critical 해결 필요 |
| QA | 통합 테스트 10개 + 개선 권고 | — | ✅ |

---

## 즉시 실행 가능 vs 추가 검토 필요

### 즉시 실행 (Day 0~1)
- AWS 환경 셋업 및 CDK 배포
- Claude API + Slack Webhook 연동 테스트
- React 대시보드 Vercel 배포

### 추가 검토 필요 (1~3일)
- API Key → Secrets Manager 이전 (보안 Critical)
- Slack 4000자 초과 분할 로직 구현
- Claude API 재시도 로직 추가

---

## 예상 일정 및 리소스

| 단계 | 기간 | 인력 |
|------|------|------|
| 보안 조치 완료 | 1~2일 | BE 개발자 1명 |
| 통합 테스트 | 2~3일 | QA 1명 + BE 1명 |
| Production 배포 | 1일 | DevOps 1명 |
| **총계** | **약 1주** | **3명** |

---

## 핵심 리스크와 대응

| 리스크 | 확률 | 영향 | 대응 |
|--------|------|------|------|
| Claude API 지연 | 중 | 고 | 비동기 처리 + 캐시 |
| DB 스키마 변경 | 저 | 고 | 마이그레이션 버전 관리 |
| Slack API 장애 | 저 | 중 | SES 이메일 백업 전송 |

---

## 다음 액션 아이템

| # | 항목 | 담당 | 기한 |
|---|------|------|------|
| 1 | API Key Secrets Manager 이전 | BE팀 | D+1 |
| 2 | Slack 분할 로직 구현 | BE팀 | D+1 |
| 3 | Cognito 인증 구성 | DevOps | D+3 |
| 4 | 부하 테스트 (동시 20명) | QA팀 | D+5 |
| 5 | Production 배포 | DevOps | D+7 |

---

*본 보고서는 Claude Code 멀티 에이전트 시스템이 자동 생성했습니다.*  
*PM · 기획자 · 디자이너 · UX · 프론트엔드 · 백엔드 · AWS SA · 보안 · QA — 9개 에이전트 협업 산출물*
"""
}

def run_demo():
    print("""
╔══════════════════════════════════════════════════════════════╗
║     Multi-Agent Development Automation System                ║
║     Claude Code 기반 · 9개 전문 에이전트 오케스트레이션     ║
╚══════════════════════════════════════════════════════════════╝
""")
    print(f"  브리프: {BRIEF[:80]}...")
    print(f"  세션 ID: {SESSION}")
    print(f"  출력: {OUT}\n")
    print("=" * 66)

    steps = [
        ("PHASE 1", "PM", "브리프 분석 및 역할 배분", "01_pm_analysis.md", 0.8),
        ("PHASE 2", "Planner", "기능명세서 & WBS 작성", "02_plan_wbs.md", 0.8),
        ("PHASE 3", "Designer", "UI 디자인 시스템", "03_design_spec.md", 0.6),
        ("PHASE 3", "UX Expert", "사용자 여정 분석", None, 0.5),
        ("PHASE 3", "Frontend", "React/TS 컴포넌트 생성", "05_frontend_code.md", 0.6),
        ("PHASE 3", "Backend", "FastAPI + Claude 연동", "06_backend_code.md", 0.7),
        ("PHASE 3", "AWS SA", "서버리스 아키텍처 설계", "07_aws_architecture.md", 0.6),
        ("PHASE 3", "Security", "보안 취약점 리뷰", "08_security_report.md", 0.6),
        ("PHASE 4", "QA", "통합 검증 수행", "09_qa_report.md", 0.7),
        ("PHASE 5", "PM", "최종 통합 보고서 생성", "10_FINAL_REPORT.md", 0.5),
    ]

    start = time.time()
    current_phase = None

    for phase, agent, task, filename, delay in steps:
        if phase != current_phase:
            current_phase = phase
            labels = {
                "PHASE 1": "PM 에이전트 — 브리프 분석",
                "PHASE 2": "기획자 에이전트 — 기능명세서",
                "PHASE 3": "전문가 에이전트 병렬 실행",
                "PHASE 4": "QA / 기술검토",
                "PHASE 5": "PM 최종 통합",
            }
            print(f"\n[{phase}] {labels.get(phase, phase)}")

        ts = datetime.now().strftime("%H:%M:%S")
        print(f"  [{ts}] → [{agent:12s}] {task}...", end="", flush=True)
        time.sleep(delay)

        if filename and filename in OUTPUTS:
            content = OUTPUTS[filename]
            if filename == "10_FINAL_REPORT.md":
                content = content.replace("{datetime}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            (OUT / filename).write_text(content, encoding="utf-8")

        print(f"  ✓ 완료")

    # README 생성
    elapsed = time.time() - start
    files = sorted(OUT.glob("*.md"))
    file_list = "\n".join(f"- [{f.name}](./{f.name})" for f in files)
    readme = f"""# Multi-Agent 프로젝트 산출물

**세션 ID**: {SESSION}  
**생성 일시**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**총 소요 시간**: {elapsed:.1f}초  
**에이전트**: PM · 기획자 · 디자이너 · UX · 프론트엔드 · 백엔드 · AWS SA · 보안 · QA (9개)

## 산출물 목록
{file_list}
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")

    print(f"""
{'=' * 66}
  산출물 저장: {OUT}
  총 소요 시간: {elapsed:.1f}초
  생성 파일: {len(list(OUT.glob('*.md')))}개 마크다운 문서
{'=' * 66}
""")

if __name__ == "__main__":
    run_demo()
