from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

event = {
    "operation": "test",
    "input": {"x": 1},
    "result": 123
}

producer.send("api-logs", event)
producer.flush()
producer.close()

print("Mesaj trimis spre Kafka.")
