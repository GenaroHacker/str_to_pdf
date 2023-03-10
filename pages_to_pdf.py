from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Ubuntu', 'Ubuntu-Regular.ttf'))

if False:
 page_1 = [['wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww', 'day, the sun is shining ', 'and the birds are ', "chirping. I can't wait to ", 'go for a walk and ', 'enjoy the fresh air. '],
 ['I love cooking, ', 'experimenting with ', 'new ingredients and ', 'flavors. Yesterday, I ', 'made a delicious ', 'chicken curry that my ', 'family really enjoyed. '],
 ["I'm so excited to start ", 'my new job next week, ', "it's a great opportunity ", 'for me to learn and ', 'grow in my career. ']
 ]

 page_2 = [
 ['Hello World, this is a test to see if the function works how it should. I ',
  'hope it does, otherwise I will have to fix it. '],
 ['I enjoy traveling and ', 'exploring new places. ', 'Last summer, I went ', 'on a road trip across ', 'the United States and ', 'visited some amazing ', 'national parks. '],
 ['Music is a big part of ', 'my life, I listen to it ', "when I'm happy, sad, ", 'or just need to relax. ', 'My favorite band is ', 'Radiohead, their music ', 'is so unique and ', 'beautiful. ']
 ]

 page_3 = [
 ["I'm a coffee addict, I ", "can't start my day ", 'without a good cup of ', 'coffee. I like to try ', 'different blends and ', 'roasts to find my ', 'perfect cup. '],
 ["I'm passionate about ", 'sustainability and ', 'taking care of the ', 'planet. I try to reduce ', 'my waste and use ', 'eco-friendly products ', 'whenever possible. '],
 ['I love spending time ', 'with my family and ', "friends, whether it's ", 'going out to eat or just ', 'hanging out at home. ', "It's always a good time ", "when we're together. "]
 ]

 pages = [page_1, page_2, page_3]






def pages_to_pdf(pages,output_file_name):
    c = canvas.Canvas(output_file_name, pagesize=A4)
    for page in pages:
        c.setFont('Ubuntu', 16)
        c.setLineWidth(.3)
        c.setStrokeColorRGB(0.2,0.5,0.3)
        c.line(3*cm, 0*cm, 3*cm, 29.7*cm)
        for i in range(32):
            c.line(0*cm, 2.2*cm+i*0.8*cm, 21*cm, 2.2*cm+i*0.8*cm)
        for block in page:
            for line in block:
                c.drawString(3.2*cm, 1.45*cm+i*0.8*cm, line)
                i += -1
        c.showPage()
    c.save()
    
#The function empty text recibes a text and erase some words replacyng its characters for spacebars
def empty_text(text,coeficient):
    import random
    new_text = ""
    words = text.split()
    for word in words:
        if random.random() < coeficient:
            new_text += " "*len(word)
        else:
            new_text += word
        new_text += " "
    return new_text
def list_of_tuples_to_pages(list_of_tuples, tags, amount_of_pages=1,coeficient=0.5):
    from random import choice
    pages = []
    for i in range(amount_of_pages):
        page = []
        for j in range(6):
            block = []
            #choice
            random_tag = choice(tags)
            #filter
            filtered_list_of_tuples = []
            for tuple in list_of_tuples:
                if tuple[1] == random_tag:
                    filtered_list_of_tuples.append(tuple)
            #choice
            if len(filtered_list_of_tuples) > 0:
                random_tuple = choice(filtered_list_of_tuples)
                #split
                from str_to_block import split_string
                block = split_string(random_tuple[2],600)
                #empty text with coeficient 0.5
                block = [empty_text(line,coeficient) for line in block]
            page.append(block)
        pages.append(page)
    return pages
