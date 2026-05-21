# 以AI為基礎動態預測飛機滑行碰撞預防系統

**Dynamic AI-based Predictive Flight Taxiing Collision Avoidance System**

國立雲林科技大學 資訊工程系 ｜ 指導教授：張本杰 特聘教授 ｜ 2022/12 – 2023/11

---

## 系統概述

飛機在機場地面滑行時，主要依賴塔台人員指揮與機長目視，容易因疏失造成擦撞事故（如 2023/06 日本羽田機場事件）。本系統透過接收 ADS-B 訊號取得即時飛機資料，利用分散式雲端系統儲存與處理，並以演算法判斷碰撞風險，在碰撞發生前 **40～50 秒**提前發出警告。

## 系統架構

```
ADS-B 天線 (1090MHz)
    │
    ▼
ADS-B 解碼器 ──► HBase (NoSQL) ──► MapReduce（過濾地面飛機）
                                          │
                                          ▼
                               Python 主程式 (main.py)
                               ├── SAT 演算法（機身多邊形碰撞偵測）
                               ├── TTC 計算（碰撞時間）
                               └── 三圈警戒（綠 834m / 黃 500m / 紅 276m）
                                          │
                              ┌───────────┴───────────┐
                              ▼                       ▼
                   OpenStreetMap 網頁監控        LINE Notify 警報
                   (web/osmmap.html)
```

## 技術棧

- **後端**：Python 3、Flask、happybase
- **雲端**：Apache Hadoop 3 + HDFS、HBase 2、MapReduce
- **演算法**：SAT (Separating Axis Theorem)、TTC (Time-To-Collision)、Haversine 公式
- **前端**：Leaflet.js、OpenStreetMap
- **通知**：LINE Notify API
- **資料來源**：ADS-B (Automatic Dependent Surveillance-Broadcast)、FlightAware AeroAPI

## 專案結構

```
airplane-collision-avoidance/
├── core/
│   ├── main.py        # 主程式：從 HBase 讀取飛機資料，進行碰撞偵測
│   └── server.py      # Flask API：提供飛機狀態給網頁前端
├── web/
│   └── osmmap.html    # 網頁監控地圖（Leaflet + OpenStreetMap）
├── demo/
│   ├── demo_haneda_v1.py   # 模擬羽田事件（10架）
│   ├── demo_haneda_v2.py   # 模擬羽田事件（19架，完整版）
│   ├── demo_taoyuan.py     # 桃園機場實測場景
│   └── README.md
├── docs/
│   ├── 專題報告.pdf
│   └── 專題海報.pdf
├── .env.example       # 環境變數範本
├── .gitignore
└── requirements.txt
```

## 安裝與執行

### 前置需求

- Python 3.8+
- 運作中的 **HBase 叢集**（需要 Ubuntu 私有雲環境）
- LINE Notify Token
- FlightAware AeroAPI 金鑰（選用，用於查詢航班資訊）

### 安裝步驟

```bash
git clone https://github.com/your-username/airplane-collision-avoidance.git
cd airplane-collision-avoidance

pip install -r requirements.txt

# 設定環境變數
cp .env.example .env
# 編輯 .env，填入 HBASE_HOST、LINE_TOKEN 等
```

### 執行

```bash
# 1. 啟動碰撞偵測主程式
python core/main.py

# 2. 另開終端啟動 Flask API（供網頁前端呼叫）
python core/server.py

# 3. 開啟 web/osmmap.html 查看即時監控地圖

# 4. （選用）執行模擬 demo
python demo/demo_haneda_v2.py
```

> **注意**：本系統核心功能需要 Hadoop + HBase 私有雲環境。
> 若只想查看前端介面，可直接開啟 `web/osmmap.html`（無資料狀態）。

## 研究成果

- 實際前往**桃園國際機場**部署測試，確認系統可正確偵測真實 ADS-B 訊號
- 成功重現 **2023/06/10 羽田機場 TG-683 × BR-189 擦撞事件**，系統在碰撞前 43 秒發出紅色警告
- 參加雲科大資工系大學部專題競賽

## 作者

- 莊哲綸 (Che-Lun Chuang)
- 邱忠憲 (Chung-Hsien Chiu)
- 詹閔勝 (Min-Sheng Chan)

指導教授：張本杰 特聘教授（國立雲林科技大學資訊工程系）
