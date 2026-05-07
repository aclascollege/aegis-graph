# Institutional Evidence (SAG)

The **Sovereign Academic Graph (SAG)** is the institutional evidence layer of the Aegis-Graph protocol. It integrates locally maintained institutional indices with global public registries (such as ROR and OpenAlex) to provide the necessary context for credential auditing.

## 📊 Data Topology

The SAG is not a "judgment database" that proves a credential's authenticity; rather, it is a dynamic model that provides institutional background evidence.

### Core Evidence Sources
| Source | Role |
| :--- | :--- |
| **Local Index** | Caches metadata for high-trust institutions, blacklist aliases, and known fraud patterns. |
| **ROR** | Provides standardized identities (ROR IDs) and operational status for global research organizations. |
| **OpenAlex** | Provides scholarly output background and institutional impact metrics as supporting evidence. |

---

## 🏛️ Evidence Logic

During the audit process, the SAG is used to answer critical questions:
1. **Institutional Existence**: Does the institution have a record in recognized global registries?
2. **Lifecycle Consistency**: Is the credential issuance date within the institution's operational lifespan?
3. **Status Validation**: Is the institution currently active, or has it been flagged for revocation or fraud?

> [!IMPORTANT]
> **Key Clarification:** The presence of an institution in registries like ROR is evidence that the organization exists, but it is **not** proof that a specific credential issued in its name is authentic.

---

## ⚡ Indexing & Matching

To ensure accuracy in evidence resolution, Aegis-Graph utilizes several strategies:
1. **Normalization**: Institutional names are standardized to eliminate variations in spelling or symbols.
2. **Multi-Factor Matching**: Cross-references geographic location, founding year, and official domains.
3. **Evidence Weighting**: Matching results are assigned a confidence score, which serves as a key input for the LogicAuditor's final decision.

---
*Return to [Documentation Home](README.md)*
