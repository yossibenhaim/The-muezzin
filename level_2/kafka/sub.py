import os
from kafka import KafkaConsumer
from dotenv import load_dotenv
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="../../logs/logs.log")
load_dotenv('../../.env')

topic = os.getenv('TOPIC-FOR-PROCESSING-SERVICE')
host = os.getenv('HOST-FOR-PROCESSING-SERVICE')

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=host,
    api_version=(0, 11, 5),
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    request_timeout_ms=100000
)
print(f"{topic} מקשיב להודעות...")

for message in consumer:
    print("התקבלה הודעה:", message.value)