from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List

from models import Admin
from database import get_session

router = APIRouter(prefix="/admins", tags=["Admins"])

# ---------------- Admin Endpoints ---------------- #

@router.get("/", response_model=List[Admin])
def list_admins(session: Session = Depends(get_session)):
    """List all admins"""
    admins = session.exec(select(Admin)).all()
    return admins


@router.post("/", response_model=Admin)
def add_admin(admin: Admin, session: Session = Depends(get_session)):
    """Add new admin"""
    existing_admin = session.exec(select(Admin).where(Admin.email == admin.email)).first()
    if existing_admin:
        raise HTTPException(status_code=400, detail="Admin with this email already exists")
    session.add(admin)
    session.commit()
    session.refresh(admin)
    return admin


@router.put("/{admin_id}")
def update_admin(admin_id: int, updated: Admin, session: Session = Depends(get_session)):
    admin = session.get(Admin, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    admin.name = updated.name
    admin.email = updated.email
    admin.password = updated.password
    session.add(admin)
    session.commit()
    session.refresh(admin)

    return {"success": True, "message": "Admin updated successfully"}


@router.delete("/{admin_id}")
def delete_admin(admin_id: int, session: Session = Depends(get_session)):
    """Delete an admin"""
    admin = session.get(Admin, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    session.delete(admin)
    session.commit()
    return {"success": True, "message": "Admin deleted successfully"}
