# Monacelium
> **去中心化隱私感測與邊緣 AI 網路** | DePIN + DataFi + 抗審查通訊

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Seed Stage](https://img.shields.io/badge/Status-Seed%20Stage-yellow)](https://github.com/ilove307ok-cpu/Monacelium)
[![Docs: V8.1](https://img.shields.io/badge/Docs-V8.1-blue)](./docs/)

---

## 📋 **我們在做什麼**

**Monacelium** 是一個垂直整合的 Web3 基礎設施,讓使用者能夠:
- 🔐 **完全擁有** 自己的生理與環境數據(透過零知識證明,原始數據永不離開本地設備)
- 💰 **獲得收益** 透過 VRC-20 DataDAO 將匿名化數據授權給 AI 研究機構
- 📡 **抗審查通訊** 結合 LoRa Mesh 與 WiFi,在斷網/災害情境下仍可運作
- 🎵 **無縫體驗** 以音樂串流作為入口,使用者無需理解技術細節即可參與

**核心產品:** Atman 節點 ($99 USD 硬體) = 本地 AI 推理 + 多模態感測 + 去中心化通訊

---

## 🏗️ **技術架構**
```
┌─────────────────────────────────────────────────────────┐
│  Application Layer (Vana DataDAO)                      │
│  [Music Streaming] [Health Monitor] [Secure Messaging] │
└────────────────────┬────────────────────────────────────┘
                     │ JSON-RPC API
┌────────────────────▼────────────────────────────────────┐
│  Compute & Logic (Atman Node)                          │
│  [TinyML] [zk-Proof] [Local LLM] [PoC Validator]       │
│  ESP32-S3  |  Halo2  |  Llama 3.2  |  Reputation       │
└────────────────────┬────────────────────────────────────┘
                     │ Reticulum Network Stack
┌────────────────────▼────────────────────────────────────┐
│  Communication Plane (Dual-Network)                    │
│  [Control] LoRa (915MHz) - Auth/Route/Emergency        │
│  [Data]    WiFi Mesh     - AI Inference/File Sync      │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ **技術棧**

| 層級 | 技術選型 | 用途 |
|------|---------|------|
| **硬體** | ESP32-S3 + Raspberry Pi 5 + PPG/MEMS | 本地感測與 AI 推理 |
| **通訊** | Reticulum (LoRa + WiFi) | 去中心化 Mesh 網路 |
| **隱私** | Halo2 zk-SNARKs + TEE | 零知識證明數據驗證 |
| **儲存** | IPFS + Arweave | 內容尋址不可變儲存 |
| **區塊鏈** | Vana Chain (VRC-20) | DataDAO 代幣標準 |
| **AI** | NCNN + Llama.cpp | 邊緣推理引擎 |

---

## 📦 **硬體規格: Atman Node V1**

| 組件 | 型號 | 成本 (USD) |
|------|------|-----------|
| 主控 MCU | ESP32-S3-WROOM-1 (8MB RAM) | $4.50 |
| 邊緣算力 | Raspberry Pi 5 (8GB) | $80.00 |
| 生理感測 | MAX30102 PPG + MEMS 麥克風 | $5.20 |
| 通訊模組 | SX1262 LoRa HAT (915MHz) | $12.00 |
| 安全晶片 | ATECC608A (硬體私鑰保存) | $2.00 |
| **總 BOM** | | **~$85** |
| **建議零售價** | | **$99** |

完整 BOM 與供應鏈: [hardware/bom.csv](./hardware/bom.csv)

---

## 🚀 **快速開始**

### 前置需求
- Python 3.9+
- Node.js 18+ (for tooling)
- Raspberry Pi 5 或相容 ARM64 SBC

### 安裝 Reticulum 測試網節點
```bash
# 1. Clone repo
git clone https://github.com/ilove307ok-cpu/Monacelium.git
cd Monacelium

# 2. 安裝 Reticulum 協議棧
pip3 install rns --break-system-packages

# 3. 執行最小測試網 (開發中)
cd firmware/reticulum-test
python3 test_node.py
```

> ⚠️ **注意:** 完整 Atman 韌體尚在開發中 (見 [Roadmap](#roadmap))

---

## 📚 **文件導覽**

| 文件 | 描述 |
|------|------|
| [技術藍皮書](./docs/technical-bluepaper.md) | 系統架構、通訊協議、隱私設計 |
| [代幣經濟](./docs/tokenomics.md) | MONA 發行機制、DAT 流通、PoC 公式 |
| [法律合規](./docs/legal/taiwan-compliance.md) | 台灣刑法 315-1、個資法分析 |
| [硬體設計](./hardware/README.md) | PCB 原理圖、BOM、組裝指南 |
| [API 參考](./docs/api-reference.md) | DataDAO SDK 使用範例 |

---

## 🗓️ **Roadmap** {#roadmap}

### Phase 0: 概念驗證 (2026 Q2)
- [x] V8.1 技術藍皮書完成
- [ ] Reticulum + LoRa 測試網 (3 節點)
- [ ] Halo2 on RPi5 Benchmark
- [ ] 法律意見書 (台灣/新加坡)

### Phase 1: 原型與開源 (2026 Q2-Q4)
- [ ] Atman V1 EVT (100 台試產)
- [ ] 開源硬體設計 (KiCad)
- [ ] 首個 DataDAO (MusBioDAO)
- [ ] Seed Round 融資 ($2.5M)

### Phase 2: 代幣經濟啟動 (2027 Q1-Q4)
- [ ] Vana 主網整合
- [ ] 批量生產 2,000 台
- [ ] IDO/LBP 代幣發行
- [ ] 首個 AI 公司授權協議

### Phase 3: 規模化生態 (2028+)
- [ ] 10,000+ 活躍節點
- [ ] Atman V2 (專用 ZK 加速晶片)
- [ ] DAO 完全自治

---

## 💰 **代幣經濟 (簡要)**

### 雙代幣設計
- **MONA**: 協議治理代幣 (總量 10 億,固定)
- **DAT**: 每個 DataDAO 獨立發行 (VRC-20 標準)

### 價值捕獲
1. AI 公司訪問數據 → 燃燒 1% MONA + 10% DAT
2. 協議手續費 → 50% 回購銷毀,50% 生態基金
3. 節點質押 MONA → 提升 PoC 分數,獲得更多 DAT 獎勵

詳細機制: [docs/tokenomics.md](./docs/tokenomics.md)

---

## 🆚 **競品對照**

| 功能 | Monacelium | Helium | Ocean Protocol | Audius | 紙鴿 App |
|------|-----------|--------|---------------|--------|---------|
| 硬體節點 | ✅ | ✅ | ❌ | ❌ | ❌ |
| DataFi | ✅ | ❌ | ✅ | ❌ | ❌ |
| 離線通訊 | ✅ (LoRa) | ✅ (LoRaWAN) | ❌ | ❌ | ✅ (藍牙) |
| zk 隱私 | ✅ (Halo2) | ❌ | ⚠️ (部分) | ❌ | ⚠️ |
| 音樂串流 | ✅ | ❌ | ❌ | ✅ | ❌ |
| **差異化** | **垂直整合** | 僅通訊 | 僅數據市場 | 僅音樂 | 僅聊天 |

---

## 🤝 **如何貢獻**

我們歡迎:
- 🐛 Bug 回報與修復
- 💡 功能建議
- 📖 文件改進
- 🔧 硬體測試回饋

請閱讀 [CONTRIBUTING.md](./CONTRIBUTING.md) 並遵循行為準則。

---

## 📄 **授權**

本專案採用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權:
- ✅ 允許商業使用
- ✅ 允許修改與再分發
- ⚠️ 需標明原作者
- ⚠️ 需保留授權聲明

硬體設計採用 [CERN-OHL-S v2](https://ohwr.org/cern_ohl_s_v2.txt) 開源硬體授權。

---

## 📞 **聯絡我們**

- **GitHub Issues**: [提交問題或建議](https://github.com/ilove307ok-cpu/Monacelium/issues)
- **Email**: [即將公開]
- **Discord**: [社群籌備中]

---

## 🙏 **致謝**

感謝以下開源專案:
- [Reticulum Network Stack](https://reticulum.network/) - 去中心化通訊協議
- [Vana Protocol](https://vana.org/) - DataDAO 標準
- [Halo2](https://github.com/zcash/halo2) - zk-SNARK 函式庫
- [Earth Species Project](https://www.earthspecies.org/) - NatureLM-audio
- [紙鴿 App](https://apps.apple.com/app/id6760900452) - 台灣離線通訊先驅

---

**最後更新:** 2026-04-02 | **版本:** V8.1 | **狀態:** Seed Stage