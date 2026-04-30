<div align="center">
  <img src="https://avatars.githubusercontent.com/u/195760091?v=4" width="120" height="120" alt="ACLAS Logo" style="border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.15)">
  
  # 🛡️ Aegis-Graph
  ### 主權學術審計與邏輯驗證協議
  
  [![Documentation](https://img.shields.io/badge/Docs-GitBook-0070f3?style=for-the-badge&logo=gitbook&logoColor=white)](https://atlanta-college-of-liberal-arts-and-sciences.gitbook.io/atlanta-college-of-liberal-arts-and-sciences/aegis-graph)
  [![Live Demo](https://img.shields.io/badge/Live-Demo-00dfd8?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aclascollege.github.io/aegis-graph/)
  [![License](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey?style=for-the-badge)](LICENSE)
  
  **「用主權 AI 與代理智能守護教育的未來。」**
</div>

---

### 🌍 全球語言導航 (Multi-language)

| 🌍 地區 | 語言矩陣 |
| :--- | :--- |
| **美洲 / 歐洲 / 非洲** | [🇺🇸 English](../README.md) • [🇫🇷 Français](README_FR.md) • [🇪🇸 Español](README_ES.md) • [🇩🇪 Deutsch](README_DE.md) • [🇵🇹 Português](README_PT.md) |
| **亞太地區** | [🇭🇰 繁體中文](README_ZH.md) • [🇯🇵 日本語](README_JP.md) • [🇰🇷 한국어](README_KR.md) |
| **中東地區** | [🇸🇦 العربية (RTL)](README_AR.md) |

---

## 🏛️ 機構背景

**Aegis-Graph** 是 [**亞特蘭大文理學院 (ACLAS College)**](https://aclas.college/) 的技術旗艦項目。作為一個主權節點，它旨在對抗由大語言模型 (LLM) 和視覺基礎模型生成的高仿真學術欺詐。

---

## 🚀 技術核心：代理式 GraphRAG

與傳統的 OCR 驗證不同，Aegis-Graph 通過 **3 層計算級聯** 驗證憑證的 **邏輯拓撲**。

### 🤖 代理集群 (Agent Swarm) 拆解
- **視覺取證代理 (Vision Forensics Agent)**：分析噪聲模式、元數據一致性和字體間距異常，以檢測高仿真的合成憑證。
- **圖譜導航代理 (Graph Navigator Agent)**：在全球 2.5 億條學術記錄 (OpenAlex/ROR) 中執行多跳查詢，驗證機構合法性與學術譜系。
- **邏輯審計代理 (Logic Auditor Agent)**：交叉引用畢業時間線、課程依賴關係和學分邏輯，檢測內部的語義矛盾。

---

## 🔒 隱私與安全設計

Aegis-Graph 採用了 **「主權邊緣 (Sovereign Edge)」** 安全模型：
*   **PII 脫敏**：個人身份信息在進入圖譜遍歷前，在邊緣端 (NPU 級別) 進行哈希或移除。
*   **零知識證明 (路線圖)**：未來將集成 ZK-Snarks，實現「學位認證」而無需洩露完整成績單。
*   **內存運行**：敏感文檔解析在臨時內存中進行，確保審計後的文檔不留痕跡。

---

## 🗺️ 2026-2027 發展路線圖

- **2026 Q3**: 全球節點上線 (歐盟與亞太機構集群)。
- **2026 Q4**: 集成 ZK 隱私層，實現不公開詳情的認證服務。
- **2027 Q1**: Aegis-Verify 隱私錢包 (主權憑證管理)。
- **2027 Q2**: 去中心化治理 (ACLAS 技術委員會 DAO)。

---

## 🛠️ 快速上手

```bash
# 1. 克隆主權節點
git clone https://github.com/aclascollege/aegis-graph.git
cd aegis-graph

# 2. 環境配置
# 創建 .env 文件並配置 API 密鑰:
# OPENALEX_API_KEY=your_key
# OPENAI_API_KEY=your_key
pip install -r requirements.txt

# 3. 啟動審計
python main_pipeline.py --input examples/sample_transcript.pdf
```

---

<div align="center">
  <p>© 2026 亞特蘭大文理學院 (ACLAS College). 版權所有。</p>
  <p>技術委員會: <a href="mailto:info@aclas.college">info@aclas.college</a></p>
</div>
