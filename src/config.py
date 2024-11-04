import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///advwebdev.db'  # Or another DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
