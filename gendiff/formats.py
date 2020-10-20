# This Python file uses the following encoding: utf-8

"""Functions for work with json files."""
from gendiff import diff
from gendiff import files
from gendiff import FORMATS_DICT


def generate(file_path1, file_path2, format):
    data_file1 = files.load(file_path1)
    data_file2 = files.load(file_path2)
    if isinstance(data_file1, dict) and isinstance(data_file2, dict):
        return FORMATS_DICT[format](diff.make_diff(data_file1, data_file2))
