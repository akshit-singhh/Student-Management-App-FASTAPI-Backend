from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select, func
from typing import List
from models import Student
from database import get_session

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[Student])
def list_students(session: Session = Depends(get_session)):
    """List all students"""
    students = session.exec(select(Student)).all()
    return students


# ✅ Define before any route with /{student_id}
@router.get("/count")
def get_student_count(session: Session = Depends(get_session)):
    """Return total number of students"""
    total = session.exec(select(func.count()).select_from(Student)).one()
    return {"total_students": total}


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int, session: Session = Depends(get_session)):
    """Get a single student"""
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.post("/", response_model=Student)
def add_student(student: Student, session: Session = Depends(get_session)):
    """Add a new student"""
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, updated: Student, session: Session = Depends(get_session)):
    """Update an existing student"""
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = updated.name
    student.class_name = updated.class_name
    student.roll_no = updated.roll_no
    student.contact = updated.contact

    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@router.delete("/{student_id}")
def delete_student(student_id: int, session: Session = Depends(get_session)):
    """Delete a student"""
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    session.delete(student)
    session.commit()
    return {"success": True}
