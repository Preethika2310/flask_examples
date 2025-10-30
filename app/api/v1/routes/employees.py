from flask import Blueprint, request, jsonify
from app.api.v1.services.employees_services import (
    fetch_employees,
    create_employee,
    fetch_employee_by_id,
    edit_employee,
    delete_employee_by_id
)

employees_bp = Blueprint("employees", __name__)

@employees_bp.route('/', methods=['GET'])
def get_employees():
    fetch_list = fetch_employees()
    return jsonify(fetch_list), 200

@employees_bp.route('/', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = create_employee(data) 
    return jsonify(new_employee), 201

@employees_bp.route('/<int:id>', methods=['GET'])
def get_employee(id):
    employee = fetch_employee_by_id(id)
    if employee:
        return jsonify(employee), 200
    return jsonify({"error": "Employee not found"}), 404

@employees_bp.route('/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    updated_employee = edit_employee(id, data)
    if updated_employee:
        return jsonify(updated_employee), 200
    return jsonify({"error": "Employee not found"}), 404

@employees_bp.route('/<int:id>', methods=['DELETE'])
def delete_employee(id):
    success = delete_employee_by_id(id)
    if success:
        return jsonify({"message": f"Employee with id {id} deleted"}), 200
    return jsonify({"error": f"Employee with id {id} not found"}), 404
