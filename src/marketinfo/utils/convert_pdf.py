import pdfkit


class ConvertPDF:
    def __init__(self, data):

        self.pdf = "_test.pdf"
        css = "assets/css.css"

        # Pfad zu wkhtmltopdf
        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
        # PDF erstellen
        pdfkit.from_string(data, self.pdf, configuration=config, css=css)
