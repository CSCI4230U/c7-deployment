from flask import Blueprint, request, jsonify, abort
from ..models.user import User
from ..services.auth_service import AuthService  # Import the AuthManager class

auth_bp = Blueprint('auth_bp', __name__)

auth_manager = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    # Logic for logging in a user and generating tokens
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    print(f'username: {username}, email: {email}')

    # Authenticate the user
    # TODO: sanitize the input before querying the database
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    tokens = auth_manager.generate_tokens(user)

    return jsonify(tokens), 200


# # User login route to generate a JWT token
# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     if not data or not data.get('username') or not data.get('email'):
#         abort(400, 'Invalid credentials')

#     # database lookup
#     user = User.query.filter_by(username=data['username'], email=data['email']).first()
#     if not user:
#         abort(401, 'User not found')

#     # Generate a JWT token for the user
#     token = generate_token(user)

#     return jsonify({'token': token})
