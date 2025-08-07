from kafka import KafkaProducer
import json

def send_log(event: dict):
    try:
        print(f"[DEBUG] TRIMIT LOG LA KAFKA: {event}")
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        producer.send('api-logs', event)
        producer.flush()
        producer.close()
    except Exception as e:
        print(f"[Kafka] Eroare la trimiterea logului: {e}")


