"""
Multi-Agent Development Automation System
PM 에이전트가 8개 전문 에이전트를 오케스트레이션하여
브리프 하나로 기획서 → 코드 → 인프라 → 보안보고서까지 자동 산출

Usage:
    python orchestrator.py --brief "프로젝트 내용" --output ./outputs
    python orchestrator.py --brief-file brief.txt
"""

import anthropic
import json
import time
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
from agents.pm_agent import PMAgent
from agents.planner_agent import PlannerAgent
from agents.designer_agent import DesignerAgent
from agents.ux_agent import UXAgent
from agents.frontend_agent import FrontendAgent
from agents.backend_agent import BackendAgent
from agents.aws_sa_agent import AWSSAAgent
from agents.security_agent import SecurityAgent
from agents.qa_agent import QAAgent

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║     Multi-Agent Development Automation System                ║
║     Claude Code 기반 · 8개 전문 에이전트 오케스트레이션     ║
╚══════════════════════════════════════════════════════════════╝
"""

class MultiAgentOrchestrator:
    """
    PM 에이전트가 총괄하는 멀티 에이전트 자동화 시스템.
    
    파이프라인:
    [브리프] → PM → 기획자 → [병렬: 디자이너, UX, FE, BE, SA, 보안] → QA → PM 통합
    """

    def __init__(self, output_dir: str = "./outputs"):
        self.client = anthropic.Anthropic()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_dir = self.output_dir / self.session_id
        self.session_dir.mkdir(parents=True, exist_ok=True)
        self.results = {}
        self.start_time = None

        # 에이전트 초기화
        self.pm = PMAgent(self.client)
        self.planner = PlannerAgent(self.client)
        self.designer = DesignerAgent(self.client)
        self.ux = UXAgent(self.client)
        self.frontend = FrontendAgent(self.client)
        self.backend = BackendAgent(self.client)
        self.aws_sa = AWSSAAgent(self.client)
        self.security = SecurityAgent(self.client)
        self.qa = QAAgent(self.client)

    def log(self, agent: str, msg: str, level: str = "INFO"):
        icons = {"INFO": "◆", "OK": "✓", "WARN": "!", "RUN": "→"}
        ts = datetime.now().strftime("%H:%M:%S")
        icon = icons.get(level, "·")
        print(f"  [{ts}] {icon} [{agent:12s}] {msg}")

    def save(self, filename: str, content: str) -> Path:
        path = self.session_dir / filename
        path.write_text(content, encoding="utf-8")
        return path

    def run(self, brief: str) -> dict:
        print(BANNER)
        self.start_time = time.time()
        print(f"  프로젝트 브리프:\n  {brief[:120]}{'...' if len(brief)>120 else ''}\n")
        print(f"  세션 ID: {self.session_id}")
        print(f"  출력 경로: {self.session_dir}\n")
        print("=" * 66)

        # ─── STEP 1: PM 분석 및 역할 배분 ────────────────────────────────
        print("\n[PHASE 1] PM 에이전트 — 브리프 분석 및 역할 배분")
        self.log("PM", "브리프 분석 시작...", "RUN")
        pm_analysis = self.pm.analyze_brief(brief)
        self.results["pm_analysis"] = pm_analysis
        self.save("01_pm_analysis.md", pm_analysis)
        self.log("PM", "분석 완료 → 8개 에이전트 지시 준비", "OK")

        # ─── STEP 2: 기획자 ──────────────────────────────────────────────
        print("\n[PHASE 2] 기획자 에이전트 — 기능명세서 & WBS")
        self.log("Planner", "요구사항 정의 및 WBS 작성 중...", "RUN")
        plan = self.planner.create_plan(brief, pm_analysis)
        self.results["plan"] = plan
        self.save("02_plan_wbs.md", plan)
        self.log("Planner", "기능명세서 + WBS 완료", "OK")

        # ─── STEP 3: 병렬 전문가 에이전트 ───────────────────────────────
        print("\n[PHASE 3] 전문가 에이전트 병렬 실행 (6개 역할)")
        context = {"brief": brief, "pm_analysis": pm_analysis, "plan": plan}

        specialist_jobs = [
            ("Designer",  self.designer.design,   "03_design_spec.md"),
            ("UX Expert", self.ux.analyze,        "04_ux_report.md"),
            ("Frontend",  self.frontend.build,    "05_frontend_code.md"),
            ("Backend",   self.backend.build,     "06_backend_code.md"),
            ("AWS SA",    self.aws_sa.architect,  "07_aws_architecture.md"),
            ("Security",  self.security.review,   "08_security_report.md"),
        ]

        for agent_name, agent_fn, filename in specialist_jobs:
            self.log(agent_name, "작업 시작...", "RUN")
            result = agent_fn(context)
            self.results[agent_name.lower().replace(" ", "_")] = result
            self.save(filename, result)
            self.log(agent_name, "완료", "OK")

        # ─── STEP 4: QA 통합 검증 ────────────────────────────────────────
        print("\n[PHASE 4] QA / 기술검토 에이전트 — 통합 검증")
        self.log("QA", "전체 산출물 통합 테스트 중...", "RUN")
        qa_report = self.qa.validate(self.results)
        self.results["qa_report"] = qa_report
        self.save("09_qa_report.md", qa_report)
        self.log("QA", "검증 완료", "OK")

        # ─── STEP 5: PM 최종 통합 ────────────────────────────────────────
        print("\n[PHASE 5] PM 에이전트 — 최종 통합 보고서")
        self.log("PM", "전체 결과 통합 중...", "RUN")
        final = self.pm.integrate(brief, self.results)
        self.results["final_report"] = final
        self.save("10_FINAL_REPORT.md", final)

        # ─── INDEX 생성 ──────────────────────────────────────────────────
        elapsed = time.time() - self.start_time
        index = self._make_index(elapsed)
        self.save("README.md", index)
        self.log("PM", f"완료! 총 소요: {elapsed:.1f}초", "OK")

        print(f"\n{'=' * 66}")
        print(f"  산출물 저장 위치: {self.session_dir}")
        print(f"  총 소요 시간: {elapsed:.1f}초")
        print(f"  생성 파일: {len(list(self.session_dir.glob('*.md')))}개")
        print(f"{'=' * 66}\n")

        return {"session_dir": str(self.session_dir), "elapsed": elapsed, "results": self.results}

    def _make_index(self, elapsed: float) -> str:
        files = sorted(self.session_dir.glob("*.md"))
        file_list = "\n".join(f"- [{f.name}](./{f.name})" for f in files if f.name != "README.md")
        return f"""# Multi-Agent 프로젝트 산출물

