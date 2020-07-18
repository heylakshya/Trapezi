from PyPDF2 import PdfFileWriter, PdfFileReader
from copy import copy

''' source is directory of source file.

target is directory of target file.

tables is a dictionary of coordinates 

coordinates is a list of "values"
"values" as  list of 4 values (left,bottom,right,top)
'''
def crop(source, target, tables):
    pdf = PdfFileReader(open(source,'rb'))
    output = PdfFileWriter()
    for pageNum, coordinates in tables.items():
        page = pdf.getPage(pageNum)
        for values in coordinates:
            temp = copy(page)
            bottomLeft = (values[0], values[1])
            topRight = (values[2], values[3])
            temp.trimBox.lowerLeft = bottomLeft
            temp.trimBox.upperRight = topRight
            temp.cropBox.lowerLeft = bottomLeft
            temp.cropBox.upperRight = topRight
            temp.mediaBox.lowerLeft = bottomLeft
            temp.mediaBox.upperRight = topRight
            output.addPage(temp)
    
    outfile = open(target,'wb')
    output.write(outfile)
    outfile.close
