
class Information_analysis:

    def __init__(self, dangerous_words : list , less_dangerous_words : list):
        self.dangerous_words = dangerous_words
        self.less_dangerous_words = less_dangerous_words



    def create_bds_percent(self, text):
        bds_percent = self.check_how_many_dangerous_words_there_are(text)
        bds_percent += self.check_how_many_lass_dangerous_words_there_are(text)
        return bds_percent

    def create_threshold(self, score : float):
        """
        :param score: float,
                The function accepts a number that represents the level of danger.
        :return: bool,
                returns true or false whether the message is criminalized.
        """
        if score > 0.01:
            return True
        else:
            return False


    def check_how_many_dangerous_words_there_are(self, text):
        """
        :param text: str,
        The function receives text and checks whether and how many dangerous words it contains.
        It finally divides the number of dangerous words found by the total number of words and that is what is returned

        :return: float,
        It returns a score of the danger level.
        """
        dangerous_words = []
        for dangerous_word in self.dangerous_words:
            if dangerous_word in text:
                dangerous_words.append(dangerous_word)
        if dangerous_words:
            print( ((len(dangerous_words) * 2) / len(text)) * 100)
            return ((len(dangerous_words) * 2) / len(text)) * 100
        else:
            return 0

    def check_how_many_lass_dangerous_words_there_are(self, text):
        """
        :param text: str,
        The function receives text and checks whether and how many dangerous words it contains.
        It finally divides the number of dangerous words found by the total number of words and that is what is returned

        :return: float,
        It returns a score of the danger level.
        """
        less_dangerous_words = []
        for dangerous_word in self.less_dangerous_words:
            if dangerous_word in text:
                less_dangerous_words.append(dangerous_word)
        if len(less_dangerous_words) > 0:
            print(((len(less_dangerous_words) * 2) / len(text)) * 100)
            return ((len(less_dangerous_words) * 2) / len(text)) * 100
        else:
            return -1


    def danger_level_segmentation(self, score : float):
        """
        :param score: float,
        The function accepts a number that represents the level of danger of text.
        :return: str,
        its level: none, medium, high.
        """
        if score > 0.5:
            return "high"
        elif score > 0.1:
            return "medium"
        else:
            return "none"