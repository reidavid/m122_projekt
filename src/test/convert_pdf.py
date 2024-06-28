#!/usr/bin/env python

import pypandoc
import docx


class ConvertPDF:

    def __init__(self, txt):
        doc = docx.Document
        doc.add_heading(txt)
        doc.save('tmp_doc.docx')
        pypandoc.convert_file('tmp_doc.docx', docx)
