import sys

from flask import Flask
from .extensions import db, migrate
from .config import Config
from flask_jwt_extended import JWTManager

from .controllers.auth_controller import auth_bp
from .controllers.user_controller import user_bp
from .controllers.course_controller import course_bp
from .controllers.enrollment_controller import enrollment_bp

def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config.from_object(Config)  # Load configuration from Config class

    if test_config:
        app.config.update(test_config)  # Override with test-specific config

    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI    
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Initialize JWT manager
    jwt = JWTManager(app)

    # Register the blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)  
    app.register_blueprint(course_bp)
    app.register_blueprint(enrollment_bp)

    return app