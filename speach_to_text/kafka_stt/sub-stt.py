import os
from kafka import KafkaConsumer
from dotenv import load_dotenv
import json
from speach_to_text.manager_stt import Manager
from speach_to_text.logger import Logger

Logger()
logger = Logger.get_logger()

load_dotenv('../../.env')

topic = os.getenv('TOPIC-FOR-STT-SERVICE')
host = os.getenv('HOST-FOR-STT-SERVICE')

manager_stt = Manager()

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
    manager_stt.speach_to_text_and_update_elastic(message.value)