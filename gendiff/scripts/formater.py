# This Python file uses the following encoding: utf-8

"""Functions for work with json files."""
from gendiff import diff
from gendiff import file_loader
from gendiff.views import plain
from gendiff.views import default
from gendiff.views import json


FORMATS_DICT = {
    'default': default.view,
    'json': json.view,
    'plain': plain.view,
}


def generate(file_path1, file_path2, format='default'):
    data_file1 = file_loader.load(file_path1)
    data_file2 = file_loader.load(file_path2)
    return FORMATS_DICT[format](diff.make_diff(data_file1, data_file2))
