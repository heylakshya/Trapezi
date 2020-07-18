from pdf_crop import crop
from pdf_text import extractText

source = 'pdfs/2002fang.pdf'
cropFile = '_'.join([source[:-4], 'crop.pdf'])
txtFile = '_'.join([source[:-4], 'text.txt'])

""" (left,bottom,right,top)"""

tables = {
    2: [
        [312, 618, 561, 748]
    ]
}
crop(source, cropFile, tables)
extractText(cropFile, txtFile)
