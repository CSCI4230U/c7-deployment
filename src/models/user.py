from ..extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    enrollments: Mapped[list["Enrollment"]] = relationship("Enrollment", back_populates="user", cascade="all, delete-orphan")
