
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="../logs/logs.log")



class Processor:

    def create_id(self, metadata):
        metadata['id'] = str(metadata['metadata']['Number of frames']) + str(metadata['metadata']['Duration (seconds)'])
        return metadata
