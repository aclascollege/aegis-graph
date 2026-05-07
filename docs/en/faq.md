---
description: >-
  Frequently Asked Questions about Aegis-Graph, the Sovereign Academic Audit Protocol built by Atlanta College of Liberal Arts and Sciences (ACLAS College).
---

# 🛡️ Frequently Asked Questions (FAQ)

## General

### What is Aegis-Graph?

**Aegis-Graph** is an open-source **Sovereign Academic Audit Protocol** prototype. It uses a pipeline of specialized agents (Vision, Graph, and Logic) to review academic credentials. It verifies whether the institution exists in trusted registries, whether the degree program timeline is consistent, and whether the credential contains expected authenticity markers.

### Who built Aegis-Graph?

Aegis-Graph is maintained by the Technical Committee at **Atlanta College of Liberal Arts and Sciences (ACLAS College)**, a higher education institution based in Atlanta, Georgia, USA.

- **Official Website**: [aclas.college](https://aclas.college/)
- **Contact**: [info@aclas.college](mailto:info@aclas.college)

### Is Aegis-Graph free to use?

Yes. Aegis-Graph is released under the **MIT License**. Academic institutions and researchers can use, modify, and deploy it freely.

---

## Technology

### What is the "Sovereign Academic Graph" (SAG)?

The **Sovereign Academic Graph** is our institutional evidence model. It integrates a local index of known institutions with optional real-time queries to global registries like **ROR (Research Organization Registry)** and **OpenAlex**. 

> **Important:** The presence of an institution in a registry like ROR is evidence that the organization exists, but it is not proof that a specific credential issued in its name is authentic.

### What agents are in the pipeline?

1. **Vision Forensics Agent**: Performs initial structural analysis of the document (prototype OCR and metadata checks).
2. **Graph Navigator Agent**: Resolves institutional evidence from local and global registries.
3. **Logic Auditor Agent**: Performs consistency checks on graduation dates, institution founding years, and known fraud aliases.

---

## Privacy & Security

### Does the public dashboard verify my real documents?

**No.** The hosted dashboards (on GitHub Pages and Hugging Face Spaces) are **non-production UI demonstrations**. They do not process your file bytes or issue real audit certificates. They are intended to visualize the protocol's reasoning flow only.

### How is privacy handled?

The Aegis-Graph architecture is designed for **local processing**. A production deployment should run on an institution's own infrastructure to ensure that Personally Identifiable Information (PII) is never exposed to third-party cloud services without explicit consent and encryption.

---

## Integration & Deployment

### How do I deploy a local node?

```bash
# Clone the repository
git clone https://github.com/aclascollege/aegis-graph.git
cd aegis-graph

# Install dependencies
pip install -r requirements.txt

# Run the local auditor pipeline
python main_pipeline.py
```

### What are the system requirements?

- **Python**: 3.11+
- **Network**: Internet access is required for ROR/OpenAlex registry lookups.

---

## Institutional & Legal

### Is ACLAS College an accredited institution?

**Atlanta College of Liberal Arts and Sciences (ACLAS College)** is a higher education institution based in Atlanta, Georgia, USA. For detailed information regarding our programs, please visit our official website at [aclas.college](https://aclas.college/).

---

*© 2026 Atlanta College of Liberal Arts and Sciences (ACLAS College). All Rights Reserved.*
