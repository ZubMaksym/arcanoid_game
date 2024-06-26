import os


def search_abs_path(file_name: str):
    return os.path.abspath(__file__ + f'/../../{file_name}')