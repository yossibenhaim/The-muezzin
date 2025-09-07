import wave
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="logs/logs.log")



class Processor:

    @staticmethod
    def read_wav_metadata_basic(file_path):
        logging.info("Entering read_wav_metadata_basic")
        try:
            with wave.open(file_path, 'rb') as wf:
                logging.info(f"Trying to generate metadata for {file_path}")
                metadata = {
                    "file path": file_path,
                    "metadata": {
                        "Number of channels" : wf.getnchannels(),
                        "Sample width (bytes)" : wf.getsampwidth(),
                        "Frame rate (Hz)": wf.getframerate(),
                        "Number of frames": wf.getnframes(),
                        "Compression type": wf.getcomptype(),
                        "Compression name": wf.getcompname(),
                        "Duration (seconds)": wf.getnframes() / wf.getframerate()
                    }
                }
            logging.info("The information was created")
            return metadata
        except wave.Error as e:
            logging.error(f"Error reading WAV file: {e}")
            raise f"Error reading WAV file: {e}"
