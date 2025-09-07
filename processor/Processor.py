import wave
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Processor:

    @staticmethod
    def read_wav_metadata_basic(file_path):
        logging.INFO("Entering read_wav_metadata_basic")
        try:
            with wave.open(file_path, 'rb') as wf:
                logging.INFO(f"Trying to generate metadata for {file_path}")
                matadata = {
                    "matadata": {
                        "file path" : file_path,
                        "Number of channels" : wf.getnchannels(),
                        "Sample width (bytes)" : wf.getsampwidth(),
                        "Frame rate (Hz)": wf.getframerate(),
                        "Number of frames": wf.getnframes(),
                        "Compression type": wf.getcomptype(),
                        "Compression name": wf.getcompname(),
                        "Duration (seconds)": wf.getnframes() / wf.getframerate()
                    }
                }
            logging.INFO("The information was created")
            return matadata
        except wave.Error as e:
            logging.ERROR(f"Error reading WAV file: {e}")
            raise f"Error reading WAV file: {e}"


list_all_files = ['../pondcasts/download (1).wav', '../podcasts/download (10).wav', '../podcasts/download (11).wav', '../podcasts/download (12).wav', '../podcasts/download (13).wav', '../podcasts/download (14).wav', '../podcasts/download (15).wav', '../podcasts/download (16).wav', '../podcasts/download (17).wav', '../podcasts/download (18).wav', '../podcasts/download (19).wav', '../podcasts/download (2).wav', '../podcasts/download (20).wav', '../podcasts/download (21).wav', '../podcasts/download (22).wav', '../podcasts/download (23).wav', '../podcasts/download (24).wav', '../podcasts/download (25).wav', '../podcasts/download (26).wav', '../podcasts/download (27).wav', '../podcasts/download (28).wav', '../podcasts/download (29).wav', '../podcasts/download (3).wav', '../podcasts/download (30).wav', '../podcasts/download (31).wav', '../podcasts/download (32).wav', '../podcasts/download (33).wav', '../podcasts/download (4).wav', '../podcasts/download (5).wav', '../podcasts/download (6).wav', '../podcasts/download (7).wav', '../podcasts/download (8).wav', '../podcasts/download (9).wav', '../podcasts/download.wav']
a = Processor()
for i in list_all_files:
    print(a.read_wav_metadata_basic(i))