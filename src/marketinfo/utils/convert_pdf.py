import pdfkit


class ConvertPDF:
    def __init__(self, data):
        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
        pdfkit.from_string(data, '_test.pdf', configuration=config)
