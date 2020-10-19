# -*- coding:utf-8 -*-

"""Tests for gendiff."""

from gendiff import formats
import json
import pytest


@pytest.mark.parametrize("path_1,path_2,true_path,format", [
    ('tests/fixtures/json/file1.json', 'tests/fixtures/json/file2.json', 'tests/fixtures/diff_file1_file2.txt', 'default'),
    ('tests/fixtures/yaml/file1.yaml', 'tests/fixtures/yaml/file2.yaml', 'tests/fixtures/diff_file1_file2.txt', 'default'),
    ('tests/fixtures/json/file3.json', 'tests/fixtures/json/file4.json', 'tests/fixtures/diff_file3_file4_default.txt', 'default'),
    ('tests/fixtures/json/file3.json', 'tests/fixtures/json/file4.json', 'tests/fixtures/diff_file3_file4_plain.txt', 'plain'),
])
def test_diff_view_text(path_1, path_2, true_path, format):
    """Check generate_diff for json files."""
    generated_str = formats.generate(path_1,path_2,format)
    with open(true_path, 'r') as file_w_answer:
        true_str = file_w_answer.read()

    assert true_str == generated_str


@pytest.mark.parametrize("path_1,path_2,true_path,format", [
    ('tests/fixtures/json/file3.json', 'tests/fixtures/json/file4.json', 'tests/fixtures/diff_file3_file4_json.json', 'json'),
])
def test_diff_view_json(path_1, path_2, true_path, format):
    """Check generate_diff with json output."""
    generated_str = formats.generate(path_1, path_2, format)

    with open(true_path) as file_w_answer:
        true_json = json.load(file_w_answer)

    generated_json = json.loads(generated_str)
    assert true_json == generated_json
