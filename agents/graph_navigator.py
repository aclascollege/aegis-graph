import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx
from pydantic import BaseModel


class InstitutionProfile(BaseModel):
    """Normalized institution evidence returned by the graph layer."""

    name: str = "Unknown Institution"
    ror_id: Optional[str] = None
    country: Optional[str] = None
    status: str = "unknown"
    established_year: Optional[int] = None
    reputation_score: float = 0.0
    source: str = "none"
    match_confidence: float = 0.0
    is_diploma_mill: bool = False
    warning: str = ""


class GraphNavigator:
    def __init__(self, local_index_path: str = "data/global_academic_full_index_v2.json"):
        self.local_index_path = Path(local_index_path)
        self.api_url = "https://api.ror.org/organizations"
        self.local_cache = self._load_local_cache()

    def _load_local_cache(self) -> List[Dict[str, Any]]:
        try:
            with self.local_index_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (OSError, json.JSONDecodeError):
            return []

    @staticmethod
    def _normalize(value: str) -> str:
        return " ".join(value.lower().replace("&", "and").split())

    def _local_match(self, name: str) -> Optional[InstitutionProfile]:
        query = self._normalize(name)
        if len(query) < 3 or query == "unknown institution":
            return None

        for item in self.local_cache:
            item_name = item.get("name", "")
            normalized_name = self._normalize(item_name)
            if query == normalized_name:
                return InstitutionProfile(
                    name=item_name,
                    ror_id=item.get("ror_id"),
                    country=item.get("country"),
                    status=item.get("status", "active"),
                    established_year=item.get("established_year") or item.get("established"),
                    reputation_score=float(item.get("reputation_score", 5.0)),
                    source="local_index",
                    match_confidence=1.0,
                )

        return None

    @staticmethod
    def _extract_ror_name(item: Dict[str, Any]) -> str:
        names = item.get("names") or []
        for candidate in names:
            if candidate.get("types") and "ror_display" in candidate.get("types", []):
                return candidate.get("value", "Unknown Institution")
        return names[0].get("value", "Unknown Institution") if names else "Unknown Institution"

    @staticmethod
    def _extract_country(item: Dict[str, Any]) -> Optional[str]:
        locations = item.get("locations") or []
        if not locations:
            return None
        return locations[0].get("geonames_details", {}).get("country_name")

    async def navigate(self, name: str) -> InstitutionProfile:
        """
        Resolve an institution name against the local index and ROR.

        A ROR match is evidence that an organization exists, not proof that an
        uploaded credential is authentic. The logic layer must still evaluate
        document evidence and registry consistency before issuing a verdict.
        """
        local = self._local_match(name)
        if local:
            return local

        query = self._normalize(name)
        if len(query) < 3 or query == "unknown institution":
            return InstitutionProfile(name=name, warning="No institution name could be resolved from the credential.")

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(self.api_url, params={"query": name})
                response.raise_for_status()
                results = response.json().get("items", [])
        except (httpx.HTTPError, json.JSONDecodeError) as exc:
            return InstitutionProfile(
                name=name,
                status="unverified",
                source="ror_unavailable",
                warning=f"ROR lookup failed: {exc.__class__.__name__}",
            )

        if not results:
            return InstitutionProfile(
                name=name,
                status="unverified",
                source="ror",
                warning="Institution not found in ROR results.",
            )

        top_result = results[0]
        return InstitutionProfile(
            name=self._extract_ror_name(top_result),
            ror_id=top_result.get("id"),
            country=self._extract_country(top_result),
            status=top_result.get("status", "unknown"),
            source="ror",
            match_confidence=float(top_result.get("score") or 0.0),
            reputation_score=5.0,
        )

    async def verify_institution(self, name: str) -> InstitutionProfile:
        """Backward-compatible wrapper for older examples."""
        return await self.navigate(name)


if __name__ == "__main__":
    import asyncio

    async def main():
        nav = GraphNavigator()
        res = await nav.verify_institution("University of Balamand")
        print(res.model_dump())

    asyncio.run(main())
