import os

def extractText(source, target):
    os.system(' '.join(["pdftotext -layout", source, target]))
    # file = open(source,'rb')
    # text = pdftotext.PDF(file)
    # print("\n\n".join(text))
    # out = open(target,'wb')
    # out.write(text)
    # out.close