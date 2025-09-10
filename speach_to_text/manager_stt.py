import os

from speach_to_text.write_to_elasticsearch.write_to_elasticsearch import Write_to_elasticsearch
from speach_to_text.speach_to_text.speach_to_text import Speach_to_text
from speach_to_text.kafka_stt.producer_to_analysis import Producer
from speach_to_text.utils.utils_stt import Utils
from dotenv import load_dotenv

load_dotenv('.env')


class Manager:
    def __init__(self):
        """
        Responsible for transcribing messages into text and sending them to elastic
        """
        self.es = Write_to_elasticsearch()
        self.utils = Utils()
        self.speach_to_text = Speach_to_text()
        self.producer_to_analysis = Producer()
        self.topic_to_analysis = os.getenv('TOPIC-FOR-ANALYSIS-SERVICE')



    def speach_to_text_and_update_elastic(self, doc):
        """
        Converts the meaning to text and updates in elastic
        """
        doc = self.utils.create_id(doc)

        doc = self.convert_audio_to_text(doc)
        doc_to_elastic = self.utils.update_doc_to_send_to_elastic(doc)

        self.update_in_elasticsearch(doc_to_elastic)
        self.producer_to_analysis.send_message(self.topic_to_analysis, doc)


    def update_in_elasticsearch(self, doc):
        self.es.update_docs(doc)

    def convert_audio_to_text(self, doc):
        doc['text'] = self.speach_to_text.stt(doc['file path'])
        doc['metadata'] = {"doc" : doc['metadata']}
        return doc
