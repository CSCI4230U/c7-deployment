from ..extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class Course(db.Model):
    __tablename__ = 'course'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    
    enrollments: Mapped[list["Enrollment"]] = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")