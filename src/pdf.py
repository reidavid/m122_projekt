#!/usr/bin/env python

import pypandoc
import docx


def to_pdf(txt):
    doc = docx.Document
    doc.add_heading(txt)
    doc.save('tmp_doc.docx')
    pypandoc.convert_file('tmp_doc.docx', docx)
