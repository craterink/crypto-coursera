
def open_file(file_path):
    return open(file_path, 'r')


def read_file(file_path):
    file_obj = open_file(file_path)
    return file_obj.read()


def read_lines_from_file(file_path):
    file_contents = read_file(file_path)
    return file_contents.splitlines()
