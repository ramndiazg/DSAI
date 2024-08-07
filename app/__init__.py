from flask import Flask
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

    jwt = JWTManager(app)

    client = MongoClient(app.config['MONGO_URI'])
    app.db = client.get_default_database()

    with app.app_context():
        from . import routes
        from . import auth
        from . import chatbot

        app.register_blueprint(auth.auth_bp, url_prefix='/auth')
        app.register_blueprint(chatbot.chatbot_bp, url_prefix='/chatbot')
        app.register_blueprint(routes.courses_bp, url_prefix='/courses')

    return app
