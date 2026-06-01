from pypdf import PdfReader,PdfWriter

reader = PdfReader("4th SEM HALL TICKET.pdf")
sample_reader = PdfReader("sample.pdf")
meta = reader.metadata
print(meta)
print(len(reader.pages))

page =reader.pages[0]
text = page.extract_text()  # Text from page 1
# print(text)

#- - - Extract text from all pages by looping - - -#
full_text =""
for page in reader.pages:
    full_text += page.extract_text()


###------ SPLITTING PDF INTO MULTIPLE FILES ---------###


for i , page in enumerate(sample_reader.pages):
    sample_writer = PdfWriter()
    sample_writer.add_page(page)
    with open(f'page_{i+1}.pdf' , 'wb') as f:
        sample_writer.write(f)


    






