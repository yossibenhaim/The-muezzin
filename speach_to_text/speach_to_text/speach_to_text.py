import speech_recognition as sr
from producer.logger import Logger


logger = Logger.get_logger()


class Speach_to_text:
    def __init__(self):
        self.r = sr.Recognizer()
        logger.info("the Recognizer is created")

    def stt(self, audio):
        with sr.AudioFile(audio) as source:
            audio = self.r.record(source)
            logger.info("The file has been uploaded and recorded.")

        try:
            text = self.r.recognize_google(audio)
            logger.info("The file has been converted to text.")
            print("Text: " + text)
            return text
        except Exception as e:
            logger.error("Exception: " + str(e))