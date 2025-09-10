from elasticsearch import Elasticsearch, exceptions
from dotenv import load_dotenv
import os
from consumer.logger import Logger

logger = Logger.get_logger()
load_dotenv('../../.env')


class Write_to_elasticsearch:
    def __init__(self):
        self.index_name = os.getenv('INDEX-NAME-FOR-ELASTICSEARCH')
        self.host = os.getenv("HOST-FOR-ELASTICSEARCH")
        self.port = os.getenv("PORT-FOR-ELASTICSEARCH")
        self.es = Elasticsearch(f"http://{self.host}:{self.port}")
        logger.info("the Elasticsearch is conn")

    def get_mapping(self):
        mapping = {
            "properties": {
                "name": { "type": "text" },
                "Creation date": { "type": "date" },
                "Sample width (bytes)": { "type": "int" },
                "Number of frames": { "type": "int" },
                "Duration (seconds)": { "type": "float" },
                'text' : {'type' : 'text'},
                'bds_percent' : {'type' : 'float'},
                'threshold' : { 'type' : 'boolean'},
                'bds_threat_level' : {'type' : 'keyword'}
            }
        }
        return mapping


    def create_index(self):
        try:
            mapping = self.get_mapping()
            self.es.indices.create(index=self.index_name, mappings=mapping, ignore=400)
            logger.info("the mapping is created")
        except exceptions.ElasticsearchWarning as e:
            logger.error(e)
            raise e



    def added_docs(self, doc : dict):
        try:
            self.es.index(index=self.index_name, id=doc['_id'], document=doc['metadata'])
            logger.info(f"the doc: {doc['_id']} is open to {self.index_name}")
        except exceptions.AuthorizationException as e:
            logger.error(f"error:{e}")
            raise e
        except exceptions.AuthenticationException as e:
            logger.error(f"error:{e}")
            raise e
