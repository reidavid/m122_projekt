import logging
import sys


class InitLog:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("log/log.log"),
                                logging.StreamHandler(sys.stdout)
                            ])

        # Configure error logging
        error_handler = logging.FileHandler("log/error.log")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(error_handler)

        # Logger erstellen
        self.logger = logging.getLogger(__name__)
