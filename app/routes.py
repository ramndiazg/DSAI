from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/classes', methods=['GET'])
@jwt_required()
def get_classes():
    classes = current_app.db.classes.find()
    return jsonify([cls for cls in classes])

@courses_bp.route('/class/<id>', methods=['GET'])
@jwt_required()
def get_class(id):
    cls = current_app.db.classes.find_one({"_id": ObjectId(id)})
    return jsonify(cls)

@courses_bp.route('/class', methods=['POST'])
@jwt_required()
def add_class():
    data = request.get_json()
    current_app.db.classes.insert_one(data)
    return jsonify(message="Class added successfully"), 201

@courses_bp.route('/class/<id>/exam', methods=['POST'])
@jwt_required()
def submit_exam(id):
    data = request.get_json()
    # crear el examenluego
    return jsonify(message="Exam submitted successfully"), 200