**세션 ID**: {self.session_id}  
**생성 일시**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**총 소요 시간**: {elapsed:.1f}초  
**사용 에이전트**: PM · 기획자 · 디자이너 · UX · 프론트엔드 · 백엔드 · AWS SA · 보안 · QA (9개)

## 산출물 목록

{file_list}

## 시스템 구성
- **오케스트레이터**: PM 에이전트 (Claude claude-sonnet-4-20250514)
- **파이프라인**: 브리프 → PM 분석 → 기획 → [병렬 전문가 6개] → QA → 최종 통합
- **GitHub**: [multi-agent-system](https://github.com/nambbong/multi-agent-system)
"""


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Development Automation")
    parser.add_argument("--brief", type=str, help="프로젝트 브리프 직접 입력")
    parser.add_argument("--brief-file", type=str, help="브리프 텍스트 파일 경로")
    parser.add_argument("--output", type=str, default="./outputs", help="출력 디렉토리")
    args = parser.parse_args()

    if args.brief_file:
        brief = Path(args.brief_file).read_text(encoding="utf-8").strip()
    elif args.brief:
        brief = args.brief
    else:
        brief = input("프로젝트 브리프를 입력하세요:\n> ").strip()

    if not brief:
        print("브리프가 비어 있습니다.")
        sys.exit(1)

    orchestrator = MultiAgentOrchestrator(output_dir=args.output)
    orchestrator.run(brief)


if __name__ == "__main__":
    main()
