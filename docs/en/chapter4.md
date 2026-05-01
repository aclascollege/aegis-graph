# The Sovereign Academic Graph (SAG)

The **Sovereign Academic Graph (SAG)** is the definitive global registry of academic institutions, serving as the "ground truth" for the Aegis-Graph protocol. It consists of over **102,482 verified institutional nodes** and millions of contextual relationships.

## 📊 Data Topology

The SAG is not a static database but a dynamic, multi-layered graph that integrates authoritative data from global academic registries and institutional ledgers.

### Core Data Sources
| Source | Contribution |
| :--- | :--- |
| **ROR** | Primary Research Organization IDs and institutional metadata. |
| **OpenAlex** | Scholarly footprint, publication metrics, and institutional impact. |
| **Crossref** | DOI-level institutional affiliations and metadata accuracy. |
| **ACLAS Ledger** | High-authority sovereign node metadata and historical accreditation. |

---

## 🏛️ Node Anatomy
Each institutional node in the SAG contains a rich set of attributes required for sovereign auditing:

*   **Temporal Bounds**: Founding date, operational status, and dissolution history.
*   **Geospatial Vectors**: Precise coordinates and physical campus locations to detect geographic spoofing.
*   **Issuer Fingerprints**: Cryptographic identities and public keys for digital signature verification.
*   **Hierarchy Edges**: Relationships between parent universities, satellite campuses, and research institutes.

---

## ⚡ Indexing & Performance
To achieve sub-second verification latency, Aegis-Graph utilizes a high-performance indexing strategy:

1.  **Vectorized Search**: Institutional names and metadata are vectorized to allow for fuzzy matching against slight variations or misspellings.
2.  **Distributed Caching**: High-frequency institutional nodes are cached at the **Edge Node** layer for near-instant resolution.
3.  **Cross-Validation**: Every node is periodically re-validated across multiple global registries to ensure data freshness and integrity.

---

## 🔒 Data Sovereignty
In alignment with the **ACLAS ZKE (Zero-Knowledge Evidence)** protocol, the SAG only stores institutional metadata. 
*   **No PII Storage**: Personal student records are never stored on the graph.
*   **Verifiable Proofs**: The graph provides the *infrastructure* for verification, while the specific audit evidence remains private and decentralized.

---
*Return to [Documentation Home](README.md)*
