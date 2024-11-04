from ..models.user import User
from ..extensions import db
# from flask import jsonify, abort

class UserService:

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return users

    @staticmethod
    def create_new_user(username, email):

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return new_user
