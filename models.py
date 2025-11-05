from typing import Optional

from sqlmodel import SQLModel, Field

class Admin(SQLModel, table=True):
    __tablename__ = "admin"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str


class Student(SQLModel, table=True):
    __tablename__ = "student"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    class_name: str
    roll_no: str
    contact: str
