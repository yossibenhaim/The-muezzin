import logging
from elasticsearch import Elasticsearch
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv('../.env')

host_log = os.getenv('HOST-FOR-ELASTICSEARCH',"localhost")
port_log = os.getenv('PORT-FOR-ELASTICSEARCH',"9200")
index_log = os.getenv('INDEX-NAME-LOGGING-ELASTICSEARCH-CONSUMER', 'muezzin-logging-consumer')
class Logger:
    _logger = None

    @classmethod
    def get_logger(cls, name="consumer-logs", es_host=f"http://{host_log}:{port_log}", index=index_log,
                   level=logging.INFO):
        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)

        class ESHandler(logging.Handler):
            def emit(self, record):
                try:
                    es.index(index=index, document={
                        "timestamp": datetime.utcnow().isoformat(),

                        "level": record.levelname,
                        "logger": record.name,
                        "message": record.getMessage()
                    })
                except Exception as e:
                    print(f"ES log failed: {e}")
        logger.addHandler(ESHandler())
        logger.addHandler(logging.StreamHandler())
        cls._logger = logger
        return logger