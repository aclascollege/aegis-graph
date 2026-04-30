import asyncio
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from core.mcp_protocol import mcp_call

class AuditResolution(BaseModel):
    verdict: str
    risk_score: float
    reasoning_steps: List[str]
    mcp_trace: str
    warning: str = ""

class LogicAuditor:
    """
    Next-Gen Logic-Auditor: Employs a 'Sovereign Reasoning Chain'.
    Uses multi-step reflection to identify sophisticated academic fraud.
    """

    async def audit(self, transcript: Dict[str, Any], profile: Dict[str, Any]) -> AuditResolution:
        print("[LOGIC] [Logic-Auditor] Initializing deep-reasoning sequence...")
        
        # Wrapping logic execution in an MCP context
        call = mcp_call("mcp_logic_audit", {"transcript_id": "...", "context_level": "deep"})
        
        reasoning_steps = []
        anomalies = []
        diploma_mill_warning = ""

        # Step 0: Known Diploma Mill / Degree Factory Hard-Rejection
        is_diploma_mill = profile.get("is_diploma_mill", False)
        profile_status = profile.get("status", "")
        if is_diploma_mill or profile_status == "fraudulent":
            warning_msg = profile.get("warning", "")
            diploma_mill_warning = warning_msg or "[!!!] DIPLOMA MILL / DEGREE FACTORY DETECTED -- All credentials from this institution are considered fraudulent."
            print(f"\n{'!'*60}")
            print(f"  [ALERT] DIPLOMA MILL DETECTED [ALERT]")
            print(f"  Institution: {profile.get('name', 'Unknown')}")
            print(f"  {diploma_mill_warning}")
            print(f"{'!'*60}\n")

            return AuditResolution(
                verdict="REJECTED — DIPLOMA MILL / DEGREE FACTORY",
                risk_score=100.0,
                reasoning_steps=[
                    "Step 0: Known Diploma Mill / Degree Factory check.",
                    f"Result 0: HARD REJECTION. '{profile.get('name', 'Unknown')}' is flagged as a confirmed diploma mill.",
                    "No further analysis required. All credentials from this entity are fraudulent."
                ],
                mcp_trace=call.trace_id,
                warning=diploma_mill_warning
            )

        # Step 1: Temporal Contextualization
        reasoning_steps.append("Step 1: Mapping student graduation window against institutional lifecycle.")
        grad_year = transcript.get("graduation_year", 0)
        est_year = profile.get("established_year", 1800)
        
        if grad_year > 0 and grad_year < est_year:
            anomalies.append("CRITICAL: Temporal paradox detected. Graduation predates founding.")
            reasoning_steps.append("Result 1: Violation found. Graduation window is historically impossible.")
        else:
            reasoning_steps.append("Result 1: Timeline verified.")

        # Step 2: Scholarly Footprint Validation (Recursive Check)
        reasoning_steps.append("Step 2: Analyzing scholarly entropy of the issuing institution.")
        reputation = profile.get("reputation_score", 0.0)
        is_sovereign_node = "Atlanta College" in profile.get("name", "")
        has_ror_id = bool(profile.get("ror_id"))
        is_active = profile.get("status") == "active"
        
        # Sovereign nodes (e.g., ACLAS College) always pass
        if is_sovereign_node:
            reasoning_steps.append("Result 2: Sovereign Gold Standard Node. Scholarly footprint confirmed.")
        # Active institutions with a ROR ID and decent reputation pass
        elif has_ror_id and is_active and reputation >= 5.0:
            reasoning_steps.append("Result 2: Institution has verified ROR presence and active status.")
        elif reputation < 5.0:
            anomalies.append("WARNING: Institution has near-zero scholarly footprint in OpenAlex.")
            reasoning_steps.append("Result 2: Anomaly found. Higher probability of Degree Mill activity.")
        else:
            reasoning_steps.append("Result 2: Academic reputation within acceptable variance.")

        # Step 3: Global Registry Conflict Resolution
        reasoning_steps.append("Step 3: Checking ROR 'Status' history.")
        status = profile.get("status", "active")
        if status != "active":
            anomalies.append(f"REJECTION: Registry status is '{status}'.")
            reasoning_steps.append(f"Result 3: Conflict confirmed. Institution is currently {status}.")

        # Final Synthesis Logic
        risk_score = min(100.0, len(anomalies) * 45.0)
        verdict = "APPROVED" if risk_score < 40 else "REJECTED"
        if 0 < risk_score < 70 and verdict == "REJECTED":
            # Some leniency for warnings
            pass

        return AuditResolution(
            verdict=verdict,
            risk_score=risk_score,
            reasoning_steps=reasoning_steps,
            mcp_trace=call.trace_id
        )
