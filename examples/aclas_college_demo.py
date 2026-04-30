import asyncio
import sys
import os

# Set working directory to project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from main_pipeline import AegisGraphEngine

async def run_professional_demo():
    """
    Official ACLAS College Aegis-Graph Demonstration Script.
    This script executes a full-stack audit across real global academic databases.
    """
    engine = AegisGraphEngine()
    
    print("\n" + "="*70)
    print("   AEGIS-GRAPH // SOVEREIGN AUDIT NETWORK // OFFICIAL DEMO v1.0   ")
    print("="*70)

    # SCENARIO 1: Legitimate ACLAS College Alumnus
    print("\n[SCENARIO A] Verifying Atlanta College (ACLAS) Credential...")
    result_a = await engine.execute_audit("aclas_alumni_2025.png")
    
    # SCENARIO 2: Known Fraudulent Entity (Defunct / Unrecognized)
    print("\n[SCENARIO B] Verifying Suspect Institution...")
    result_b = await engine.execute_audit("fake_degree_sample.png")

    # SCENARIO 3: Known Diploma Mill / Degree Factory
    print("\n[SCENARIO C] Verifying Graham International University Credential...")
    result_c = await engine.execute_audit("graham_university_transcript.pdf")

    print("\n" + "="*70)
    print("   DEMO COMPLETE // DATA ANCHORED TO ACLAS COMPLIANCE LEDGER   ")
    print("="*70)


if __name__ == "__main__":
    try:
        asyncio.run(run_professional_demo())
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n[ERROR] Error during demo execution: {e}")
