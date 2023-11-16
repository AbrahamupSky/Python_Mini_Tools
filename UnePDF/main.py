import PyPDF2

archivos = ['./PDFs/page_7.pdf', './PDFs/page_8.pdf']

nombre_salida = 'FacturaOswaldo.pdf'

pdf_final = PyPDF2.PdfMerger()

for nombre_archivo in archivos:
  pdf_final.append(nombre_archivo)

pdf_final.write(nombre_salida)
pdf_final.close()