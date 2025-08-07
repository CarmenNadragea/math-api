import json
from kafka import KafkaConsumer
from database import db
from models.request_log import RequestLog
from flask import Flask
from datetime import datetime


app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)

consumer = KafkaConsumer(
    'api-logs',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='log-group-test2',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

with app.app_context():
    for msg in consumer:
        data = msg.value
        print("Log Kafka primit:", data)

        new_log = RequestLog(
            operation=data.get('operation'),
            input=json.dumps(data.get('input')),
            result=json.dumps(data.get('result')),
            timestamp=datetime.utcnow()
        )
        db.session.add(new_log)
        db.session.commit()
        print("Log salvat in baza de date")


