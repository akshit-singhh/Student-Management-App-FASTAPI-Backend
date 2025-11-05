from fastapi import FastAPI, HTTPException, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, select, Session
from database import engine, get_session
from models import Admin
from admin import router as admin_router
from student import router as student_router

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
SQLModel.metadata.create_all(engine)

# Register routers
app.include_router(admin_router)
app.include_router(student_router)

# ---------- Login Endpoint ----------
@app.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session)
):
    admin = session.exec(
        select(Admin).where(Admin.email == email, Admin.password == password)
    ).first()

    if admin:
        return {
            "success": True,
            "role": "admin",
            "message": "Login successful",
            "admin_id": admin.id,
            "name": admin.name
        }

    raise HTTPException(status_code=401, detail="Invalid email or password")
