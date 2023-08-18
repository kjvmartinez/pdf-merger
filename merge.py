import sys
from PyPDF2 import PdfMerger as pdfM

import glob

def mergePDF(files):
    filename = str(input("Enter the name of the new file: ")) 
    merger=pdfM()
    for i in files:
        merger.append(i)
    merger.write(filename)

# ipaste dito ang path ng folder located ang pdfs
files = glob.glob(r"/Users/user/Documents/Dev/WIP/pdfsmerger/demo/**/*.pdf", recursive=True)
mergePDF(files)