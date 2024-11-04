from ..models.enrollment import Enrollment
from ..extensions import db

class EnrollmentService:

    @staticmethod
    def enroll_user_in_course(user_id, course_id):
        enrollment = Enrollment(user_id=user_id, course_id=course_id)
        db.session.add(enrollment)
        db.session.commit()
        return enrollment
    
    @staticmethod
    def get_enrollments_for_user(user_id):
        return Enrollment.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def remove_enrollment(enrollment_id):
        enrollment = Enrollment.query.get(enrollment_id)
        if enrollment:
            db.session.delete(enrollment)
            db.session.commit()