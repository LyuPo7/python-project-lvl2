# This Python file uses the following encoding: utf-8

"""Functions for work with json files."""
from gendiff import diff
from gendiff import files
from gendiff.views import plain
from gendiff.views import default
from gendiff.views import json
from gendiff import views


FORMATS_DICT = {
    views.DEFAULT: default.view,
    views.JSON: json.view,
    views.PLAIN: plain.view,
}


def generate(file_path1, file_path2, format):
    data_file1 = files.load(file_path1)
    data_file2 = files.load(file_path2)
    if data_file1 and data_file2:
        return FORMATS_DICT[format](diff.make_diff(data_file1, data_file2))
