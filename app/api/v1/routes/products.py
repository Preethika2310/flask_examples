from flask import Blueprint, request, jsonify
from app.api.v1.services.products_services import (
    fetch_products,
    add_product,
    get_product_by_id,
    update_product,
    delete_product
)

products_bp = Blueprint("products", __name__)  

@products_bp.route('/', methods=['GET'])
def get_products():
    fetch_list = fetch_products()
    return jsonify(fetch_list), 200

@products_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = add_product(data)
    return jsonify(new_product), 201

@products_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = get_product_by_id(id)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404


@products_bp.route('/<int:id>', methods=['PUT'])
def updates_product(id):
     data = request.get_json()
     updated_product = update_product(id, data)
     if updated_product:
         return jsonify(updated_product), 200
     return jsonify({"error": "Product not found"}), 404

@products_bp.route('/<int:id>', methods=['DELETE'])
def deletes_product(id):
    success = delete_product(id)
    if success:
        return jsonify({"message": f"Product with id {id} deleted"}), 200
    return jsonify({"error": f"Product with id {id} not found"}), 404
