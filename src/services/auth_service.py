from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from functools import wraps
from flask import jsonify
from ..models.user import User, db

class AuthService:
    def __init__(self, app=None):
        self.jwt = JWTManager(app)  # Initialize JWT Manager with the Flask app

    def generate_tokens(self, user):
        """
        Generate access and refresh tokens for the user.
        """
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return {'access_token': access_token, 'refresh_token': refresh_token}

    def token_required(self, f):
        @wraps(f)
        @jwt_required()  # This decorator ensures a valid JWT is present
        def decorated(*args, **kwargs):
            """
            Protect routes by requiring a valid JWT. Fetches current user and passes to route.
            """
            current_user_id = get_jwt_identity()
            current_user = db.session.get(User, current_user_id)

            if not current_user:
                return jsonify({'message': 'Invalid user!'}), 403

            return f(current_user, *args, **kwargs)

        return decorated
