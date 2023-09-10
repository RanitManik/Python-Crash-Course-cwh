# This is project 04

import PyPDF2

# taking input of 2 pdfs and storing them into a variable as lists ==>
x = input("Enter the name with location of the first pdf file: ")
y = input("Enter the name with location of the second pdf file: ")
pdf_files = [x, y]

# PDF merging ==>
pdfMerge = PyPDF2.PdfMerger()

for filename in pdf_files:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfMerge.append(pdfReader)

pdfFile.close()
pdfMerge.write('merged.pdf')
