# Django Bookstore Platform

本專案是以 Django 框架開發的全功能電商書店平台，涵蓋商品瀏覽、購物車管理、訂單建立、Email 通知及 PayPal 金流串接等完整購物流程。

---

## 目錄

- [專案簡介](#專案簡介)
- [功能特色](#功能特色)
- [技術棧](#技術棧)
- [專案結構](#專案結構)
- [安裝與啟動](#安裝與啟動)
- [使用說明](#使用說明)
- [URL 路由對照表](#url-路由對照表)
- [資料庫模型](#資料庫模型)
- [畫面截圖](#畫面截圖)
- [備註](#備註)

---

## 專案簡介

本專案以 **Python Django** 框架開發，實作一個具備完整電商購物流程的 **Django Bookstore Platform**。系統架構採用 Django 的 MVT（Model-View-Template）設計模式，將商品展示、購物車、訂單管理與金流付款各自拆分為獨立的 Django App，維持高度的模組化與可維護性。

### 系統目標

- 提供使用者友善的商品瀏覽介面，支援依分類篩選商品
- 實作基於 Django Session 的購物車機制，無需登入即可使用
- 完整的結帳流程，從填寫收件資訊到產生訂單一氣呵成
- 整合 PayPal 沙盒（Sandbox）金流，模擬真實付款情境
- 訂單建立後自動觸發 Email 確認通知，提升使用者體驗
- 透過 Django Admin 後台提供管理員完整的商品與訂單管理能力

### 開發背景

本系統以書店作為主題情境，將電子商務系統開發中常見的核心功能整合於單一專案之中，涵蓋前後端模板渲染、資料庫設計、Session 狀態管理、第三方金流串接與後台管理系統等技術，適合作為 Django Web 應用開發的完整實作參考。

---

## 功能特色

-  **商品目錄** — 瀏覽所有商品，支援依分類篩選
-  **商品詳細頁** — 查看商品資訊，可直接加入購物車
-  **購物車管理** — 基於 Session 的購物車，支援數量修改與刪除
-  **訂單建立** — 填寫收件人資料後送出訂單
-  **Email 通知** — 訂單成立後自動發送確認信給買家
-  **PayPal 金流** — 整合 PayPal 沙盒進行測試付款
-  **後台管理** — 透過 Django Admin 管理商品、分類與訂單

---

## 技術棧

| 類別 | 技術 |
|---|---|
| 後端框架 | Django |
| 資料庫 | SQLite3 |
| 前端 | Bootstrap 3、jQuery 1.12、Font Awesome 4.7 |
| 金流串接 | django-paypal（PayPal 沙盒測試模式）|
| 圖片處理 | Pillow |
| 模板引擎 | Django Template Language（DTL）|

---

## 專案結構

```
bookshop/
├── django_shop_tutorial/       # 專案設定
│   ├── settings.py             # 全域設定（資料庫、Email、PayPal、靜態檔案）
│   ├── urls.py                 # 根路由設定
│   └── wsgi.py
│
├── shop/                       # 商品展示 App
│   ├── models.py               # Category、Product 模型
│   ├── views.py                # 商品列表與詳細頁 View
│   ├── admin.py                # Admin 後台設定
│   ├── urls.py                 # 商品相關路由
│   └── templates/shop/
│       ├── base.html           # 共用版型（含導覽列與購物車小工具）
│       └── product/
│           ├── list.html       # 商品列表頁
│           └── detail.html     # 商品詳細頁
│
├── cart/                       # 購物車 App
│   ├── cart.py                 # Cart 類別（Session 儲存）
│   ├── context_processors.py   # 將購物車注入所有模板
│   ├── views.py                # 加入、移除、查看購物車 View
│   ├── forms.py                # 加入購物車表單
│   └── templates/cart/
│       └── detail.html         # 購物車詳細頁
│
├── orders/                     # 訂單管理 App
│   ├── models.py               # Order、OrderItem 模型
│   ├── views.py                # 訂單建立 View
│   ├── forms.py                # 訂單表單
│   ├── task.py                 # 訂單成立後發送 Email
│   ├── admin.py                # 訂單後台（含 Inline 訂單項目）
│   └── templates/orders/order/
│       └── create.html         # 結帳表單頁
│
├── payment/                    # 金流付款 App
│   ├── views.py                # 付款流程 View
│   └── templates/payment/
│       └── process.html        # PayPal 付款頁
│
├── media/                      # 商品圖片上傳目錄
├── db.sqlite3                  # SQLite 資料庫檔案
└── requirements.txt            # Python 套件清單
```

---

## 安裝與啟動

### 環境需求

- Python 3.8 以上
- pip

### 安裝步驟

**1. 複製專案**

```bash
git clone <your-repository-url>
cd bookshop
```

**2. 建立並啟用虛擬環境**

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. 安裝所需套件**

```bash
pip install -r requirements.txt
```

**4. 執行資料庫遷移**

```bash
python manage.py migrate
```

**5. 建立管理員帳號**

```bash
python manage.py createsuperuser
```

**6. 啟動開發伺服器**

```bash
python manage.py runserver
```

**7. 開啟瀏覽器**

```
http://127.0.0.1:8000/
```

---

## 使用說明

### 後台管理

前往 `http://127.0.0.1:8000/admin/` 登入 Django 後台，可執行以下操作：
- 新增／編輯 **商品分類** 與 **商品**
- 查看與管理 **訂單**
- 上傳商品圖片

### 購物流程

```
瀏覽商品  →  加入購物車  →  查看購物車  →  建立訂單  →  PayPal 付款
   /             /cart/         /cart/        /orders/    /payment/process/
```

---

## URL 路由對照表

| URL 路徑 | View 函式 | 說明 |
|---|---|---|
| `/` | `product_list` | 首頁，顯示所有商品 |
| `/<分類-slug>/` | `product_list_by_category` | 依分類篩選商品 |
| `/<id>/<slug>/` | `product_detail` | 商品詳細頁 |
| `/cart/` | `cart_detail` | 購物車頁面 |
| `/cart/add/<id>/` | `cart_add` | 加入商品至購物車（POST）|
| `/cart/remove/<id>/` | `cart_remove` | 從購物車移除商品 |
| `/orders/` | `order_create` | 建立訂單（結帳）|
| `/payment/process/` | `payment_process` | PayPal 付款流程 |
| `/admin/` | Django Admin | 後台管理介面 |

---

## 資料庫模型

### `shop` App

```
Category（商品分類）
├── name        CharField       商品分類名稱
└── slug        SlugField       URL 用識別碼（唯一值）

Product（商品）
├── category    ForeignKey → Category  所屬分類
├── name        CharField              商品名稱
├── slug        SlugField              URL 用識別碼
├── image       ImageField             商品圖片
├── description TextField             商品描述
├── price       DecimalField          價格
├── stock       PositiveIntegerField  庫存數量
├── available   BooleanField          是否上架
├── created     DateTimeField         建立時間（自動）
└── updated     DateTimeField         更新時間（自動）
```

### `orders` App

```
Order（訂單）
├── first_name  CharField       買家名字
├── last_name   CharField       買家姓氏
├── email       EmailField      電子郵件
├── address     CharField       收件地址
├── postal_code CharField       郵遞區號
├── city        CharField       城市
├── paid        BooleanField    是否已付款
├── created     DateTimeField   建立時間（自動）
└── updated     DateTimeField   更新時間（自動）

OrderItem（訂單項目）
├── order       ForeignKey → Order    所屬訂單
├── product     ForeignKey → Product  商品
├── price       DecimalField          當時購買價格
└── quantity    PositiveIntegerField  購買數量
```

---

## 畫面截圖

> _請在此處補充商品列表頁、購物車、結帳表單及付款頁面的截圖。_

---

## 備註

- **Email 後端** 設定為 `console` 模式，訂單確認信會輸出至終端機而非實際寄出。
- **PayPal** 透過 `PAYPAL_TEST = True` 設定為沙盒（測試）模式，不會產生真實交易。
- 商品圖片上傳路徑為 `media/products/<年>/<月>/<日>/`。

