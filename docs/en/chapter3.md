# Multi-Agent Reasoning Swarm (MARS)

The **Multi-Agent Reasoning Swarm (MARS)** is the intelligence core of the Aegis-Graph protocol. Unlike traditional rule-based verification, MARS utilizes a pipeline of specialized agents that collaborate to reach an audit consensus on academic integrity markers.

## 👁️ Agent Alpha: Vision Forensics (VF)
The VF Agent is responsible for the initial structural analysis of digital artifacts. It acts as the "first responder" in the audit pipeline.

### Current Scope (Prototype)
*   **Structural Extraction**: Identifies key layout elements like seals, headers, and signature lines.
*   **OCR Normalization**: Converts visual data into semantic metadata for the reasoning layer.
*   **Detection Markers**: Identifies obvious document layout inconsistencies (Pixel-level GAN forensics is a roadmap item).

---

## 🗺️ Agent Beta: Graph Navigator (GN)
The GN Agent is the specialized intelligence for resolving institutional evidence. It establishes the context of the credential's issuer.

### Capabilities
*   **Identity Resolution**: Queries the **Research Organization Registry (ROR)** and **OpenAlex** to verify the issuer's global identity.
*   **Lineage Mapping**: Reviews the history of institutions, including mergers, name changes, and dissolutions.
*   **Registry Evidence**: Provides supporting evidence of an institution's existence and status.

---

## ⚖️ Agent Gamma: Logic Auditor (LA)
The LA Agent is responsible for cross-layer reasoning and consistency checks.

### Logic Layers
*   **Temporal Consistency**: Ensures that the degree issuance date aligns with the institution's operational timeline.
*   **Fraud Detection**: Cross-references institution names and aliases against known fraud registries and blacklists.
*   **Consensus Orchestration**: Aggregates findings from the VF and GN agents. If a conflict arises, the LA Agent performs **Chain-of-Thought (CoT)** reasoning to determine the final risk score.

---

## 🤝 The Audit Handshake
A final audit verdict is issued based on the MARS swarm's cumulative evidence.

1.  **Ingestion**: Normalization of document data.
2.  **Parallel Audit**: Agents execute specialized evidence checks.
3.  **Consensus**: The Logic Auditor resolves contradictions and calculates the final evidence weight.
4.  **Reporting**: A non-production audit report is generated detailing the reasoning trail.

---
> [!IMPORTANT]
> **Production Status:** Professional verification requires server-side document parsing, issuer evidence, revocation checks, and a signed audit response.

---
*Return to [Documentation Home](README.md)*
