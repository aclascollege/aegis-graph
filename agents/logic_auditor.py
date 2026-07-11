import json
from pathlib import Path
from typing import Any, Dict, List

from pydantic import BaseModel

from core.mcp_protocol import mcp_call


class AuditResolution(BaseModel):
    verdict: str
    risk_score: float
    reasoning_steps: List[str]
    mcp_trace: str
    warning: str = ""


class LogicAuditor:
    """
    Evidence-weighted logic auditor for credential review.

    The auditor treats registry matches as supporting evidence only. It does not
    approve a credential solely because an institution exists in ROR or because a
    file name contains a trusted-looking keyword.
    """

    def __init__(self, blacklist_path: str = "data/fraud_blacklist.json"):
        self.blacklist_path = Path(blacklist_path)

    @staticmethod
    def _normalize(value: str) -> str:
        return " ".join(value.lower().replace("&", "and").split())

    def _load_blacklist_names(self) -> set[str]:
        names: set[str] = set()
        try:
            with self.blacklist_path.open("r", encoding="utf-8") as f:
                blacklist_data = json.load(f)
        except (OSError, json.JSONDecodeError):
            return names

        for entry in blacklist_data.get("blacklist", []):
            if entry.get("name"):
                names.add(self._normalize(entry["name"]))
            for alias in entry.get("aliases", []):
                names.add(self._normalize(alias))
        return names

    async def audit(self, transcript: Dict[str, Any], profile: Dict[str, Any]) -> AuditResolution:
        print("[LOGIC] [Logic-Auditor] Initializing evidence-weighted review...")
        call = mcp_call("mcp_logic_audit", {"transcript_id": "...", "context_level": "deep"})

        reasoning_steps: List[str] = []
        anomalies: List[tuple[str, float]] = []
        warnings: List[str] = []

        profile_name = self._normalize(profile.get("name", ""))
        transcript_name = self._normalize(transcript.get("institution_name", ""))
        blacklist_names = self._load_blacklist_names()
        profile_blacklisted = profile_name in blacklist_names
        transcript_blacklisted = transcript_name in blacklist_names
        is_diploma_mill = profile.get("is_diploma_mill", False) or profile_blacklisted or transcript_blacklisted
        profile_status = profile.get("status", "unknown")

        reasoning_steps.append("Step 0: Checking known diploma-mill and degree-factory indicators.")
        if is_diploma_mill or profile_status == "fraudulent":
            warning_msg = profile.get("warning") or "DIPLOMA MILL / DEGREE FACTORY DETECTED -- credentials from this institution require hard rejection."
            rejected_name = transcript.get("institution_name") if transcript_blacklisted else profile.get("name", "Unknown")
            return AuditResolution(
                verdict="REJECTED - DIPLOMA MILL / DEGREE FACTORY",
                risk_score=100.0,
                reasoning_steps=[
                    *reasoning_steps,
                    f"Result 0: HARD REJECTION. '{rejected_name}' is flagged by the fraud registry.",
                    "No approval is issued because the issuing entity is disqualified.",
                ],
                mcp_trace=call.trace_id,
                warning=warning_msg,
            )
        reasoning_steps.append("Result 0: No exact blacklist or alias match found.")

        reasoning_steps.append("Step 1: Mapping graduation window against institutional lifecycle.")
        grad_year = int(transcript.get("graduation_year") or 0)
        est_year = profile.get("established_year")
        if grad_year > 0 and est_year and grad_year < int(est_year):
            anomalies.append(("CRITICAL: Graduation predates the institution founding year.", 55.0))
            reasoning_steps.append("Result 1: Temporal violation found.")
        elif est_year:
            reasoning_steps.append("Result 1: Timeline is internally consistent.")
        else:
            warnings.append("Founding year unavailable; temporal validation is incomplete.")
            reasoning_steps.append("Result 1: Founding year unavailable; timeline needs review.")

        reasoning_steps.append("Step 2: Evaluating registry evidence without granting automatic approval.")
        has_ror_id = bool(profile.get("ror_id"))
        source = profile.get("source", "none")
        match_confidence = float(profile.get("match_confidence") or 0.0)
        if has_ror_id and profile_status == "active":
            reasoning_steps.append("Result 2: Active ROR presence found as supporting institution-existence evidence.")
        elif has_ror_id:
            anomalies.append((f"WARNING: ROR status is '{profile_status}', not active.", 30.0))
            reasoning_steps.append("Result 2: Registry presence found, but status requires review.")
        else:
            anomalies.append(("WARNING: No verified registry identifier was resolved.", 35.0))
            reasoning_steps.append("Result 2: No ROR identifier available.")

        if source in {"ror", "local_index"} and 0 < match_confidence < 0.80:
            anomalies.append(("WARNING: Institution match confidence is below the production threshold.", 25.0))
            reasoning_steps.append("Result 2b: Match confidence is low and should be manually reviewed.")

        reasoning_steps.append("Step 3: Checking credential-authenticity evidence.")
        if not transcript.get("credential_id") and not transcript.get("signature_verified"):
            anomalies.append(("WARNING: No credential ID or cryptographic issuer signature was verified.", 35.0))
            reasoning_steps.append("Result 3: Credential authenticity remains unproven.")
        else:
            reasoning_steps.append("Result 3: Credential-level evidence is present.")

        risk_score = min(100.0, sum(weight for _, weight in anomalies))
        if risk_score >= 85:
            verdict = "REJECTED"
        elif risk_score > 0 or warnings:
            verdict = "NEEDS_REVIEW"
        else:
            verdict = "APPROVED"

        return AuditResolution(
            verdict=verdict,
            risk_score=risk_score,
            reasoning_steps=[*reasoning_steps, *[item for item, _ in anomalies], *warnings],
            mcp_trace=call.trace_id,
            warning="; ".join(warnings),
        )
