

class Utils:

    @staticmethod
    def create_id(metadata):
        metadata['_id'] = str(metadata['metadata']['Number of frames']) + str(metadata['metadata']['Duration (seconds)'])
        return metadata

    @staticmethod
    def create_doc_to_send_to_elastic(doc):
        doc_to_elastic = {"_id" : doc['_id'], "metadata" : doc['metadata']}
        return doc_to_elastic

    @staticmethod
    def create_doc_to_send_to_mongodb(doc):
        doc_to_mongodb = {"_id" : doc['_id'], "data": Utils.get_binary_audio_file(doc['file path'])}
        return doc_to_mongodb


    @staticmethod
    def get_binary_audio_file(audio_file_path):
        with open(audio_file_path, 'rb') as audio_file:
            binary_data = audio_file.read()
        return binary_data
