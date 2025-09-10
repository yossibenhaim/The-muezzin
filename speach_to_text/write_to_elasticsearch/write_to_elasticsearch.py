from elasticsearch import Elasticsearch, exceptions
from dotenv import load_dotenv
import os
from speach_to_text.logger import Logger

logger = Logger.get_logger()
load_dotenv('../.env')


class Write_to_elasticsearch:
    def __init__(self):
        self.index_name = os.getenv('INDEX-NAME-FOR-ELASTICSEARCH')
        self.host = os.getenv("HOST-FOR-ELASTICSEARCH")
        self.port = os.getenv("PORT-FOR-ELASTICSEARCH")
        self.es = Elasticsearch(f"http://{self.host}:{self.port}")
        logger.info("the Elasticsearch is conn")


    def update_docs(self, doc : dict):
        try:
            body_for_create = {
                "doc": doc['metadata'],
                "doc_as_upsert": True
            }
            print(doc['metadata'])
            self.es.update(index=self.index_name, id=doc['_id'], body=body_for_create)
            logger.info(f"the doc: {doc['_id']} is update in {self.index_name}")
        except exceptions.AuthorizationException as e:
            logger.error(f"error:{e}")
            raise e
        except exceptions.AuthenticationException as e:
            logger.error(f"error:{e}")
            raise e
