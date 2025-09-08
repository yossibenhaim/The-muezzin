from producer.reading_files.reading_files import Reading_files
from producer.utils_producer import Utils
from producer.kafka_producer.kaska_producer import Producer
import os
from dotenv import load_dotenv
from producer.logger import Logger



logger = Logger.get_logger()

load_dotenv('../.env')

class Manager:
    def __init__(self):
        self.reading_files = Reading_files()
        self.utils = Utils()
        self.producer = Producer()
        self.topic = os.getenv('TOPIC-FOR-PROCESSING-SERVICE')

    def start(self):
        files = self.reading_files.get_all_files()
        if not self.producer.producer:
            self.producer.conn()
        for file in files:
            metadata = self.utils.read_wav_metadata_basic(file)
            self.producer.send_message(self.topic, metadata)
        self.producer.close_conn()

a = Manager()
a.start()