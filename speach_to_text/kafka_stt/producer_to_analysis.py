import json
import os
from kafka import KafkaProducer
from kafka.errors import RecordListTooLargeError, AuthorizationError, InvalidConfigurationError, KafkaError
from dotenv import load_dotenv
from producer.logger import Logger

logger = Logger.get_logger()

load_dotenv('../.env')


class Producer:
    def __init__(self):
        try:
            self.host = os.getenv("HOST-FOR-ANALYSIS-SERVICE")
            self.producer = KafkaProducer(bootstrap_servers=self.host,
                                    value_serializer=lambda x:
                                    json.dumps(x).encode('utf-8')
                                    )

            logger.info("Reading the environment variables")
        except FileNotFoundError as e:
            raise f"error: {e}"

    def send_message(self, topic, message):
        try:
            self.producer.send(topic, message)
            logger.info(f"the massage: --- is send to topic: {topic}")
        except RecordListTooLargeError as e:
            logger.error(f"error: {e}")
            raise f"error: {e}"
        except AuthorizationError as e:
            logger.error(f"error: {e}")
            raise f"error: {e}"
        except InvalidConfigurationError as e:
            logger.error(f"error: {e}")
            raise f"error: {e}"


    def close_conn(self):
        try:
            self.producer.close()
            logger.info(f"the conn of {self.host} is closed")
        except KafkaError as e:
            logger.error(f"error: {e}")
            raise f"error: {e}"

    def conn(self):
        if not self.producer:
            self.producer = KafkaProducer(bootstrap_servers=self.host,
                                    value_serializer=lambda x:
                                    json.dumps(x).encode('utf-8'),
                                          )