from PyPDF2 import PdfReader, PdfWriter

pdf_reader = PdfReader('./PDFs/MackBookProM1.pdf')

for index, page in enumerate(pdf_reader.pages):
  pdf_writter = PdfWriter()
  pdf_writter.add_page(page)

  with open(f'page_{index+1}.pdf', 'wb') as out:
    pdf_writter.write(out)