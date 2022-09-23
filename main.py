import os

import PyPDF2
import sys

##### Function for PDFCombiner `
inputs= sys.argv[1:]
# #
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('Super.pdf')

pdf_combiner(inputs)


### en este ejercico vamos a meterle un watermark al PDF

template = PyPDF2.PdfFileReader(open('.\Folder\Super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)


    with open('watermark_ouput.pdf', 'wb') as file:
        output.write(file)










###first PDF code that rotate and write and print PDF pages

# with open('DummyPDF.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     #print(reader.numPages) # este nos devuelve el numero de paginas del PDF
#     page = reader.getPage(0)# this create another object of the page only
#     #print(page.rotateCounterClockwise(90)) # this will rotate the page 90 degrees
#     page.rotateCounterClockwise(180)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)


