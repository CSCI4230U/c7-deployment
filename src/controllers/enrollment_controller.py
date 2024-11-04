from flask import jsonify, Blueprint, request
from ..services.enrollment_service import EnrollmentService
from src.services.auth_service import AuthService

enrollment_bp = Blueprint('enrollment', __name__)

auth_service = AuthService()

from unittest.mock import patch, MagicMock

@enrollment_bp.route('/enroll', methods=['POST'])   
@auth_service.token_required
def enroll_user(current_user):
    data = request.get_json()
    user_id = data.get('user_id')
    course_id = data.get('course_id')

    if not user_id or not course_id:
        return jsonify({'error': 'Invalid input'}), 400
    
    enrollment = EnrollmentService.enroll_user_in_course(user_id, course_id)
    
    return jsonify({'id': enrollment.id, 'user_id': enrollment.user_id, 'course_id': enrollment.course_id}), 201

@enrollment_bp.route('/enrollments/<int:user_id>', methods=['GET'])
@auth_service.token_required
def get_user_enrollments(current_user, user_id):
    enrollments = EnrollmentService.get_enrollments_for_user(user_id)
    return jsonify([{'id': enrollment.id, 'user_id': enrollment.user_id, 'course_id': enrollment.course_id} for enrollment in enrollments])

@enrollment_bp.route('/enrollments/<int:enrollment_id>', methods=['DELETE'])
@auth_service.token_required
def remove_enrollment(current_user, enrollment_id):
    EnrollmentService.remove_enrollment(enrollment_id)
    return jsonify({'message': 'Enrollment removed'}), 200