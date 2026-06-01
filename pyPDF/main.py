from pypdf import PdfReader,PdfWriter

reader = PdfReader("sample.pdf")

meta = reader.metadata
print(meta)
print(len(reader.pages))

page =reader.pages[0]
text = page.extract_text(0)  
# print(text)                       # Text from page 1

#- - - Extract text from all pages by looping - - -#
full_text =""
for page in reader.pages:
    full_text += page.extract_text()


###------ SPLITTING PDF INTO MULTIPLE FILES ---------###


for i , page in enumerate(reader.pages):
    sample_writer = PdfWriter()
    sample_writer.add_page(page)
    with open(f'page_{i+1}.pdf' , 'wb') as f:
        sample_writer.write(f)

###------- MERGING PDFs ---------###

merger =PdfWriter()
for pdf in ["page_1.pdf","page_2.pdf","page_3.pdf","page_4.pdf","page_5.pdf"]:
    merger.append(pdf)
merger.write("Merged.pdf")


