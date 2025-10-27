# 1141 Database

- 姓名：廖振廷  
- 學號：41271126H  
- 系級：科技116  

---

## HW1:  美食訂單系統 (Flask + MySQL)

<img src="images/demo.png" alt="系統示範" width="600">

🎥 [HW1 影片連結（點我觀看）](https://youtu.be/WG6yLcLKp0M)

---

### 🧩 功能特色

- 新增訂單  
- 修改訂單  
- 刪除訂單  
- 顯示訂單紀錄  
- 自動計算總營收  

---

### 🧱 技術架構

| 類別 | 技術 |
|------|------|
| 前端 | HTML、CSS、Jinja2 |
| 後端 | Flask (Python) |
| 資料庫 | MySQL |
| 工具 | MySQL Workbench、VS Code |

---

### ⚙️ 安裝與執行步驟

```bash
# 1️⃣ 下載專案
git clone https://github.com/childe0905/11401database.git
cd food_order_system

# 2️⃣ 建立虛擬環境
python3 -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

# 3️⃣ 安裝套件
pip install -r requirements.txt

# 4️⃣ 啟動伺服器
python app.py
```
## HW2:  美食訂單系統進階版 (Flask + MySQL + CRUD 強化)

> 第二次作業延伸自 HW1，新增完整 CRUD 功能與資料庫關聯操作。  
> 使用 Flask + MySQL 實作，讓使用者可以管理訂單、更新狀態與查詢統計。

---

 🎥 系統示範

<img src="images/demo_hw2.png" alt="系統示範" width="500"> <img src="images/demo_hw2-2.png" alt="系統示範" width="500">

🎬 [HW2 示範影片（點我觀看）](https://youtu.be/jl4w44F1gVQ)

---

### 🧭 系統簡介

此系統為 HW1 的升級版本，  
除了保留基本的新增、修改、刪除訂單外，  
還加入「訂單狀態管理」與「使用者登入系統」，  
實現真正的 CRUD（Create / Read / Update / Delete）功能。

---

### 🧩 功能特色

| 功能 | 說明 |
|------|------|
| ➕ 新增訂單 (Create) | 使用者可輸入客人姓名、餐點、數量等資訊並儲存至資料庫 |
| 📋 顯示訂單 (Read) | 顯示所有訂單紀錄，可依時間或狀態排序 |
| ✏️ 修改訂單 (Update) | 點擊「編輯」按鈕即可更新訂單內容 |
| ✅ 完成訂單 (Update) | 點擊「完成」自動將狀態改為「已完成」 |
| 🗑 刪除訂單 (Delete) | 可移除不需要的訂單資料 |
| 💰 營收統計 | 自動計算所有訂單金額總和 |

---

### 🧱 專案結構

```bash
food_order_system_v2/
├── app.py                # Flask 主程式
├── templates/
│   ├── index.html        # 主頁面（顯示與新增訂單）
│   ├── edit.html         # 編輯訂單頁面
│   └── login.html        # 登入/註冊頁面（選用）
├── static/
│   └── styles.css        # CSS 樣式
├── requirements.txt      # 套件清單
└── README_HW2.md         # 此說明文件
