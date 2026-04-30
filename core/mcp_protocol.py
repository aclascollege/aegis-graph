import uuid
import time
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class MCPEnvelope(BaseModel):
    """
    Standardized Model Context Protocol (MCP) Envelope for Agent communication.
    Reflects the 2025/2026 industry standard for agentic interoperability.
    """
    jsonrpc: str = "2.0"
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    method: str
    params: Dict[str, Any]
    timestamp: float = Field(default_factory=time.time)
    trace_id: str = Field(default_factory=lambda: str(uuid.uuid4()))

class AegisAgentResponse(BaseModel):
    """Encapsulates the response from an Aegis Agent with reasoning metadata."""
    result: Any
    reasoning_chain: Optional[str] = None
    confidence_score: float = 1.0

def mcp_call(method: str, params: Dict[str, Any]) -> MCPEnvelope:
    """Helper to wrap calls into MCP envelopes for logging and telemetry."""
    envelope = MCPEnvelope(method=method, params=params)
    print(f"[MCP] >> CALL {envelope.method} (Trace: {envelope.trace_id[:8]})")
    return envelope
