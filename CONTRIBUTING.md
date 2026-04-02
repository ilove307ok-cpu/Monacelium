# 貢獻指南

感謝你考慮為 Monacelium 做出貢獻!本指南將幫助你了解如何參與專案。

---

## 📋 目錄

1. [行為準則](#行為準則)
2. [我能貢獻什麼?](#我能貢獻什麼)
3. [開發環境設置](#開發環境設置)
4. [提交流程](#提交流程)
5. [代碼風格](#代碼風格)
6. [測試要求](#測試要求)
7. [問題回報](#問題回報)

---

## 行為準則

### 我們的承諾

為了營造開放且友善的環境,我們承諾:

- ✅ 尊重不同的觀點與經驗
- ✅ 優雅地接受建設性批評
- ✅ 專注於對社群最有利的事情
- ❌ 不使用性化語言或圖像
- ❌ 不進行人身攻擊或政治攻擊
- ❌ 不騷擾他人

### 執行

違反行為準則的行為可向 [contact@monacelium.org](mailto:contact@monacelium.org) 回報。

---

## 我能貢獻什麼?

### 🐛 回報 Bug

發現問題?請[開啟 Issue](https://github.com/ilove307ok-cpu/Monacelium/issues/new) 並包含:
- 清晰的問題描述
- 重現步驟
- 預期行為 vs 實際行為
- 環境資訊 (OS、Python 版本、硬體)
- 相關截圖或日誌

### 💡 提出功能建議

有新想法?開啟 Issue 並標註 `enhancement`,說明:
- 功能目的與使用場景
- 可能的實作方式
- 是否願意協助開發

### 📖 改進文檔

發現文檔錯誤或不清楚?可以:
- 修正錯字或文法錯誤
- 補充使用範例
- 翻譯成其他語言
- 改善 README 或 API 文檔

### 🔧 提交代碼

參考下方的[開發環境設置](#開發環境設置)與[提交流程](#提交流程)。

---

## 開發環境設置

### 前置需求

- **Python**: 3.9+
- **Node.js**: 18+ (for tooling)
- **Git**: 2.30+
- **硬體** (選配): Raspberry Pi 5 + LoRa 模組

### 1. Fork 並 Clone 專案
```bash
# Fork 專案到你的 GitHub 帳號
# 然後 clone

git clone https://github.com/YOUR_USERNAME/Monacelium.git
cd Monacelium
```

### 2. 安裝依賴
```bash
# Python 依賴
pip install -r requirements.txt

# 安裝 Reticulum
pip install rns --break-system-packages

# (選配) 開發工具
pip install pytest black flake8 mypy
```

### 3. 創建開發分支
```bash
git checkout -b feature/your-feature-name
```

---

## 提交流程

### 1. 開發

- 遵循[代碼風格](#代碼風格)
- 為新功能添加測試
- 更新相關文檔

### 2. 測試
```bash
# 運行測試套件
pytest tests/

# 代碼格式檢查
black --check .
flake8 .

# 類型檢查
mypy src/
```

### 3. Commit

使用[語意化提交訊息](https://www.conventionalcommits.org/):
```bash
git commit -m "feat: 新增 DataDAO 自動聚合功能"
git commit -m "fix: 修正 LoRa 封包解析錯誤"
git commit -m "docs: 更新 API 參考文件"
```

**Commit 類型:**
- `feat`: 新功能
- `fix`: Bug 修復
- `docs`: 文檔更新
- `style`: 代碼格式 (不影響功能)
- `refactor`: 重構
- `test`: 測試相關
- `chore`: 建構工具或輔助工具

### 4. Push 並開啟 Pull Request
```bash
git push origin feature/your-feature-name
```

然後在 GitHub 上開啟 Pull Request,描述:
- 變更內容
- 相關 Issue 編號 (如 `Closes #123`)
- 測試方法
- 截圖 (如適用)

---

## 代碼風格

### Python

遵循 [PEP 8](https://peps.python.org/pep-0008/) 並使用工具自動格式化:
```bash
# 格式化代碼
black src/

# Lint 檢查
flake8 src/ --max-line-length=100
```

**範例:**
```python
# ✅ 好
def calculate_poc_score(node_id: str, epoch: int) -> float:
    """計算節點的 Proof of Contribution 分數。
    
    Args:
        node_id: 節點唯一識別碼
        epoch: 週期編號
        
    Returns:
        PoC 分數 (0.0-1.0)
    """
    pass

# ❌ 壞
def calc(n,e):  # 無類型註解、無 docstring
    pass
```

### Markdown

- 使用 ATX 風格標題 (`#` 而非底線)
- 列表項目前後空行
- 代碼區塊指定語言

---

## 測試要求

### 單元測試

所有新功能必須包含測試:
```python
# tests/test_poc.py
import pytest
from monacelium.poc import calculate_poc_score

def test_poc_score_basic():
    score = calculate_poc_score("node_123", epoch=1)
    assert 0.0 <= score <= 1.0

def test_poc_score_sybil_penalty():
    # 被標記為女巫攻擊的節點分數應大幅降低
    score = calculate_poc_score("sybil_node", epoch=1)
    assert score < 0.1
```

### 整合測試

硬體相關功能需在真實環境測試:
```bash
# 在 Raspberry Pi 5 上測試
python3 firmware/reticulum-test/test_node.py --mode announce
```

---

## 問題回報

### Bug Report Template

開啟 Issue 時請使用以下格式:
```markdown
### 描述
[清楚描述問題]

### 重現步驟
1. 執行 `python3 test_node.py`
2. 觀察輸出
3. 看到錯誤訊息

### 預期行為
應該顯示節點身份

### 實際行為
出現 `ModuleNotFoundError`

### 環境
- OS: Ubuntu 24.04
- Python: 3.11.2
- Reticulum: 0.7.8

### 額外資訊
[截圖或日誌]
```

---

## 社群資源

- **GitHub Issues**: [問題追蹤](https://github.com/ilove307ok-cpu/Monacelium/issues)
- **Discussions**: [社群討論](https://github.com/ilove307ok-cpu/Monacelium/discussions) (籌備中)
- **Discord**: [即時聊天](https://discord.gg/monacelium) (籌備中)
- **文檔**: [技術文檔](./docs/)

---

## 授權

提交代碼即表示同意你的貢獻採用專案的授權條款:
- 代碼: [MIT License](./LICENSE)
- 文檔: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 硬體: [CERN-OHL-S v2](https://ohwr.org/cern_ohl_s_v2.txt)

---

## 致謝

感謝所有貢獻者! 🎉

你的名字將出現在 [Contributors](https://github.com/ilove307ok-cpu/Monacelium/graphs/contributors) 列表中。

---

**有問題?** 隨時開啟 Issue 或聯繫維護團隊。

**最後更新:** 2026-04-02