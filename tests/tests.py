# -*- coding:utf-8 -*-

"""Tests for gendiff."""

from gendiff.cli import generate_diff


def test_generate_diff():
    """Check generate_diff."""
    generated_str = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')

    file_w_answer = open('tests/fixtures/diff_file1_file2.txt')

    true_str = file_w_answer.read()
    true_list = true_str.split('\n')
    list4check = generated_str.split('\n')

    assert set(true_list) == set(list4check)
