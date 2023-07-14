import streamlit as st
import PyPDF2
def combine_pdfs(docs):
    pdfMerge = PyPDF2.PdfMerger()

    for filename in docs:
            #pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfReader(filename)
            pdfMerge.append(pdfReader)
    #doc=pdfMerge.write('merged.pdf')
    pdfMerge.write('merged.pdf')
    file=open("merged.pdf",'rb')
    return file

st.header('Combine Your PDFs for Nayandhika :sunglasses:')
st.divider()
files=None
files=st.file_uploader('Attach Your PDFs here',type=['pdf'],accept_multiple_files=True)
print(files)
if files!=None and files:
     doc=combine_pdfs(files)
     if(doc!=None):
         st.download_button('Combine PDfs',data=doc,file_name='combined_pdf.pdf')
else:
     st.write('Upload Files to begin')