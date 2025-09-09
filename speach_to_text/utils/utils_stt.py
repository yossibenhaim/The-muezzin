
class Utils:

    @staticmethod
    def create_id(metadata):
        metadata['_id'] = str(metadata['metadata']['Number of frames']) + str(metadata['metadata']['Duration (seconds)'])
        return metadata

    @staticmethod
    def update_doc_to_send_to_elastic(doc):
        doc_to_elastic = {"_id" : doc['_id'], "metadata" : doc['metadata'], 'text': doc['text']}
        return doc_to_elastic