import pytest
from src.app import create_app
from src.extensions import db
from src.models.user import User
from flask_jwt_extended import create_access_token

@pytest.fixture
def app():
    app = create_app()

    # Configure the app to use an in-memory SQLite database for tests
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()  # Create all the tables

    yield app

    # Teardown: drop all tables after test
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def seed_user(app):
    """
    Fixture to seed the database with a user and generate a JWT token.
    """
    with app.app_context():
        # Create the user object
        user = User(username="john_doe", email="john@example.com")
        
        # Add the user to the session and commit to the database
        db.session.add(user)
        db.session.commit()
        
        # Generate JWT access token for the user
        access_token = create_access_token(identity=user.id)
        
        # Return the user object and the token
        return user, access_token
