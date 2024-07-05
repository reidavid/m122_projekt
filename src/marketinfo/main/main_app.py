import sys
from src.marketinfo.data.get_data import GetData
from src.marketinfo.utils.send_mail import *
from src.marketinfo.utils.convert_pdf import *


class MainApp:
    def __init__(self):
        with open("CREDENTIALS.json") as f:
            cred = json.load(f)

        # API Call mit externer JSON Datei und Skriptparameter als Limit
        data = GetData(cred, sys.argv[1]).formatted_data

        SendMail(cred, data)
        ConvertPDF(data)
