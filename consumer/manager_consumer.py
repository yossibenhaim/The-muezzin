from write_to_elasticsearch.write_to_elasticsearch import Write_to_elasticsearch
from write_to_mongo.write_to_mongoDB import Write_to_mongoDB
from utils.utils import Utils

class Manager:
    def __init__(self):
        """
        Responsible for managing the flow of the consumer
        Initializes variables for writing to elasticsearch and mongoD
        In addition, uses utiles to divide the information
        To the sender for writing as needed
        """
        self.es = Write_to_elasticsearch()
        self.mongo = Write_to_mongoDB()
        self.utils = Utils()


    def write_to_elastic_and_mongodb(self, doc):
        pass

    def write_to_elasticsearch(self, doc):
        self.es.added_docs(doc)

    def write_to_mongodb(self, doc):
        self.mongo.insert_dod(doc)

    def get_doc_from_mongodb(self, _id):
        doc = self.mongo.get_docs_by_id(_id)
        return doc