def read_file(file_path):
    with open(file_path) as file:
        return file.read()


def write_to_file(file_path, content):
   with open(file_path, "w") as file:
    file.write(content)