# Multi-Agent Reasoning Swarm (MARS)

The **Multi-Agent Reasoning Swarm (MARS)** is the decentralized intelligence core of the Aegis-Graph protocol. Unlike traditional rule-based verification, MARS utilizes a swarm of specialized AI agents that collaborate to reach a sovereign consensus on academic integrity.

## 👁️ Agent Alpha: Vision Forensics (VF)
The VF Agent is responsible for the pixel-level forensic analysis of digital artifacts. It acts as the "first responder" in the audit pipeline.

### Technical Specifications
*   **Model Architecture**: Optimized ResNet-50 backbone with custom attention layers for document fraud.
*   **Detection Vectors**:
    *   **Diffusion Artifacts**: Identifies high-frequency noise patterns typical of Stable Diffusion and Midjourney.
    *   **Vector Consistency**: Analyzes kerning, font weight, and SVG path integrity in PDF objects.
    *   **Seal Forensics**: Pixel-level comparison of institutional seals against a reference database of 40,000+ official stamps.
*   **Output**: A `Confidence Score [0.0 - 1.0]` and a heatmap of suspected manipulated regions.

---

## 🗺️ Agent Beta: Graph Navigator (GN)
The GN Agent is the specialized intelligence for traversing the **Sovereign Academic Graph (SAG)**. It establishes the institutional context of the credential.

### Capabilities
*   **Identity Resolution**: Queries the **Research Organization Registry (ROR)** and **OpenAlex** to verify the issuer's global identity.
*   **Lineage Mapping**: Traces the history of institutions, including mergers, name changes, and dissolutions.
*   **Scholarly Footprint**: Cross-references the issuer with global publication metrics to ensure the institution is active in the academic ecosystem.
*   **Connectivity**: Validates the relationship between the degree-granting body and its parent or affiliate organizations.

---

## ⚖️ Agent Gamma: Logic Auditor (LA)
The LA Agent is the "Chief Justice" of the swarm, responsible for cross-layer reasoning and paradox detection.

### Logic Layers
*   **Temporal Paradox Checking**: Ensures that the degree issuance date aligns with the institution's operational timeline (e.g., degree cannot pre-date founding).
*   **Program Credibility**: Verifies that the specific degree program exists within the institution's accredited curriculum for that specific period.
*   **Consensus Orchestration**: Aggregates the evidence from VF and GN agents. If a conflict arises (e.g., VF flags a seal but GN finds a high-authority node), the LA Agent initiates a **Chain-of-Thought (CoT)** reasoning path to resolve the discrepancy.

---

## 🤝 The Consensus Handshake
A final **Sovereign Audit Certificate** is only issued when the MARS swarm reaches a consensus threshold of `> 0.90`.

1.  **Initial Ingestion**: Multi-spectral data extraction.
2.  **Parallel Processing**: Agents execute specialized audits simultaneously.
3.  **Evidence Exchange**: Agents share intermediate findings via a secure handshake protocol.
4.  **Final Resolution**: The Logic Auditor issues the definitive verdict and anchors the cryptographic proof to the ledger.

---
*Return to [Documentation Home](README.md)*
