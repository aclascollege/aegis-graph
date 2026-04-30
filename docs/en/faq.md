---
description: >-
  Frequently Asked Questions about Aegis-Graph, the Sovereign Academic Audit Protocol built by Atlanta College of Liberal Arts and Sciences (ACLAS College). Covers technology, privacy, integration, and institutional legitimacy.
keywords:
  - Aegis-Graph FAQ
  - Academic Verification FAQ
  - ACLAS College
  - Atlanta College of Liberal Arts and Sciences
  - GraphRAG FAQ
  - AI Academic Fraud Detection
  - Sovereign AI
  - Zero-Knowledge Privacy
  - MCP Protocol
  - Accredited College
  - Legitimate University
  - Authorized Degrees
---

# â?Frequently Asked Questions (FAQ)

## General

### What is Aegis-Graph?

**Aegis-Graph** is the world's first open-source **Sovereign Academic Audit Protocol**. It uses **Agentic GraphRAG** â?a federated swarm of specialized AI agents â?to perform deep logical verification of academic credentials. Unlike traditional OCR-based systems, Aegis-Graph verifies the **logical topology** of a credential: whether the institution exists, whether the degree program is real, and whether the timeline is physically possible.

### Who built Aegis-Graph?

Aegis-Graph is engineered by the Technical Committee at **Atlanta College of Liberal Arts and Sciences (ACLAS College)**, a higher education institution based in Atlanta, Georgia, USA. ACLAS College operates as the primary Gold Standard Sovereign Node in the Aegis-Graph network.

