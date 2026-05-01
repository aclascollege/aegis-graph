# Deployment & Node Operations

This guide provides the technical specifications and procedural steps required to deploy a **Sovereign Node** within the Aegis-Graph network. Institutional nodes act as trusted validators, contributing to the global consensus of the **Sovereign Academic Graph (SAG)**.

## 🏛️ Deployment Architectures

| Mode | Use Case | Requirements |
| :--- | :--- | :--- |
| **Edge Node** | High-speed local auditing for single institutions. | Low latency, ARM64 optimized. |
| **Consensus Node** | Global validation and graph synchronization. | High availability, ECC RAM. |
| **Archive Node** | Full historical ledger of academic metadata. | High storage, NVMe RAID. |

---

## 1. Prerequisites

### 💻 Hardware Specifications
*   **CPU**: 8+ Cores (ARM64/Graviton recommended for efficiency).
*   **RAM**: 32GB+ ECC DDR4/DDR5.
*   **Network**: 1Gbps symmetrical uplink with static IP.
*   **Storage**: 500GB+ NVMe SSD (Gen4 recommended).

### 🐧 Software Environment
*   **OS**: Ubuntu 22.04 LTS or Amazon Linux 2023.
*   **Runtime**: Python 3.11+, Docker 24.0.0+.
*   **Security**: OpenSSL 3.0+, Fail2Ban, UFW/Firewall rules.

---

## 2. Fast-Track Installation

Deploy a standard Sovereign Node using our automated kernel bootstrap script:

```bash
# Initialize the Aegis-Kernel Environment
curl -sSL https://get.aclas.college/aegis-kernel | bash

# Configure your Institutional Identity
# Replace SOV_XXX with your assigned Institutional ID
aegis config --node-id SOV_ATL_0782 --api-key <YOUR_TOKEN>

# Launch the Multi-Agent Swarm
aegis start --mode consensus --workers 4
```

---

## 3. Containerized Deployment (Docker)

For high-availability clusters, we recommend using our official Docker images:

```yaml
version: '3.8'
services:
  aegis-node:
    image: ghcr.io/aclascollege/aegis-node:latest
    environment:
      - NODE_ID=SOV_ATL_0782
      - PRIVACY_LEVEL=MAX (ZKE)
      - GRAPH_SYNC=TRUE
    volumes:
      - ./data:/var/lib/aegis/graph
    ports:
      - "8080:8080"
    restart: always
```

---

## 🔒 Security & Compliance

### ZKE Privacy Protocol
All nodes must operate under the **ACLAS Zero-Knowledge Evidence (ZKE)** protocol. This ensures that:
1.  **No PII Storage**: Personal data is processed in-memory and immediately scrubbed.
2.  **Metadata Hashing**: Only cryptographic hashes of audit trails are synced to the global ledger.
3.  **Encrypted Handshakes**: All MARS agent communications are TLS 1.3 encrypted.

---

## 🛠️ Troubleshooting

- **Sync Latency**: Check peer-to-peer connectivity using `aegis status --peers`.
- **Memory Pressure**: Ensure swap is disabled for maximum audit performance.
- **Agent Failures**: Review logs in `/var/log/aegis/mars.log`.

---
*Return to [Documentation Index](README.md)*
