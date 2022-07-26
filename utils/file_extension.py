import os


def get_file_extension(filename):
    root, extension = os.path.splitext(filename)
    return extension
