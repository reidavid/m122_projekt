import pdfkit

data = '<h1>hallo</h1>'

config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_string(data, '_test.pdf', verbose=True,
                   configuration=config)
