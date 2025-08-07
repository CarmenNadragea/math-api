from kafka import KafkaProducer

try:
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print("Kafka este disponibil!")
except Exception as e:
    print(f"Kafka NU este disponibil: {e}")
