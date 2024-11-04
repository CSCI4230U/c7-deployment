from ..models.course import Course
from ..extensions import db
from flask import jsonify, abort

class CourseService:

    @staticmethod
    def get_all_courses():
        courses = Course.query.all()
        return courses

    @staticmethod
    def create_new_course(data):
        
        new_course = Course(name=data['name'], description=data['description'])
        db.session.add(new_course)
        db.session.commit()

        return new_course
