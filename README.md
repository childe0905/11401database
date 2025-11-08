# 1141 Database

- 姓名：廖振廷  
- 學號：41271126H  
- 系級：科技116  

---

## 🧭 作業紀錄總覽
> 點擊每一項可展開詳細內容 👇  

---

<details>
<summary>📘 HW1：美食訂單系統 (Flask + MySQL)</summary>

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
</details>

---

<details>
<summary>📗 HW2：美食訂單系統進階版 (Flask + MySQL + CRUD 強化)</summary>

<img src="images/demo_hw2.png" alt="系統示範" width="500"> <img src="images/demo_hw2-2.png" alt="系統示範" width="500">

🎬 [HW2 示範影片（點我觀看）](https://youtu.be/jl4w44F1gVQ)

### 🧩 功能特色
| 功能 | 說明 |
|------|------|
| ➕ 新增訂單 | 儲存至資料庫 |
| ✏️ 修改訂單 | 更新內容 |
| ✅ 完成訂單 | 狀態轉為已完成 |
| 🗑 刪除訂單 | 移除資料 |
| 💰 營收統計 | 自動加總金額 |

### ⚙️ 專案結構
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
```
</details>

---

<details>
<summary>📙 HW3：學生成績管理系統 (Node.js + MongoDB + Render 部署)</summary>

#### 🖥 [線上展示網址](https://student-performance-mxq9.onrender.com)
#### 🧑‍💻[程式碼](https://github.com/childe0905/student-performance)
🎬 [HW3 示範影片（點我觀看）](https://youtu.be/gFxIUUu6Wcs)

<img src="images/demo_hw3.png" alt="系統示範" width="600">

### 🧩 功能特色
| 功能 | 說明 |
|------|------|
| ➕ 新增學生資料 | 可輸入多科成績 |
| 🔍 查詢學生成績 | 顯示與平均計算 |
| ✏️ 修改成績 | 直接編輯分數 |
| 🗑 刪除學生 | 移除學生紀錄 |
| 📋 學生清單 | 一覽所有學生 |

### 🧱 技術架構
| 類別 | 技術 |
|------|------|
| 前端 | HTML、Tailwind CSS |
| 後端 | Node.js、Express |
| 資料庫 | MongoDB Atlas |
| 部署平台 | Render |

</details>