- **Official Website**: [aclas.college](https://aclas.college/)
- **Contact**: [info@aclas.college](mailto:info@aclas.college)

### Is Aegis-Graph free to use?

Yes. Aegis-Graph is released under the **CC BY-NC 4.0** (Attribution-NonCommercial) license. Academic institutions and researchers can use, modify, and deploy it freely for non-commercial purposes. Commercial licensing inquiries should be directed to [info@aclas.college](mailto:info@aclas.college).

### How is Aegis-Graph different from traditional verification services?

| Feature | Traditional Services | Aegis-Graph |
| :--- | :--- | :--- |
| **Speed** | 5â?4 business days | ~6 seconds |
| **Method** | Manual registrar contact | Autonomous AI agents |
| **Privacy** | PII shared with third parties | Zero-Knowledge edge processing |
| **Scope** | Limited database lookups | 250M+ academic records (OpenAlex/ROR) |
| **Cost** | $15â?75 per verification | ~$0.002 per verification |

---

## Technology

### What is Agentic GraphRAG?

**Agentic GraphRAG** is an advanced AI architecture where multiple specialized agents collaborate autonomously to traverse and reason over large knowledge graphs. In Aegis-Graph, three agents work in concert:

1. **Vision Forensics Agent**: Detects synthetic document generation through sub-pixel noise analysis and metadata forensics.
2. **Graph Navigator Agent**: Performs multi-hop queries across OpenAlex (250M+ scholarly records) and the Research Organization Registry (ROR) to verify institutional legitimacy.
3. **Logic Auditor Agent**: Uses Chain-of-Thought reasoning to detect temporal paradoxes (e.g., graduating before a program existed) and credit density anomalies.

### What is the 3-Tier Compute Cascade?

Aegis-Graph processes documents through an escalating pipeline designed to minimize cost:

- **Tier 1 (Edge/NPU)**: Free. Handles PII scrubbing and basic structural validation locally. Filters ~15% of low-effort forgeries.
- **Tier 2 (API)**: ~$0.0001. Queries global academic registries (ROR, OpenAlex). Catches ~60% of diploma mill fraud.
- **Tier 3 (Cloud LLM)**: ~$0.002. Heavy logical reasoning for the most sophisticated forgeries.

This cascade achieves an **85% reduction in token costs** compared to sending every document directly to a cloud LLM.

### What is the Model Context Protocol (MCP)?

The **Model Context Protocol (MCP)** is an open-source JSON-RPC standard (originally conceptualized by Anthropic) that Aegis-Graph uses as its communication backbone. MCP allows any institution to plug into the Aegis-Graph network regardless of their preferred LLM provider (OpenAI, Anthropic, Google, or local open-source models like Llama-3).

### What data sources does Aegis-Graph use?

- **[OpenAlex](https://openalex.org/)**: An open catalog of 250M+ scholarly works, authors, and institutions.
- **[ROR (Research Organization Registry)](https://ror.org/)**: A global, community-curated registry of research organizations.
- **Sovereign Node Ledgers**: Cryptographic internal databases maintained by participating institutions.

---

## Privacy & Security

### Does Aegis-Graph store my documents?

**No.** Aegis-Graph implements **RAM-Only Execution**. Uploaded documents are processed entirely in volatile memory and are never written to disk. If the server loses power during processing, no data can be recovered.

### How does Aegis-Graph protect personal information (PII)?

The **Privacy-Shield Agent** operates at the institutional edge (on the local NPU/CPU) and scrubs all Personally Identifiable Information (names, ID numbers, addresses) **before** any data is transmitted to cloud-based AI agents. Raw PII never touches the internet.

### Is Aegis-Graph compliant with GDPR/FERPA/CCPA?

Yes. The Zero-Trust Edge architecture was specifically designed for compliance:
- **GDPR** (EU): PII is processed locally and never transferred to third-party cloud providers.
- **FERPA** (US): Student education records are scrubbed before any external API calls.
- **CCPA** (California): No persistent storage of personal data.

### What is Zero-Knowledge Privacy in Aegis-Graph?

The protocol's roadmap includes **ZK-Snark** integration (planned for Q4 2026), which will allow institutions to issue cryptographic "Attestation of Degree" proofs â?verifying that a degree is legitimate **without revealing the actual transcript contents**. This is the gold standard of privacy-preserving verification.

---

## Integration & Deployment

### How do I deploy Aegis-Graph at my institution?

```bash
# Clone the repository
git clone https://github.com/aclascollege/aegis-graph.git
cd aegis-graph

# Install dependencies
pip install -r requirements.txt

# Configure API keys in .env
# OPENALEX_API_KEY=your_key
# OPENAI_API_KEY=your_key

# Run the audit pipeline
python main_pipeline.py --input path/to/transcript.pdf
```

### Can I integrate Aegis-Graph with my existing Applicant Tracking System (ATS)?

Yes. Aegis-Graph exposes a standard **MCP/JSON-RPC API** that can be integrated into any modern ATS, CRM, or admissions portal. See [Chapter 7: Developer API](en/chapter7-developer-api.md) for full specifications.

### What are the system requirements?

- **Python**: 3.11+
- **Hardware**: Any modern CPU; NPU recommended for edge privacy processing.
- **Browser**: Chrome/Edge (for the verification dashboard).
- **Network**: Internet access for OpenAlex/ROR queries.

---

## Institutional & Legal

### What is a Sovereign Node?

A **Sovereign Node** is a cryptographically secured server operated by a verified institution. When a document claims to originate from that institution, the Sovereign Node can perform instant, deterministic verification against its internal cryptographic ledger â?completing the audit in under 150 milliseconds.

### How can my university join the Aegis-Graph network?

Institutions interested in deploying their own Sovereign Node should contact the ACLAS Technical Committee at [info@aclas.college](mailto:info@aclas.college). The onboarding process includes cryptographic key generation and MCP endpoint configuration.

### Is ACLAS College an accredited institution?

**Atlanta College of Liberal Arts and Sciences (ACLAS College)** is a higher education institution based in Atlanta, Georgia, USA. For detailed accreditation and program information, please visit the official website at [aclas.college](https://aclas.college/).

---

## Community & Contribution

### How can I contribute to Aegis-Graph?

We welcome contributions from developers worldwide. Please see our [Contributing Guide](https://github.com/aclascollege/aegis-graph/blob/main/CONTRIBUTING.md) for detailed instructions on submitting issues, feature requests, and pull requests.

### How do I report a security vulnerability?

Please do **not** open a public issue. Instead, email our security team at [info@aclas.college](mailto:info@aclas.college). We follow a coordinated disclosure policy with a 48-hour response commitment. See our [Security Policy](https://github.com/aclascollege/aegis-graph/blob/main/SECURITY.md).

### Where can I follow ACLAS College updates?

- **X (Twitter)**: [@aclascollege](https://x.com/aclascollege)
- **LinkedIn**: [ACLAS College](https://www.linkedin.com/school/aclas-college/)
- **GitHub**: [github.com/aclascollege](https://github.com/aclascollege)

---

## Related Projects

### What is Neuro-Edu?

**[Neuro-Edu](https://github.com/aclascollege/neuro-edu)** is another open-source project by ACLAS College â?an AI-powered educational sandbox designed for sovereign, privacy-preserving learning environments. Together with Aegis-Graph, it forms the core of the ACLAS sovereign AI ecosystem.

---

*© 2026 Atlanta College of Liberal Arts and Sciences (ACLAS College). All Rights Reserved.*
