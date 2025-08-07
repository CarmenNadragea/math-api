from flask import jsonify
from models.request_log import RequestLog
from models.request_schema import PowerRequest, FactorialRequest, FibonacciRequest
from services.fibonacci_service import fibonacci
from services.factorial_service import factorial
from services.power_service import calculate_power
from database import db
from log_producer import send_log


def process_operation(operation: str, input_data: dict) -> dict:
    if operation == "power":
        result = calculate_power(input_data["base"], input_data["exponent"])
    elif operation == "factorial":
        result = factorial(input_data["number"])
    elif operation == "fibonacci":
        result = fibonacci(input_data["number"])
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    # Trimite logul catre Kafka
    send_log({
        "operation": operation,
        "input": input_data,
        "result": result
    })

    return {"result": result}


def get_logs():
    logs = RequestLog.query.order_by(RequestLog.timestamp.desc()).all()
    result = []

    for log in logs:
        result.append({
            "id": log.id,
            "operation": log.operation,
            "input": log.input,
            "result": log.result,
            "timestamp": log.timestamp.isoformat() if log.timestamp else None
        })

    return jsonify(result)
