# 🖥️ Student Management Backend — FastAPI (V1.0)

Backend API for the Student Management App, built using Python FastAPI.  
Provides CRUD operations for students, admin profile management, and handles authentication for the Android app.

**App GitHub Repo:** [Student Management App](https://github.com/akshit-singhh/Student-Management-App)

---

## ✨ Features

| Feature                  | Description                                 |
|--------------------------|---------------------------------------------|
| 👤 Admin Authentication  | Secure login and profile management.       |
| 🏫 Student CRUD          | Add, update, view, and delete student records. |
| 🔒 Session Handling      | Token-based authentication for API calls. |
| ⚡ REST API              | Provides endpoints consumed by Android app. |
| 🐍 FastAPI + MySQL      | Lightweight, high-performance backend.    |

---

## 🧠 Tech Stack

- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Database:** MySQL (default, can use PostgreSQL)
- **ORM:** SQLAlchemy
- **Authentication:** JWT / Token-based

---

## 📦 Setup Guide

### ✅ Step 1 — Clone Repository
```bash
git clone https://github.com/akshit-singhh/student-management-backend.git
cd student-management-backend
```

## ✅ Step 2 — Create Virtual Environment
```
python -m venv venv
source venv/bin/activate       # Linux / Mac
venv\Scripts\activate          # Windows
```

## ✅ Step 3 — Install Dependencies
```
pip install -r requirements.txt
```
- Dependencies include:
- fastapi → Web framework
- uvicorn → ASGI server
- sqlalchemy → ORM
- pydantic → Data validation

## ✅ Step 4 — Database Setup (MySQL)

1. Install MySQL and create a database for the project:
2. Update the .env file in the backend project root with your MySQL credentials:

## 5️⃣ Run the Backend
```
uvicorn main:app --reload
```
- The API will be available at: http://127.0.0.1:8000
- SQLModel will automatically create tables if you have something like:
```
from sqlmodel import SQLModel, create_engine
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

```
If using mobile app-
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
This will host on local

🛠️ API Endpoints
Endpoint	Method	Description
| Endpoint         | Method    | Description                 |
| ---------------- | --------- | --------------------------- |
| `/login`         | POST      | Admin login                 |
| `/admin/profile` | GET / PUT | View / update admin profile |
| `/students`      | GET       | List all students           |
| `/students`      | POST      | Add a new student           |
| `/students/{id}` | GET       | Get student by ID           |
| `/students/{id}` | PUT       | Update student by ID        |
| `/students/{id}` | DELETE    | Delete student by ID        |


## ⚠️ Notes
Ensure MySQL server is running before starting the backend.
```
pip install pymysql
```

## 🚀 Connecting to Android App

- Update API base URL in Android project (ApiClient.kt) to match your backend IP/port.
- Make sure device/emulator and backend are on the same network.
 -Test /login endpoint first to validate connectivity.

## 👨‍💻 Developer Info

- Developed by Akshit Singh
- GitHub: @akshit-singhh
- Email: akshitsingh658@gmail.com
- LinkedIn: linkedin.com/in/akshit-singhh

## ⭐ Support

If you find this project helpful, star this repository 🌟 and share your feedback or improvements!
