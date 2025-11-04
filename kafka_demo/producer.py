import time
from kafka import KafkaProducer

TOPIC_NAME = "orders"

producer = KafkaProducer(
    bootstrap_servers=f"kafka-20fad464-abdullahjubairt-9bfb.e.aivencloud.com:19397",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

for i in range(100):
    message = f"Hello from Python using SSL {i + 1}!"
    producer.send(TOPIC_NAME, message.encode('utf-8'))
    print(f"Message sent: {message}")
    time.sleep(1)

producer.close()