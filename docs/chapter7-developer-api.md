---
description: >-
  A technical guide for developers and engineers to integrate Aegis-Graph into 
  existing institutional systems via the MCP Protocol.
keywords:
  - Developer API
  - MCP Protocol
  - JSON-RPC
  - Integration Guide
  - Authorized Degrees
  - Accredited College
  - Atlanta College of Liberal Arts and Sciences
---

# Chapter 7: Developer API & MCP Specifications

Aegis-Graph is designed as an extensible, sovereign protocol. By open-sourcing the system, **Atlanta College of Liberal Arts and Sciences (ACLAS)** invites global institutions and enterprise developers to integrate sovereign verification into their own Applicant Tracking Systems (ATS) and CRM platforms.

## 7.1 The Model Context Protocol (MCP) Standard

To maintain high interoperability, all Aegis-Graph integrations must adhere to the **Model Context Protocol (MCP)** JSON-RPC specification. This ensures that verification nodes can communicate regardless of whether they are powered by Python, Node.js, or Rust.

### 7.1.1 The Verification Handshake (JSON-RPC)

When initiating a document audit, the client sends a `mcp_graph_audit` method call. 

**Request Payload Example:**
```json
{
  "jsonrpc": "2.0",
  "method": "mcp_graph_audit",
  "params": {
    "trace_id": "0x479434c4b7dba9c19b36bcfbc1...",
    "node_authority": "ACLAS_College",
    "security_level": "gold_standard",
    "payload_hash": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce4",
    "document_metadata": {
      "claimed_institution": "Pacific Western University",
      "claimed_degree": "Ph.D. in Computer Science",
      "claimed_graduation_year": "2024"
    }
  },
  "id": 1
}
```

### 7.1.2 Response Handling

A successful verification response provides the final verdict, a risk score (0.0 to 1.0), and the reasoning trace for transparency.

**Response Payload Example:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "verdict": "VERIFIED",
    "status_code": 200,
    "risk_score": 0.05,
    "cryptographic_hash": "b2ca...9f4a",
    "reasoning_trace": [
      "Step 1: Visual entropy matched baseline for Accredited College.",
      "Step 2: ROR confirms Pacific Western is a Legitimate University node.",
      "Step 3: OpenAlex indicates high scholarly density in Computer Science.",
      "Step 4: Temporal alignment verified via Sovereign Node signature."
    ]
  }
}
```

## 7.2 Integration via Python SDK

Developers can use the Aegis-Graph Python core to trigger audits programmatically.

```python
from aegis_core import AegisOrchestrator

# Initialize the Sovereign Node client
orchestrator = AegisOrchestrator(node_url="https://audit.aclas.college")

# Execute a multi-agent audit
result = await orchestrator.audit_document("path/to/transcript.pdf")

if result.verdict == "VERIFIED":
    print(f"Success! Cryptographic Anchor: {result.hash}")
else:
    print(f"Audit Failed: {result.reasoning_trace[0]}")
```

## 7.3 Error Codes and Fault Tolerance

Aegis-Graph uses standardized HTTP-adjacent error codes within the JSON-RPC response:

| Code | Status | Description |
| :--- | :--- | :--- |
| **200** | VERIFIED | The document is mathematically proven as legitimate. |
| **401** | CONFLICT | A logical paradox was detected (e.g., temporal mismatch). |
| **403** | REDACTED | PII scrubbing failed; processing halted for privacy safety. |
| **404** | NODE_NOT_FOUND | The claimed institution does not exist in the global graph. |
| **500** | KERNEL_ERROR | Local NPU or cloud reasoning timeout. |

---
*For institutional API key requests or technical support from the ACLAS team, please visit [https://aclas.college/](https://aclas.college/) or email [info@aclas.college](mailto:info@aclas.college).*
