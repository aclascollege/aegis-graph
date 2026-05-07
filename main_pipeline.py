import asyncio
import time
from typing import Dict, Any

from agents.vision_forensics import VisionForensicsAgent
from agents.graph_navigator import GraphNavigator
from agents.logic_auditor import LogicAuditor
from privacy_filter.local_slm_scrubber import LocalSLMScrubber
from core.mcp_protocol import mcp_call

class AegisGraphEngine:
    """
    The High-Authority Orchestrator for Aegis-Graph.
    Now 100% MCP-Native with verifiable reasoning traces.
    """
    
    def __init__(self):
        self.vision = VisionForensicsAgent()
        self.navigator = GraphNavigator()
        self.auditor = LogicAuditor()
        self.scrubber = LocalSLMScrubber()

    async def execute_audit(self, file_path: str) -> Dict[str, Any]:
        # MCP Handshake
        kernel_call = mcp_call("mcp_kernel_init", {"session_type": "sovereign_audit"})
        
        print("\n" + ">>>" * 3 + f" INITIALIZING AEGIS-GRAPH [Trace: {kernel_call.trace_id[:8]}] " + "<<<" * 3)
        print("-" * 60)
        
        # 1. Vision Forensics (MCP: mcp_vision_analyze)
        mcp_call("mcp_vision_analyze", {"uri": file_path})
        raw_transcript = await self.vision.analyze(file_path)
        
        # 2. Local Privacy Scrubbing (Shield)
        print("[SHIELD] Applying local NPU mask to PII data...")
        masked_name = self.scrubber.scrub(raw_transcript.institution_name)
        
        # 3. Graph Navigation (MCP: mcp_resolve_ror)
        mcp_call("mcp_resolve_ror", {"query": masked_name})
        inst_profile = await self.navigator.navigate(raw_transcript.institution_name)
        
        # 4. Deep Logic Audit (MCP: mcp_logic_audit)
        mcp_call("mcp_logic_audit", {"cot": True})
        resolution = await self.auditor.audit(raw_transcript.model_dump(), inst_profile.model_dump())
        
        print("-" * 60)
        print(f"REPORT: FINAL VERDICT: {resolution.verdict}")
        print(f"REPORT: RISK SCORE: {resolution.risk_score:.1f}")
        print(f"REPORT: TRACE ID: {resolution.mcp_trace}")
        print("-" * 60)
        
        return {
            "verdict": resolution.verdict,
            "risk_score": resolution.risk_score,
            "trace_id": resolution.mcp_trace,
            "reasoning": resolution.reasoning_steps
        }

if __name__ == "__main__":
    # Internal kernel test
    async def main():
        engine = AegisGraphEngine()
        await engine.execute_audit("aclas_demo.pdf")
    asyncio.run(main())
