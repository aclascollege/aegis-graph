# Chapter 8: Sovereign Node Deployment
This chapter guides institutions on how to join the Aegis-Graph network and run a private sovereign audit node.

## 1. Hardware Requirements
*   **CPU**: 8 Cores (ARM64 recommended)
*   **RAM**: 32GB ECC
*   **Storage**: 500GB NVMe (for local graph indexing)

## 2. Node Initialization
```bash
# Download the Sovereign Kernel
curl -sSL https://get.aclas.college/aegis-kernel | bash

# Bind Institutional ID
aegis config --node-id SOV_ATL_0782
```

## 3. Compliance
All nodes must adhere to the **ACLAS ZKE (Zero-Knowledge Evidence)** protocol, ensuring no PII is stored.
