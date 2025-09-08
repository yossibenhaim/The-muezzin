from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="logs/logs.log")

load_dotenv('../../.env')


class Write_to_elasticsearch:
    def __init__(self):
        self.index_name = os.getenv('INDEX-NAME-FOR-ELASTICSEARCH')
        self.host = os.getenv("HOST-FOR-ELASTICSEARCH")
        self.port = os.getenv("PORT-FOR-ELASTICSEARCH")
        self.es = Elasticsearch(f"http://{self.host}:{self.port}")
        logging.info("the Elasticsearch is conn")

    def get_mapping(self):
        mapping = {
                "properties": {
                    "name": { "type": "text" },
                    "Creation date": { "type": "date" },
                    "Sample width (bytes)": { "type": "int" },
                    "Number of frames": { "type": "int" },
                    "Duration (seconds)": { "type": "float" }
                }
            }
        return mapping


    def create_index(self):
        try:
            mapping = self.get_mapping()
            self.es.indices.create(index=self.index_name, mappings=mapping, ignore=400)
            logging.info("the mapping is created")
        except:
            logging.error("error:")
            raise "error:"



    def added_docs(self, doc : dict):
        try:
            self.es.index(index="users_extended", id=doc['id'], document=doc['metadata'])
            logging.info(f"the doc: {doc} is open to {self.index_name}")
        except:
            logging.error("error:")
            raise "error:"