from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = {
        "username": data['username'],
        "password": data['password']
    }
    current_app.db.users.insert_one(user)
    return jsonify(message="User registered successfully"), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = current_app.db.users.find_one({"username": data['username']})
    if user and user['password'] == data['password']:
        access_token = create_access_token(identity=data['username'])
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401
