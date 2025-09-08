from consumer.write_to_elasticsearch.write_to_elasticsearch import Write_to_elasticsearch
from consumer.write_to_mongo.write_to_mongoDB import Write_to_mongoDB
from consumer.utils.utils_consumer import Utils

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
        """
        Receives the file and sends it to elastic and mongodb as needed
        :param doc: dict
        """
        #send to added id
        doc = self.utils.create_id(doc)

        doc_to_elastic = self.utils.create_doc_to_send_to_elastic(doc)
        doc_to_mongodb = self.utils.create_doc_to_send_to_mongodb(doc)

        self.write_to_elasticsearch(doc_to_elastic)
        self.write_to_mongodb(doc_to_mongodb)

    def write_to_elasticsearch(self, doc):
        self.es.added_docs(doc)

    def write_to_mongodb(self, doc):
        self.mongo.insert_dod(doc)

    def get_doc_by_id_from_mongodb(self, _id):
        doc = self.mongo.get_docs_by_id(_id)
        return doc
