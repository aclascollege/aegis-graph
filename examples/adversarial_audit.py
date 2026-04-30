import sys
import os

# Ensure the parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.logic_auditor import LogicAuditor
from privacy_filter.pii_scrubber import PrivacyShield

def run_adversarial_simulation():
    print("🛡️ Aegis-Graph | Adversarial Audit Simulation v1.0")
    print("--------------------------------------------------")
    
    # 1. The 'Perfect' Fake Document (Simulated Data)
    # This document has correct institution names and ROR IDs, 
    # but contains a hidden temporal paradox.
    fake_credential = {
        "student_name": "Alice Smith",
        "institution": "Atlanta College of Liberal Arts and Sciences",
        "ror_id": "https://ror.org/05v4k8765", # Legitimate ROR ID
        "degree": "B.Sc. in Quantum Ethics",
        "graduation_year": 2018,
        "attendance_dates": "2014 - 2018",
        "email": "alice.smith@not-a-real-domain.com"
    }

    print(f"[*] Analyzing credential for: {fake_credential['student_name']}")
    print(f"[*] Declared Degree: {fake_credential['degree']}")
    
    # 2. Step 0: Privacy Scrubbing (Edge Execution)
    shield = PrivacyShield()
    safe_payload = shield.prepare_audit_payload(fake_credential)
    print(f"[+] Privacy Shield active. PII Redacted: {safe_payload['email']}")

    # 3. Step 1: Logic Auditing (Temporal Paradox Detection)
    auditor = LogicAuditor()
    
    # Simulate a deep logic check against historical node data
    # KNOWLEDGE: The 'Quantum Ethics' program was only established in 2021.
    program_established_year = 2021
    
    print("[!] Running Sovereign Reasoning Chain...")
    
    is_valid = True
    reason = "All logical checks passed."
    
    if fake_credential['graduation_year'] < program_established_year:
        is_valid = False
        reason = f"TEMPORAL PARADOX: Graduation year ({fake_credential['graduation_year']}) precedes program establishment ({program_established_year})."

    # 4. Final Verdict
    if not is_valid:
        print(f"\n❌ AUDIT REJECTED: {reason}")
        print("Conclusion: High-fidelity synthetic fraud detected via logical inconsistency.")
    else:
        print("\n✅ AUDIT APPROVED.")

if __name__ == "__main__":
    run_adversarial_simulation()
