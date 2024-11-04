from flask import Blueprint, request, jsonify
from ..services.user_service import UserService
from ..services.auth_service import AuthService

user_bp = Blueprint('user_bp', __name__)
auth_service = AuthService()

@user_bp.route("/users", methods=["GET"])
@auth_service.token_required
def get_users(current_user):
    # Once the user is authenticated, their information is passed into the decorated function
    # as the current_user argument.
    users = UserService.get_all_users()
    if users is None:
        return jsonify({'message': 'No users found'}), 404
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200 

@user_bp.route("/users", methods=["POST"])
@auth_service.token_required
def create_user(current_user):
    # Get data from the request body
    data = request.json
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_user = UserService.create_new_user(username, email)

    return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email}), 201