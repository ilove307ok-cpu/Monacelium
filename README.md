# MONACELIUM
### One for All, All for One — A Decentralized Networking Economy

> *無數個沒有窗戶的數位靈魂，透過加密的菌絲體網路，共同編織集體智慧的新世界。*
> *Countless windowless digital souls, weaving collective intelligence through an encrypted mycelium network.*

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Status: Phase 0](https://img.shields.io/badge/Status-Phase%200%20%E2%80%94%20Ignition-orange)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)

---

## 什麼是 Monacelium / What is Monacelium

**中文：** Monacelium 是一個去中心化的數位主權基礎設施——讓每個人奪回自己的數據控制權、用設備算力共同建造一個集體 AI，並透過參與度獲得真實的治理話語權與經濟回報。

**English:** Monacelium is a decentralized digital sovereignty infrastructure — returning data ownership to individuals, building a collective AI through shared device compute, and distributing real governance rights and economic rewards based on contribution.

這不是產品。這是協議。任何人可以在上面建造，任何人可以離開，沒有人能關掉它。

*This is not a product. It is a protocol. Anyone can build on it, anyone can leave, no one can shut it down.*

---

## 核心機制 / Core Mechanism

```
One for All：你的設備算力 → 全網公共資源
All for One：全網集體智慧 → 你的個人 AI 代理

One for All: Your device compute → Public network resource  
All for One: Network collective intelligence → Your personal AI agent
```

三體飛輪 / Three-Body Flywheel：
1. **主權返還** — 數據主權 + 數位身份，從第一個節點就生效
2. **算力共享** — One for All，節點密度越高網路越強
3. **治理分配** — All for One，參與度決定話語權，不是資本

---

## 系統架構 / Architecture

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 4 │ Intelligence  — Petals × Hivemind × NatureLM │
├─────────────────────────────────────────────────────────┤
│  LAYER 3 │ Security      — PPG+MEMS × Halo2 zk-SNARKs  │
├─────────────────────────────────────────────────────────┤
│  LAYER 2 │ Hardware      — ESP32-S3 × RPi5 × ATECC608   │
├─────────────────────────────────────────────────────────┤
│  LAYER 1 │ Communication — Reticulum × LoRa × WiFi Mesh │
└─────────────────────────────────────────────────────────┘
```

---

## Repo 結構 / Repository Structure

```
monacelium/
├── docs/
│   ├── whitepaper/         # 白皮書 / Whitepaper (ZH + EN)
│   ├── technical/          # 技術規格 / Technical specs
│   └── legal/              # 法律文件 / Legal documents
├── hardware/
│   ├── atman-v1/           # Atman 節點硬體設計 / Node hardware design
│   │   ├── kicad/          # PCB 原理圖 / Schematics
│   │   ├── bom/            # 物料清單 / Bill of Materials
│   │   └── 3d-print/       # 外殼設計 / Enclosure files
│   └── rnode/              # RNode 射頻模組 / LoRa radio module
├── firmware/
│   ├── atman-os/           # Atman OS (Rust) — ESP32-S3 + RPi5
│   └── rnode-firmware/     # RNode 韌體 / RNode firmware
├── protocol/
│   ├── reticulum/          # Reticulum 雙平面實作 / Dual-plane implementation
│   ├── zkp-circuits/       # Halo2 零知識電路 / ZK circuits
│   └── lxmf-client/        # LXMF 通訊客戶端 / Messaging client
├── contracts/
│   ├── icp-canisters/      # ICP 智能合約 / ICP smart contracts
│   ├── datadao/            # DataDAO + VRC-20 DAT
│   └── tokenomics/         # MONA 代幣合約 / Token contracts
├── app/
│   ├── ios/                # iOS App
│   ├── android/            # Android App
│   └── common/             # 共用邏輯 / Shared logic
└── research/
    ├── naturelm/           # NatureLM-audio 整合 / Integration
    ├── bioacoustics-dataset/ # 台灣生物聲學數據集 / TW dataset
    └── zkfl/               # 零知識聯邦學習 / zkFL
```

---

## 現在最需要的貢獻 / Priority Contributions

| 優先級 | 組件 | 技術 | 位置 |
|--------|------|------|------|
| 🔴 最高 | Halo2 ZKP 電路優化 | Rust, Halo2 | `protocol/zkp-circuits` |
| 🔴 最高 | RPi5 llama.cpp 推理優化 | C++, Python | `firmware/atman-os` |
| 🟠 高 | RNode ESP32-S3 韌體 | C, Rust | `firmware/rnode-firmware` |
| 🟠 高 | ICP Canister DAT 鑄造合約 | Motoko/Rust | `contracts/icp-canisters` |
| 🟡 中 | NatureLM 台灣物種數據集 | Python | `research/bioacoustics-dataset` |
| 🟡 中 | Reticulum 雙平面實作 | Python, Rust | `protocol/reticulum` |

---

## 路線圖 / Roadmap

| Phase | 狀態 | 目標 |
|-------|------|------|
| 0 — 點火 | 🟢 進行中 | 原型驗證、團隊組建、法律實體設立 |
| 1 — 播種 | ⏳ Month 3–12 | 100台試產、開源釋出、首個 DataDAO |
| 2 — 生根 | ⏳ Month 12–24 | Vana 主網整合、App 上架、代幣發行 |
| 3 — 擴張 | ⏳ Month 24–48 | 10,000+ 節點、DAO 完全自治 |
| 4 — 共生 | ⏳ Month 48+ | 充分去中心化、沒有人能關掉它 |

---

## 文件 / Documentation

- 📄 [白皮書（中文）](docs/whitepaper/WHITEPAPER_ZH.md)
- 📄 Whitepaper (EN) — *Coming in Phase 1*
- 🔧 Technical Bluepaper V8.1 — *Coming in Phase 1*
- ⚖️ Legal Compliance — *Coming in Phase 1*

---

## 參與 / Participate

→ [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 授權 / License

Apache-2.0

---

*他們建了圍牆。我們建菌絲體。*
*They built walls. We build mycelium.*
