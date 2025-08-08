from flask import Blueprint, request, jsonify
from controllers.math_controller import process_operation, get_logs 
from flask_jwt_extended import create_access_token, jwt_required


#"blueprint"- mini-aplicatie Flask modulara
math_blueprint = Blueprint('math', __name__)

@math_blueprint.route("/api/<operation>", methods=["POST"])
def handle_operation(operation):
    try:
        data = request.get_json()  # preia datele din body (JSON->dict)
        result = process_operation(operation, data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#Autentificare JWT(hardcodata)
@math_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "password":
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

#Endpoint pentru vizualizarea logurilor
@math_blueprint.route("/logs", methods=["GET"])
@jwt_required()
def logs_route():
    return get_logs()
