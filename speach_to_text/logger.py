import logging
from elasticsearch import Elasticsearch
from datetime import datetime
import os
from dotenv import dotenv_values

dotenv_values('../.env')

host_log = os.getenv('HOST-FOR-ELASTICSEARCH')
port_log = os.getenv('PORT-FOR-ELASTICSEARCH')
host_log = f"{host_log}:{port_log}"
index_log = os.getenv('INDEX-NAME-LOGGING-ELASTICSEARCH')
class Logger:
    _logger = None

    @classmethod
    def get_logger(cls, name="speach-to-text-logs", es_host='http://localhost:9200', index=index_log,
                   level=logging.DEBUG):
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