from app import app
from models.request_log import RequestLog


with app.app_context():
    logs = RequestLog.query.all()
    for log in logs:
        print(f"[{log.timestamp}] {log.operation.upper()} {log.input} = {log.result}")
