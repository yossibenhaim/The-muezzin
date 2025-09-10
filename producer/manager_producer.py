from producer.reading_files.reading_files import Reading_files
from producer.utils_producer import Utils
from producer.kafka_producer.kafka_producer import Producer
import os
from dotenv import load_dotenv


load_dotenv('.env')

class Manager:
    def __init__(self):
        self.reading_files = Reading_files()
        self.utils = Utils()
        self.producer = Producer()
        self.topic_to_consumer = os.getenv('TOPIC-FOR-CONSUMER-SERVICE')
        #topic to convert speach to text
        self.topic_to_stt = os.getenv('TOPIC-FOR-STT-SERVICE')

    def start(self):
        files = self.reading_files.get_all_files()
        if not self.producer.producer:
            self.producer.conn()
        for file in files:
            metadata = self.utils.read_wav_metadata_basic(file)
            self.producer.send_message(self.topic_to_consumer, metadata)
            self.producer.send_message(self.topic_to_stt, metadata)
        self.producer.close_conn()

a = Manager()
a.start()