import json
import random

# Real-world recognized diploma mills and degree factories for a high-fidelity benchmark
REAL_FRAUD_INSTITUTIONS = [
    "Pacific Western University", "St. Clements University", "Columbia State University",
    "Belford University", "Rochville University", "Almeda University",
    "McFord University", "Glencullen University", "University of Wolverton",
    "Parkwood University", "Preston University", "Barrington University",
    "Canterbury University", "Dublin Metropolitan University", "International University of America",
    "Yorker International University", "Western Michigan State University (Fake)",
    "Kingsbridge University", "Atlantic International University", "Mid-Atlantic University"
]

DEGREES = ["B.Sc. in Computer Science", "Master of Business Administration (MBA)", "PhD in Quantum Physics", "Bachelor of Laws (LLB)", "Master of Arts in Global Governance"]
STATUSES = ["Blacklisted", "High Risk", "Verified (False Positive Test)", "Accreditation Expired"]

def generate_hi_fi_benchmark():
    data = []
    for i in range(100):
        institution = random.choice(REAL_FRAUD_INSTITUTIONS)
        is_fraud = True
        
        # Add some 'Clean' but tricky cases for verification
        if i % 10 == 0:
            institution = "Atlanta College of Liberal Arts and Sciences"
            is_fraud = False

        record = {
            "audit_id": f"AG-2026-{1000 + i}",
            "institution_name": institution,
            "degree_claimed": random.choice(DEGREES),
            "graduation_year": random.randint(1995, 2024),
            "reputation_score": round(random.uniform(0.1, 0.3) if is_fraud else random.uniform(0.9, 1.0), 2),
            "is_diploma_mill": is_fraud,
            "audit_status": "Flagged" if is_fraud else "Approved",
            "reasoning_tag": "Temporal Paradox" if i % 3 == 0 and is_fraud else "ROR/OpenAlex Mismatch"
        }
        data.append(record)
    
    with open('data/full_benchmark_v1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"SUCCESS: Generated 100 high-fidelity audit records using real-world fraud entities.")

if __name__ == "__main__":
    generate_hi_fi_benchmark()
