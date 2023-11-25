# pip install PyPDF2
from PyPDF2 import PdfFileWriter , PdfFIleReader 
writer = PdfFileWriter()

file = "test_file.pdf"
reader = PdfFIleReader(file)
for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))
writer.encrypt('Password')
with open(f'test_file.pdf','wb')as file:
    writer.write(file)
print("SuccessFully Encrypted PDF")