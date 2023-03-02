
#The function splits text inte lines of 280 characters each. The function returns a list of lines. The last line may contain less than 280 characters without breaking any word
#It discards the last line
def split_text_into_lines(text):
    lines = []
    for i in range(0, len(text), 280):
        lines.append(text[i:i+280])
    lines.pop()
    return lines


def insert_text_into_table(text,tag,base,table):
    from sql_core import insert_record
    blocks = split_text_into_lines(text)
    for block in blocks:
        #filter all the " and ' from the text
        block = block.replace("'","")
        block = block.replace('"',"")
        insert_record(base,"INSERT INTO "+table+" VALUES (NULL,'"+tag+"','"+block+"')")
    print("Inserted "+str(len(blocks))+" blocks into table "+table+" with tag "+tag)
