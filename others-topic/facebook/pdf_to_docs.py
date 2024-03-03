# convert pdf into docs

import fitz
from docx import Document

def pdf_to_docs(pdf_file, output_file):
    pdf_document = fitz.open(pdf_file)
    docx_document = Document()
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        docx_document.add_paragraph(text)
    docx_document.save(output_file)
    pdf_document.close()


if __name__ == "__main__":
    pdf_file = "C:/Users/Hy_vipan/Downloads/sample3 (1).pdf"
    output_file = 'output.docx'

    pdf_to_docs(pdf_file, output_file)