from PyPDF2 import PdfFileMerger
from glob import glob

merger = PdfFileMerger()

for pdf in glob('PdfFiles/*.pdf'):
	merger.append(pdf)

merger.write('result.pdf')
merger.close()


