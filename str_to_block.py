from PIL import ImageFont


#The function takes a font and a string as input and returns the width of the string in pixels
def get_string_width(font_path, string):
    font = ImageFont.truetype(font_path, 20)
    width = 0
    for char in string:
        width += font.getsize(char)[0]
    return width

get_string_width("Ubuntu-Regular.ttf", "Hello World")

#The function takes a string and a integer that represents the maximun with allowed for the string in each line.
#Then the function splits the string into lines without breaking words and returns a list of strings
def split_string(string, max_width):
    words = string.split()
    lines = []
    line = ""
    for word in words:
        if get_string_width("Ubuntu-Regular.ttf", line + word) < max_width:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)
    return lines

#Test
splited = split_string("Hello World, this is a test to see if the function works how it should. I hope it does, otherwise I will have to fix it.", 615)
print(splited)