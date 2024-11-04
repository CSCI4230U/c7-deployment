from flask import Blueprint, request, jsonify
from ..services.course_service import CourseService
from ..services.auth_service import AuthService

course_bp = Blueprint('course_bp', __name__)

auth_service = AuthService()

@course_bp.route("/courses", methods=["GET"])
@auth_service.token_required
def get_courses(current_user):
    courses = CourseService.get_all_courses()
    # Ensure that courses is an iterable or handle None
    if courses is None:
        return jsonify({'message': 'No courses found'}), 404
    # Return the list of courses
    return jsonify([{
        'id': course.id,
        'name': course.name,
        'description': course.description
    } for course in courses]), 200
    
@course_bp.route("/courses", methods=["POST"])
@auth_service.token_required
def create_course(current_user):
    data = request.json
    name = data.get('name')
    description = data.get('description')

    if not name or not description:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_course = CourseService.create_new_course(name, description)

    return jsonify({'id': new_course.id, 'name': new_course.name, 'description': new_course.description}), 201