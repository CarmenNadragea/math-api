from flask import Blueprint, request, jsonify
from controllers.math_controller import process_operation


# Creăm un "blueprint" – o mini-aplicație Flask modulară
math_blueprint = Blueprint('math', __name__)


@math_blueprint.route("/api/<operation>", methods=["POST"])
def handle_operation(operation):
    try:
        data = request.get_json()  # preia datele din body (JSON → dict)
        result = process_operation(operation, data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
