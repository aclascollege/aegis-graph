from typing import Dict, Any
from pydantic import BaseModel

class Transcript(BaseModel):
    institution_name: str
    graduation_year: int
    gpa: float

class VisionForensicsAgent:
    """
    Vision-Forensics Agent: Extracts structured data from credentials.
    """

    async def analyze(self, source_path: str) -> Transcript:
        print(f"[VISION] [Vision-Forensics] Extracting structured data from {source_path}")
        
        # Deterministic simulation for demo stability
        if "aclas" in source_path.lower():
            return Transcript(
                institution_name="Atlanta College of Liberal Arts and Sciences",
                graduation_year=2025,
                gpa=3.8
            )
        elif "graham" in source_path.lower():
            return Transcript(
                institution_name="Graham International University",
                graduation_year=2024,
                gpa=3.9
            )
        elif "fake" in source_path.lower() or "fraud" in source_path.lower():
            return Transcript(
                institution_name="Pacific Western University",
                graduation_year=2024,
                gpa=4.2
            )
        else:
            return Transcript(
                institution_name="Unknown Institution",
                graduation_year=2024,
                gpa=3.5
            )

