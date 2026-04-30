# 第 8 章：主权节点部署指南
本章节指导机构如何接入 Aegis-Graph 网络并运行私有的主权审计节点。

## 1. 硬件要求
*   **CPU**: 8 核 (推荐 ARM64 架构)
*   **RAM**: 32GB ECC
*   **存储**: 500GB NVMe (用于本地图谱索引)

## 2. 节点初始化
```bash
# 下载主权内核
curl -sSL https://get.aclas.college/aegis-kernel | bash

# 绑定机构 ID
aegis config --node-id SOV_ATL_0782
```

## 3. 安全合规
所有节点必须遵守 **ACLAS ZKE (零知识证据)** 协议，确保不存储任何个人身份信息 (PII)。
