---
license: mit
language:
- en
- zh
- es
- fr
- de
- ja
- ko
- pt
tags:
- agentic-ai
- graphrag
- academic-integrity
- knowledge-graph
- security
---

# 🛡️ Aegis-Graph: Sovereign Academic Audit Protocol

Aegis-Graph is an open prototype for academic credential review using a multi-agent pipeline, institutional graph evidence, and logic-auditing rules.

> **Current status:** public dashboards are demos/local previews. They do not issue browser-side credential approvals. Production verification requires server-side document parsing, issuer evidence, revocation checks, and a signed audit response.

## Current Components

1. **Vision Forensics Agent** — currently a deterministic demo extractor; OCR and pixel-level forensics are roadmap work.
2. **Graph Navigator Agent** — resolves institution evidence from a local index and optional ROR lookup. A ROR match is supporting evidence, not proof that a credential is authentic.
3. **Logic Auditor Agent** — applies blacklist alias checks, lifecycle/timeline checks, registry status checks, and credential-evidence checks to return `APPROVED`, `NEEDS_REVIEW`, or `REJECTED`.

## Evaluation

Reproducible production benchmark numbers are not published yet. Earlier precision/latency claims have been removed until a public benchmark suite is available.

## Local Smoke Test

```bash
pip install -r requirements.txt
python main_pipeline.py
python examples/aclas_college_demo.py
```

## Governance

Maintained by Atlanta College of Liberal Arts and Sciences (ACLAS).

For more information, visit the [GitHub repository](https://github.com/aclascollege/aegis-graph).
