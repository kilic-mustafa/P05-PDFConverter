from pdf2docx import Converter

pdf_file = "sample.pdf"
docx_file = "sample.docx"

# convert pdf to docx
cv = Converter(pdf_file=pdf_file) # pdf_file is a parameter name of the method
cv.convert(docx_filename=docx_file) # all pages by default
cv.close()