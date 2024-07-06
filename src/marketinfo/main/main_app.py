import json
from ..data.get_data import GetData
from ..utils.send_mail import SendMail
from ..utils.convert_pdf import ConvertPDF
from ..utils.logging import InitLog


class MainApp:
    def __init__(self):
        # Logging Initialisieren
        logger = InitLog().logger

        try:
            logger.info("Versuche, Daten aus CREDENTIALS.json auszulesen")
            with open("CREDENTIALS.json") as f:
                cred = json.load(f)
        except FileNotFoundError:
            logger.error('CREDENTIALS.json Datei nicht gefunden')
        except:
            logger.error('Daten von Credentials lesen ist fehlgeschlagen')

        # API Call mit externer JSON Datei und Skriptparameter als Limit
        data = GetData(cred, sys.argv[1]).formatted_data

        SendMail(cred, data)
        ConvertPDF(data)
