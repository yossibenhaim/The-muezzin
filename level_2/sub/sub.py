import os
from kafka import KafkaConsumer
from dotenv import load_dotenv
import logging
import json
from level_2.processor.Processor import Processor
from level_2.elstricsearch.es import Es


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="../../logs/logs.log")
load_dotenv('../../.env')

es = Es()
processor = Processor()

topic = os.getenv('TOPIC-FOR-PROCESSING-SERVICE')
host = os.getenv('HOST-FOR-PROCESSING-SERVICE')

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

    es.create_index()
    print("התקבלה הודעה:", message.value)
    es.added_docs(processor.create_id(message.value))

