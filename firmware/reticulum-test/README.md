\# Reticulum 測試網節點



最小可行實現 (MVP),驗證 Monacelium 的 Reticulum Mesh 通訊可行性。



\## 快速開始



\### 1. 安裝依賴

```bash

pip install rns --break-system-packages

```



\### 2. 運行測試節點



\*\*節點 A (廣播模式):\*\*

```bash

python3 test\_node.py --mode announce

```



\*\*節點 B (監聽模式):\*\*

```bash

python3 test\_node.py --mode listen

```



\## 預期輸出



\### 節點 A (announce):

```

============================================================

Monacelium Reticulum 測試節點 v0.1

============================================================



\[Monacelium] 正在初始化 Reticulum Network Stack...

\[Monacelium] 節點身份: 3b2a8f9e1c4d

\[Monacelium] 公鑰: a1b2c3d4e5f6...

\[Monacelium] Destination 已建立: 7f8e9d0c1b2a

\[Monacelium] 模式: announce

\------------------------------------------------------------

```



\## 硬體需求



\- \*\*開發測試\*\*: 無需硬體,Reticulum 會自動使用 UDP 介面模擬

\- \*\*實際部署\*\*: SX1262 LoRa 模組 (915MHz / 868MHz)



\## 故障排除



\### 錯誤: ModuleNotFoundError: No module named 'RNS'

```bash

pip install rns --break-system-packages

```



\## 技術說明



此腳本展示:

\- ✅ Reticulum Identity (身份管理)

\- ✅ Destination (通訊端點)

\- ✅ Announce (節點廣播)

\- ✅ Packet 收發

\- ⏳ LoRa 硬體整合 (待硬體到位)



\---



\*\*版本:\*\* v0.1 | \*\*狀態:\*\* 開發中 | \*\*授權:\*\* MIT

