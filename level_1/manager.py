import logging
from level_1.dal.DAL_files_from_path_ import DAL
from level_1.utils import Utils
from level_1.pub.pub import Producer
import os
from dotenv import load_dotenv

load_dotenv('../.env')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="../logs/logs.log")



class Manager:
    def __init__(self):
        self.DAL = DAL()
        self.utils = Utils()
        self.producer = Producer()
        self.topic = os.getenv('TOPIC-FOR-PROCESSING-SERVICE')

    def start(self):
        files = self.DAL.get_all_files()
        if not self.producer.producer:
            self.producer.conn()
        for file in files:
            print(file)
            metadata = self.utils.read_wav_metadata_basic(file)
            self.producer.send_message(self.topic, metadata)
        self.producer.close_conn()
a = Manager()
a.start()