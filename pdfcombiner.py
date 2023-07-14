import PyPDF2, os

pdfiles = []

for filename in os.listdir('C:\\Users\\navan\\OneDrive\\Desktop\\pdfs'):
        if filename.endswith('.pdf'):
                if filename != 'merged.pdf':
                        pdfiles.append(filename)
                        
pdfiles.sort(key = str.lower)

pdfMerge = PyPDF2.PdfMerger()

for filename in pdfiles:
        pdfFile = open('C:\\Users\\navan\\OneDrive\\Desktop\\pdfs\\'+filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        pdfMerge.append(pdfReader)

pdfFile.close()
pdfMerge.write('merged.pdf')