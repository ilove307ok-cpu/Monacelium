---
date: 2026-09-30
tags: [claude-code, tooling, evaluation, decision]
status: deferred
---

## Claude Code 外掛評估（來源：Threads @kwons_en 貼文）

**結論：不安裝，暫存備查。** 效益不足以自動執行。

| 外掛 | 判定 | 理由 |
|---|---|---|
| OmniRoute | 不裝 | 請求經第三方閘道，可能轉給免費供應商；模型品質不一；用訂閱轉發可能違反 ToS（未驗證）。上限問題改用官方 API key 備援。 |
| claude-mem | 暫緩 | 本機 Mac 才有意義；雲端 session 為一次性容器，記憶庫用完即丟。現有 `//handoff` + CLAUDE.md 已涵蓋大部分需求。 |
| playwright | 不需要 | 雲端環境已預裝 Chromium。 |
| frontend-design | 不需要 | 已有 `artifact-design` skill，功能重疊。 |

## claude-mem 審查摘要（淺層讀碼，非完整審計）
- 來源：github.com/thedotmack/claude-mem（main 淺層 clone，1,534 檔）
- Telemetry **預設開啟**（PostHog）→ 安裝後須 `npx claude-mem telemetry disable` 或 `CLAUDE_MEM_TELEMETRY=0`
- Cloud sync（sync.cmem.ai）預設關閉，需 token/user ID/hub URL 三者才啟動
- 壓縮預設走 Claude；可換 Gemini/OpenRouter/DeepSeek（會外送內容）
- PostToolUse hook 對每次工具呼叫觸發，額外消耗壓縮 token
- 資料位置 `~/.claude-mem/`（settings.json、.env）
- 未驗證：是否過濾工具輸出中的 token/key；各事件 telemetry 是否確實無內容

## 重新評估觸發條件
- 常在 Mac 本機長期跨對話開發同一專案，且 handoff 明顯不夠用
- claude-mem 官方提供預設關閉 telemetry 或本機-only 模式

## 安裝步驟（備用；憑記憶，可能過時）
1. `/plugin marketplace add thedotmack/claude-mem`
2. `/plugin install claude-mem`
3. `npx claude-mem telemetry disable`
4. 確認 `~/.claude-mem/settings.json` 的 `CLOUD_SYNC_*` 為空
