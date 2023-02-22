def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content