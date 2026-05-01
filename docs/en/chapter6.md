# Consensus Mechanisms

The final verdict of an Aegis-Graph audit is the result of a **Multi-Agent Consensus Handshake**. This chapter details the mathematical and logical process by which the MARS swarm resolves conflicts and issues a sovereign proof.

## ⚖️ The Weighted Voting Model

Each agent in the MARS swarm (Vision, Graph, Logic) contributes a **Confidence Vector (v)** and an **Evidence Weight (w)** to the final decision.

| Agent | Core Metric | Base Weight (W) |
| :--- | :--- | :--- |
| **Vision (VF)** | Artifact Fidelity | 0.30 |
| **Graph (GN)** | Institutional Standing | 0.35 |
| **Logic (LA)** | Temporal Consistency | 0.35 |

---

## 🤝 The Handshake Protocol

1.  **Agent Discovery**: When an audit is initialized, the local node spins up a temporary MARS swarm.
2.  **Independent Audit**: Agents perform their specialized checks in parallel, generating internal evidence logs.
3.  **Conflict Detection**: If the Vision agent flags a "High Risk" but the Graph agent finds a "High Authority" institution, a **Consensus Conflict** is triggered.
4.  **CoT Resolution**: The Logic Auditor initiates a **Chain-of-Thought** reasoning path, querying both agents for their raw evidence. It then assigns a higher weight to the layer with the most robust primary-source alignment.

---

## 🔒 Settlement & Finality

Once the consensus threshold (`T > 0.90`) is met, the system generates a **Sovereign Audit Proof**.

*   **Finality**: Once a proof is signed by the MARS quorum, it is anchored to the institutional node's ledger.
*   **Immutability**: The reasoning trail (minus PII) is preserved to allow for future audits or appeals if new data enters the global graph.

---
*Return to [Documentation Home](README.md)*
