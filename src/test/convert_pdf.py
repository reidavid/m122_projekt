from fpdf import FPDF


class ConvertPDF:
    def __init__(self, data):
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size = 15)

        # open the text file in read mode
        f = open("%tmp.txt", "w+")
        f.write(data)

        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

        # save the pdf with name .pdf
        pdf.output("asdf.pdf")
