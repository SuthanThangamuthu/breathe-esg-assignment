# 🌱 Breathe ESG Assignment

## 🚀 Live API

🔗 https://breathe-esg-assignment-pgdv.onrender.com/api/upload/

---

# 📌 Project Overview

This project is a full-stack ESG Emissions Management application developed for the **Breathe ESG Assignment**.

The application allows users to:

✅ Upload ESG emissions CSV files
✅ Process and validate emission records
✅ Store emissions data in database
✅ Manage records using Django Admin
✅ Access APIs through REST endpoints
✅ Connect frontend and backend seamlessly

---

# 🛠️ Tech Stack

## 🎨 Frontend

* ⚛️ React JS
* 📡 Axios
* 🎨 CSS

---

## ⚙️ Backend

* 🐍 Python
* 🌐 Django
* ⚡ Django REST Framework

---

## 🗄️ Database

* 💾 SQLite

---

## ☁️ Deployment & Tools

* 🚀 Render (Backend Deployment)
* ▲ Vercel (Frontend Deployment)
* 📮 Postman (API Testing)
* 🧑‍💻 Git & GitHub

---

# ✨ Features

✅ CSV File Upload API
✅ ESG Emissions Data Processing
✅ REST API Integration
✅ Database Storage
✅ Django Admin Panel
✅ API Testing with Postman
✅ Cloud Deployment

---

# 📂 Project Structure

```text id="ps1"
BREATHE-ESG-ASSIGNMENT
│
├── backend
│   ├── config
│   ├── emissions
│   ├── manage.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── docs
│
├── runtime.txt
└── README.md
```

---

# 📡 API Endpoint

## 📤 Upload Emissions CSV

### Endpoint

```text id="ps2"
POST /api/upload/
```

### 🔗 Production URL

```text id="ps3"
https://breathe-esg-assignment-pgdv.onrender.com/api/upload/
```

---

# 📥 Form Data Parameters

| Key             | Type |
| --------------- | ---- |
| 📄 file         | File |
| 🏢 company_name | Text |
| ⚡ source_type  | Text |

---

# 🧪 API Testing

Tested successfully using **Postman**.

### Sample Values

```text id="ps4"
company_name = Tesla
source_type = Electricity
```

Upload:

```text id="ps5"
emissions.csv
```

---

# 💻 Run Locally

## Backend Setup

```bash id="ps6"
cd backend

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Frontend Setup

```bash id="ps7"
cd frontend

npm install

npm start
```

---

# 🔐 Admin Panel

🔗 https://breathe-esg-assignment-pgdv.onrender.com/admin/

---

# ☁️ Deployment

## 🚀 Backend Deployment

* Render

## ▲ Frontend Deployment

* Vercel

---

# 👨‍💻 Developed By

### Suthan T
