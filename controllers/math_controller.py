from models.request_log import RequestLog
from services.fibonacci_service import fibonacci
from services.factorial_service import factorial
from services.power_service import calculate_power
from database import db
from models.request_schema import PowerRequest, FactorialRequest, FibonacciRequest


def process_operation(operation: str, input_data: dict) -> dict:
    if operation == "power":
        request_model = PowerRequest(**input_data)
        result = calculate_power(request_model.base, request_model.exponent)
    elif operation == "factorial":
        request_model = FactorialRequest(**input_data)
        result = factorial(request_model.number)
    elif operation == "fibonacci":
        request_model = FibonacciRequest(**input_data)
        result = fibonacci(request_model.number)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    # Creează un nou log si il salveaza in baza de date
    log = RequestLog(
        operation=operation,
        input=str(input_data),
        result=str(result)
    )
    db.session.add(log)
    db.session.commit()

   # returneaza rezulatatul
    return {"result": result}
