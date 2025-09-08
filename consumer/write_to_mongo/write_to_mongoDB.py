from pymongo import MongoClient, errors
from dotenv import dotenv_values
import os
import logging

dotenv_values('../../.env')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="logs/logs.log")


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
            logging.info(f"Connected to {self.host}!")
        except errors.ServerSelectionTimeoutError as err:
            logging.error(f"Server selection timeout: {err}")
            raise
        except errors.ConnectionFailure as err:
            logging.error(f"Connection failed: {err}")
            raise
        except errors.ConfigurationError as err:
            logging.error(f"Configuration error: {err}")
            raise
        except Exception as err:
            logging.error(f"Unexpected error: {err}")
            raise

    def close_conn(self):
        self.client.close()
        logging.info("the conn to mongodb is closed")

    def get_all_docs(self):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            result = list(collection.find({}))
            logging.info("the data is get from mongodb")
            return result
        except Exception as e:
            logging.error(e)
            raise Exception(e)
        finally:
            self.close_conn()

    def get_docs_by_id(self,doc_id):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            result = list(collection.find({'_id':doc_id}))
            logging.info(f"the doc: {doc_id} is get from mongodb")
            return result
        except Exception as e:
            logging.error(e)
            raise Exception(e)
        finally:
            self.close_conn()


    def insert_dod(self, dod : dict):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            collection.insert_one(dod)
            logging.info(f"the doc: {dod} inserted to mongodb")
        except Exception as e:
            logging.error(e)
            raise Exception(e)
        finally:
            self.close_conn()