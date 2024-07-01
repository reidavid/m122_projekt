from src.marketinfo.data.get_data import GetData
from src.marketinfo.utils import *


class MainApp:
    def __init__(self):

        data = GetData().formatted_data

        # Mail senden
        SendMail(data)
        # ConvertPDF(data)
