# 貢獻指南 / Contributing to Monacelium

歡迎。Monacelium 是一個協議，不是一家公司。你的貢獻直接塑造它的走向。

---

## 最高優先級貢獻 / Top Priority

| 組件 | 目標 | 技術 | 位置 |
|------|------|------|------|
| Halo2 ZKP 電路優化 | 活體驗證延遲 <1 秒 | Rust, Halo2 | `protocol/zkp-circuits` |
| RPi5 llama.cpp 優化 | 1–3B 推理速度 2x | C++, ARM64 | `firmware/atman-os` |
| RNode ESP32-S3 韌體 | 完整 RNS 支援 | C, Rust | `firmware/rnode-firmware` |
| ICP Canister DAT 合約 | DAT 鑄造流程 | Motoko/Rust | `contracts/icp-canisters` |
| NatureLM 台灣數據集 | 本地物種基準 | Python | `research/bioacoustics-dataset` |

---

## 流程 / Process

```bash
git checkout -b feat/your-feature-name
git commit -m "feat: 描述你做了什麼"
# 發 PR，說明：改了什麼 / 為什麼 / 如何測試
```

---

## 貢獻度計算 / Contribution Scoring

所有合併的 PR 都記錄為參與度基分（Proof of Contribution），累積為治理票權。詳見白皮書第3章。

---

## 授權 / License

貢獻即同意 Apache-2.0 授權條款。

*代碼合併即記錄，永久可驗證。Every merged commit is permanently verifiable.*
