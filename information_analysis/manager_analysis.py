from information_analysis.utils.utils_analysis import Utils
from information_analysis.decoding_words.decoding_words import Decoding_words
from information_analysis.write_to_elasticsearch.write_to_elasticsearch import Write_to_elasticsearch
from information_analysis.information_analysis.analysis import Information_analysis


class Manager:
    def __init__(self):

        self.decoding = Decoding_words()
        self.utils = Utils()
        self.es = Write_to_elasticsearch()
        self.dangerous_words = None
        self.less_dangerous_words = None

    def running_the_data_analysis(self, doc):
        self.get_all_words()
        self.create_the_analysis(doc)


    def get_all_words(self):
        self.dangerous_words = self.decoding.get_dangerous_words().split(",")
        self.less_dangerous_words = self.decoding.get_less_dangerous_words().split(",")


    def create_the_analysis(self, doc):
        analysis = Information_analysis(self.dangerous_words, self.less_dangerous_words)
        bds_percent = analysis.create_bds_percent(doc["text"])
        threshold = analysis.create_threshold(bds_percent)
        level_segmentation = analysis.danger_level_segmentation(bds_percent)
        doc_to_elastic = self.utils.creating_json_to_send_to_elastic(doc, bds_percent, threshold, level_segmentation)
        self.write_to_elasticsearch(doc_to_elastic)




    def write_to_elasticsearch(self, doc):
        """
        send doc to write in elastic
        :param doc: dict
        """
        self.es.added_docs(doc)

