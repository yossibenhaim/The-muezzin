from pymongo import MongoClient, errors
from dotenv import dotenv_values
import os
from consumer.logger import Logger

dotenv_values('../.env')


logger = Logger.get_logger()
class Write_to_mongoDB:
    def __init__(self):
        self.client = None
        self.host = os.getenv("DB_HOST")
        self.db_name = os.getenv("DB_NAME")
        self.db_coll = os.getenv("DB_COLL")
        self.db_port = os.getenv("BD_PORT")

    def connect(self):
        try:
            self.client = MongoClient(f"mongodb://{self.host}:{self.db_port}")
            self.client.admin.command("ping")
            logger.info(f"Connected to {self.host}!")
        except errors.ServerSelectionTimeoutError as err:
            logger.error(f"Server selection timeout: {err}")
            raise
        except errors.ConnectionFailure as err:
            logger.error(f"Connection failed: {err}")
            raise
        except errors.ConfigurationError as err:
            logger.error(f"Configuration error: {err}")
            raise
        except Exception as err:
            logger.error(f"Unexpected error: {err}")
            raise

    def close_conn(self):
        self.client.close()
        logger.info("the conn to mongodb is closed")

    def get_all_docs(self):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            result = list(collection.find({}))
            logger.info("the data is get from mongodb")
            return result
        except Exception as e:
            logger.error(e)
            raise Exception(e)
        finally:
            self.close_conn()

    def get_docs_by_id(self,doc_id):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            result = list(collection.find({'_id':doc_id}))
            logger.info(f"the doc: {doc_id} is get from mongodb")
            return result
        except Exception as e:
            logger.error(e)
            raise Exception(e)
        finally:
            self.close_conn()


    def insert_dod(self, doc : dict):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            filter_criteria  = {'_id' : doc["_id"]}
            result = collection.update_one(filter_criteria, {"$set": doc}, upsert=True)
            if result.upserted_id:
                logger.info(f"the doc: {doc["_id"]} inserted to mongodb")
            else:
                logger.info(f"the doc: {doc['_id']} is exists - the file is updated in mongodb")

        except Exception as e:
            logger.error(e)
            raise Exception(e)
        finally:
            self.close_conn()