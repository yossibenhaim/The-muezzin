import os
from kafka import KafkaConsumer
from dotenv import load_dotenv
import json
from consumer.manager_consumer import Manager
from consumer.logger import Logger

Logger()
logger = Logger.get_logger()

load_dotenv('../../.env')

topic = os.getenv('TOPIC-FOR-PROCESSING-SERVICE')
host = os.getenv('HOST-FOR-PROCESSING-SERVICE')

manager_consumer = Manager()

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=host,
    api_version=(0, 11, 5),
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    request_timeout_ms=60000,

)
print(f"{topic} מקשיב להודעות...")

for message in consumer:
    print("התקבלה הודעה:")
    manager_consumer.write_to_elastic_and_mongodb(message.value)