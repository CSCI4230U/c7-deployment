from ..extensions import db
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    id: Mapped[int] = mapped_column(primary_key=True)
   
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    course_id: Mapped[int] = mapped_column(db.ForeignKey('course.id'))

    enrollment_date: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=datetime.utcnow)

    user: Mapped["User"] = relationship('User', back_populates='enrollments')
    course: Mapped["Course"] = relationship('Course', back_populates='enrollments')