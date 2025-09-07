from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv('../.env')


class Es:
    def __init__(self):

        self.host = os.getenv("HOST-FOR-ELASTICSEARCH")
        self.port = os.getenv("PORT-FOR-ELASTICSEARCH")

        self.es = Elasticsearch(f"http://{self.host}:{self.port}")

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
        mapping = self.get_mapping()
        self.es.indices.create(index="users_extended", mappings=mapping, ignore=400)


    def added_docs(self, docs : list):
        for i, doc in enumerate(docs, start=1):
            self.es.index(index="users_extended", id=doc['id'], document=doc['metadata'])