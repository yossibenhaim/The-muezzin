import json
import os
from kafka import KafkaProducer
from kafka.errors import RecordListTooLargeError, AuthorizationError, InvalidConfigurationError, KafkaError
from dotenv import load_dotenv
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="logs/logs.log")

load_dotenv('.env')


class Producer:
    def __init__(self):
        try:
            self.host = os.getenv("HOST-FOR-PROCESSING-SERVICE")
            self.producer = KafkaProducer(bootstrap_servers=self.host,
                                    value_serializer=lambda x:
                                    json.dumps(x).encode('utf-8')
                                    )

            logging.info("Reading the environment variables")
        except FileNotFoundError as e:
            raise f"error: {e}"

    def send_message(self, topic, message):
        try:
            self.producer.send(topic, message)
            logging.info(f"the massage: {message} is send to topic: {topic}")
            print("sent:",message, "to", topic)
        except RecordListTooLargeError as e:
            logging.error(f"error: {e}")
            raise f"error: {e}"
        except AuthorizationError as e:
            logging.error(f"error: {e}")
            raise f"error: {e}"
        except InvalidConfigurationError as e:
            logging.error(f"error: {e}")
            raise f"error: {e}"


    def close_conn(self):
        try:
            self.producer.close()
            logging.info(f"the conn of {self.host} is closed")
        except KafkaError as e:
            logging.error(f"error: {e}")
            raise f"error: {e}"

    def conn(self):
        if not self.producer:
            self.producer = KafkaProducer(bootstrap_servers=self.host,
                                    value_serializer=lambda x:
                                    json.dumps(x).encode('utf-8'),
                                          )
