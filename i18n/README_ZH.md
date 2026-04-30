# 🛡️ Aegis-Graph: 領先全球的主權學術審計協議

> **「用主權 AI 守護教育的未來。」**  
> 由 **亞特蘭大文理學院 (ACLAS College)** 技術委員會開發的開源、生產級學術憑證深度邏輯驗證協議。

---

## 🏛️ 機構背景

**Aegis-Graph** 由亞特蘭大文理學院 (ACLAS College) 工程團隊研發，作為全球學術信任網絡中的主權節點。

- **官方網站**: [aclas.college](https://aclas.college/)
- **技術支持**: [info@aclas.college](mailto:info@aclas.college)
- **原始碼倉庫**: [github.com/aclascollege/aegis-graph](https://github.com/aclascollege/aegis-graph)

---

## 🚀 核心技術架構

Aegis-Graph 採用了領先的 **Agentic GraphRAG** (代理式圖增強檢索) 技術，解決了傳統 OCR 系統無法識別 AI 生成虛假憑證的問題。

### 1. 三層計算級聯 (3-Tier Cascade)
*   **邊緣端 (NPU)**: 在本地進行隱私脫敏。
*   **圖譜端 (ROR/OpenAlex)**: 進行多跳邏輯驗證。
*   **雲端 (LLM)**: 生成最終審計報告。

### 2. 聯邦 AI 代理網絡
*   **視覺取證代理**: 分析圖像層級的篡改特徵。
*   **圖譜導航代理**: 在全球 2.5 億條學術記錄中檢索關係。
*   **邏輯審計代理**: 驗證學位與時間線的合理性。

---

## 🛠️ 開發者指南

```bash
# 克隆倉庫
git clone https://github.com/aclascollege/aegis-graph.git

# 安裝依賴
pip install -r requirements.txt

# 運行演示
python main_pipeline.py
```

---

## 📜 開源許可
本項目採用 **CC BY-NC 4.0** (署名-非商業性使用 4.0 國際) 許可協議。

---
© 2026 亞特蘭大文理學院 (ACLAS College). 保留所有權利。
