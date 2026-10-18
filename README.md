<div align="center">
  <img src="assets/hero-banner.png" alt="Aegis-Graph Banner" width="100%">
  
  <br>

  [![Project Logo](assets/logo-new.png)](https://aclas.college)

  # 🛡️ Aegis-Graph
  ### **The Sovereign Academic Audit Protocol**
  *Empowering Global Education with Sovereign Intelligence & Decentralized Graph Integrity*

  <p align="center">
    <a href="https://aclascollege.github.io/aegis-graph/"><b>Live Dashboard</b></a> •
    <a href="WHITEPAPER.md"><b>Whitepaper</b></a> •
    <a href="https://aclas.college"><b>Atlanta College of Liberal Arts and Sciences (ACLAS) Official Site</b></a>
  </p>

  <div>
    <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/License-CC--BY--NC--4.0-lightgrey?style=for-the-badge" alt="License">
    <img src="https://img.shields.io/github/stars/aclascollege/aegis-graph?style=for-the-badge" alt="Stars">
    <img src="https://img.shields.io/badge/i18n-8_Languages-00ffaa?style=for-the-badge&logo=google-translate" alt="Languages">
  </div>
</div>

---

## 🏛️ Executive Vision

**Aegis-Graph** is a decentralized framework specifically engineered to safeguard academic integrity in the age of synthetic data. While technically governed by the **Atlanta College of Liberal Arts and Sciences (ACLAS)**, it operates as a global, sovereign protocol powered by **Agentic GraphRAG**.

> "In an era of synthetic data, truth must be sovereign." — ACLAS Sovereign Node Group.

---

## ⚠️ Current Status

The hosted dashboard is a **non-production UI demo**. It no longer issues browser-side credential approvals; professional verification requires server-side document parsing, issuer evidence, revocation checks, and a signed audit response.

---

## 🚀 Key Features

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h4>👁️ Vision Forensics</h4>
      <p>Planned pixel-level and OCR-based analysis to detect AI-generated artifacts in digital credentials and transcripts.</p>
    </td>
    <td width="50%" valign="top">
      <h4>🗺️ Graph Navigator</h4>
      <p>Institution evidence resolution using a local index plus optional ROR lookup; ROR matches are supporting evidence, not automatic credential approval.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>⚖️ Logic Auditor</h4>
      <p>Evidence-weighted consistency checks for registry status, timelines, blacklist aliases, and missing credential-authenticity proof.</p>
    </td>
    <td width="50%" valign="top">
      <h4>🔒 Sovereign Ledger</h4>
      <p>Planned cryptographically signed audit trails for reproducible, tamper-evident credential review.</p>
    </td>
  </tr>
</table>

---

## 🧠 The Agentic Architecture (MARS)

Aegis-Graph operates via a collaborative **Multi-Agent Reasoning Swarm (MARS)**. Each agent handles a specific layer of the audit protocol, reaching consensus before issuing a final verdict.

```mermaid
graph TD
    A[Digital Credential] --> B{MARS Swarm}
    B --> C[Vision Agent]
    B --> D[Graph Agent]
    B --> E[Logic Agent]
    C --> F[Pixel Forensics]
    D --> G[ROR Node Sync]
    E --> H[CoT Validation]
    F & G & H --> I[Consensus Layer]
    I --> J[Sovereign Audit Certificate]
```

---

## 📊 Performance and Evaluation

Production benchmark claims are not published yet. Current development focuses on eliminating browser-side approvals, normalizing graph evidence, and making audit decisions reproducible before publishing precision/latency metrics.

*   **Audit Precision**: pending reproducible benchmark suite
*   **Verification Latency**: pending server-side implementation
*   **Privacy Model**: local PII scrubbing prototype; ZK evidence is roadmap work
*   **Global Node Coverage**: local index plus optional ROR lookup

---

## 🌍 Global Localization (8-Language Matrix)

Our dashboard and documentation are fully localized for international adoption:
🇺🇸 EN • 🇨🇳 CN • 🇪🇸 ES • 🇫🇷 FR • 🇩🇪 DE • 🇯🇵 JP • 🇰🇷 KR • 🇵🇹 PT

---

## 🛠️ Quick Start

**Prerequisites:** Python 3.10+, `pip`, `git`.

```bash
# 1. Clone the repository
git clone https://github.com/aclascollege/aegis-graph.git
cd aegis-graph

# 2. Install dependencies (creates the multi-agent runtime environment)
pip install -r requirements.txt

# 3. Launch the local auditor (runs the full verification pipeline)
python main_pipeline.py
```

**Python usage:**

```python
from core import AegisAuditor

auditor = AegisAuditor()
result = auditor.verify("example.edu")
print(result.verdict, result.evidence)
```

## 🗂️ Fraud Blacklist v2.0

`data/fraud_blacklist.json` (v2.0.0) lists **7 documented diploma mills** with per-entry evidence:

| Field | Meaning |
|-------|---------|
| `name` / `aliases` | Institution name and known aliases |
| `evidence_level` | `court_record` / `regulatory_action` / `investigative_report` |
| `sources` | URLs to primary sources (court filings, AG suits) |
| `severity` / `reason` | Risk rating and human-readable explanation |

```python
import json
with open("data/fraud_blacklist.json") as f:
    bl = json.load(f)
for e in bl["entries"]:
    print(e["name"], "—", e["evidence_level"])
```

---

Aegis-Graph is governed by the **AEGIS-GRAPH Open Governance Board**, with technical support from the **ACLAS Sovereign Research Group**. We welcome contributions from researchers, developers, and academic institutions worldwide.

- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <p>© 2026 <a href="https://aclas.college">Atlanta College of Liberal Arts and Sciences (ACLAS)</a>. All rights reserved.</p>
  <a href="https://aclas.college">
    <img src="assets/favicon.ico" width="30">
  </a>
</div>
