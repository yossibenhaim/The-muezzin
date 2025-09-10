

class Utils:
    @staticmethod
    def creating_json_to_send_to_elastic(doc : dict, bds_percent : float, threshold : bool, level_segmentation : str):
        doc["metadata"]["bds_percent"] = bds_percent
        doc["metadata"]["is_bds"] = threshold
        doc["metadata"]["bds_threat_level"] = level_segmentation
        return doc

