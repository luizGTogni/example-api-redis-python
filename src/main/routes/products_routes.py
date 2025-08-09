from flask import Blueprint, request, jsonify
from src.types.http.http_request import HttpRequest
from src.main.composer.product_creator_composer import product_creator_composer
from src.main.composer.product_finder_composer import product_finder_composer
from src.errors.errors_handler import handle_error

products_routes_bp = Blueprint("products_routes", __name__)

@products_routes_bp.route("/products", methods=["POST"])
def create_product():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = product_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def find_product(product_name):
    try:
        http_request = HttpRequest(params={ "name": product_name })
        http_response = product_finder_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
