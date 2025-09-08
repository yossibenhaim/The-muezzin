import wave
import os
from datetime import datetime

from producer.logger import Logger



logger = Logger.get_logger()




class Utils:

    @staticmethod
    def read_wav_metadata_basic(file_path):
        logger.info("Entering read_wav_metadata_basic")
        try:
            with wave.open(file_path, 'rb') as wf:
                logger.info(f"Trying to generate metadata for {file_path}")
                metadata = {
                    "file path": file_path,
                    "metadata": {
                        "name file" : os.path.basename(file_path),
                        "Creation date" : Utils.get_wav_creation_date(file_path),
                        "Sample width (bytes)": wf.getsampwidth(),
                        "Number of frames": wf.getnframes(),
                        "Duration (seconds)": wf.getnframes() / wf.getframerate()
                    }
                }
            logger.info("The information was created")
            for i in metadata["metadata"]:
                print(type(i))
            return metadata
        except wave.Error as e:
            logger.error(f"Error reading WAV file: {e}")
            raise f"Error reading WAV file: {e}"


    @staticmethod
    def get_wav_creation_date(file_path):
        """
        Returns the creation date of a WAV file.

        Args:
            file_path (str): The path to the WAV file.

        Returns:
            str: The creation date of the file in a human-readable format,
                 or an error message if the file is not found.
        """
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"

        try:
            # Get the creation timestamp
            creation_timestamp = os.path.getctime(file_path)

            # Convert the timestamp to a datetime object
            creation_datetime = datetime.fromtimestamp(creation_timestamp)

            # Format the datetime object for readability
            return creation_datetime.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            return f"An error occurred: {e}"
