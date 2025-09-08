import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="../logs/logs.log")

load_dotenv('.env')


class Reading_files:

    def __init__(self):
        """
        get the path for folder file
        """
        self.folder_path = os.getenv('PATH-TO-RECORDINGS-FOLDER')

    def get_all_files(self):
        """
        Goes through the folder and collects the files into a list

        :return: A list containing all files with the path
        """
        if not os.path.isdir(self.folder_path):
            logging.error(f"Folder {self.folder_path} does not exist.")
            raise f"Folder {self.folder_path} does not exist."
        else:
            logging.info(f"Folder {self.folder_path} exists.")
        found_files = []
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                found_files.append(os.path.join(root, file))
        return found_files