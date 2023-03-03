def split_string_into_lines(string):
    lines = string.splitlines()

    return lines

def detect_if_is_a_python_function(string):
    if string.startswith('def'):
        return True
    else:
        return False

def read_file(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content

def list_module_functions(file_name):
    file_content = read_file(file_name)
    lines = split_string_into_lines(file_content)
    functions = []
    for line in lines:
        if detect_if_is_a_python_function(line):
            functions.append(line)
    return functions

#test
print("""
for function in list_module_functions('/content/str_to_pdf/sql_core.py'):
    print(function)
    """
)


for function in list_module_functions('/content/str_to_pdf/sql_core.py'):
    print(function)
