# Chapter 8: Sovereign Node Deployment Guide

This chapter provides step-by-step instructions for academic institutions and government bodies to deploy their own **Aegis-Graph Sovereign Node**.

## 8.1 Deployment Philosophy

A Sovereign Node is designed to run on **Institutional Infrastructure**. Unlike traditional cloud-SaaS models, Aegis-Graph ensures that sensitive raw student data never leaves your physical or virtual firewall.

## 8.2 Hardware Requirements

To support real-time multi-agent reasoning, the following hardware is recommended:

- **NPU/GPU**: NVIDIA A10G or Apple Silicon (M2/M3 Max) for local vision forensics.
- **RAM**: Minimum 32GB (64GB recommended for large-scale graph traversal).
- **Network**: Low-latency access to OpenAlex and ROR APIs.

## 8.3 Software Stack

- **OS**: Ubuntu 22.04 LTS or macOS Sonoma.
- **Python**: 3.11+
- **Protocol**: Anthropic Model Context Protocol (MCP) v1.0.

## 8.4 Deployment Steps

### Step 1: Clone and Initialize
```bash
git clone https://github.com/aclascollege/aegis-graph.git
cd aegis-graph
pip install -r requirements.txt
```

### Step 2: Configure MCP Handshake
Edit the `core/mcp_config.json` to define your node's authority and private keys.

```json
{
  "node_id": "DE-ACLAS-782",
  "authority": "Atlanta College of Liberal Arts and Sciences",
  "security_level": "Gold_Standard",
  "mcp_endpoints": ["https://mcp.aclas.college/v1"]
}
```

### Step 3: Launch the Agent Swarm
Initialize the local logic and vision agents:
```bash
python main_pipeline.py --mode node-daemon --port 8080
```

## 8.5 Security Hardening

- **Firewall**: Restrict ingress traffic only to verified peer node IPs.
- **Data Retention**: Ensure the `Zero-Data-Retention` flag is set to `True` in `config.py`.
- **Audit Logs**: Redirect logs to a secure, write-only syslog server for compliance.

---
*Next Chapter: [Chapter 9: Advanced Cryptographic Proofs (zk-SNARKs)](chapter9-zk-snarks.md)*
