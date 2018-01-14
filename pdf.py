import os
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

for a in range(1, len(os.listdir(os.getcwd()))):
	print(a)
	pdf.image(str(a) + '.png',w=200)
pdf.output('output.pdf','f')

