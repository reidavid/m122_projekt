import logging
import pdfkit
from ..utils.logging import *


class ConvertPDF:
    def __init__(self, data):
        logger = InitLog().logger

        self.pdf = "_test.pdf"
        css = "assets/css.css"

        # Pfad zu wkhtmltopdf
        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
        # PDF erstellen
        try:
            pdfkit.from_string(data, self.pdf, configuration=config, css=css)
        except:
            logger.error("Failed to convert String to PDF")
