# This is project 04

# credits ==>
print("Welcome to PDF Merger v2.3 created by Ranit Kumar Manik.")

import PyPDF2

# taking input of 2 pdfs and storing them into a variable as lists ==>
choice = input("If you want to try a demo press: 'd', if you want to go for custom press:'c'\n")
if choice == 'd':
    pdf_files = ["assets/1.pdf", "assets/2.pdf"]
elif choice == 'c':
    x = input("Enter the name with location of the first pdf file: ")
    y = input("Enter the name with location of the second pdf file: ")
    pdf_files = [x, y]
else:
    print("Plz Enter a valid choice")

# PDF merging ==>
pdfMerge = PyPDF2.PdfMerger()

for filename in pdf_files:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfMerge.append(pdfReader)

pdfFile.close()
pdfMerge.write('merged.pdf')
