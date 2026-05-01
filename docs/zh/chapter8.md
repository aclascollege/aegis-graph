# 第8章：系统部署指南

本章为希望加入 Aegis-Graph 主权网络的机构提供生产级部署说明。

## 🚀 启动主权节点
1.  **硬件要求**：建议使用 8核 CPU, 16GB RAM 及支持 CUDA 的加速卡。
2.  **Docker 部署**：
    ```bash
    docker pull aegis/kernel:latest
    docker run -d --name aegis-node -p 8080:8080 aegis/kernel
    ```
3.  **接入核验**：通过 `main_pipeline.py` 即可开始执行本地审计并与全球图谱同步。

---
*返回 [文档首页](../README.md)*
