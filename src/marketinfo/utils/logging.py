import logging
import sys
import os


class InitLog:
    def __init__(self):
        # LOG-Files erstellen, falls nicht vorhanden
        if not os.path.exists("src/log/log.log"):
            with open("src/log/log.log", "w"): pass
        if not os.path.exists("src/log/error.log"):
            with open("src/log/error.log", "w"): pass

        # Configure logging
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("src/log/log.log"),
                                logging.StreamHandler(sys.stdout)
                            ])

        # Configure error logging
        error_handler = logging.FileHandler("src/log/error.log")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(error_handler)

        # Logger erstellen
        self.logger = logging.getLogger(__name__)
