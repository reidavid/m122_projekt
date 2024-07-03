import sys
import json
from src.marketinfo.data.get_data import GetData
from src.marketinfo.utils import *


class MainApp:
    def __init__(self):
        with open("src/CREDENTIALS.json") as f:
            cred = json.load(f)

        data = GetData(cred, sys.argv[1]).formatted_data

        SendMail(cred, data)
        ConvertPDF(data)
