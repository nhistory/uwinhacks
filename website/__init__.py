"""Configurations"""
from flask import Flask
from .homepage import homepage
from .auth import auth

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'example'

    app.register_blueprint(homepage, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
