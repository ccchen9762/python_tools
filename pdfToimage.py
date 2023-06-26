from pdf2image import convert_from_path

pages = convert_from_path('')

i = 0
for page in pages:
    i+=1
    page.save('0' + str(i) +'.jpg', 'JPEG')