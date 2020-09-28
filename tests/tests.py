# -*- coding:utf-8 -*-

"""Tests for gendiff."""

from gendiff.generate_diff.generate_diff import generate_diff


def test_generate_diff_json():
    """Check generate_diff for json files."""
    generated_str = generate_diff(
        'tests/fixtures/json/file1.json',
        'tests/fixtures/json/file2.json',
    )
    file_w_answer = open('tests/fixtures/diff_file1_file2.txt',)

    true_str = file_w_answer.read()
    true_list = true_str.split('\n')
    list4check = generated_str.split('\n')

    assert set(true_list) == set(list4check)


def test_generate_diff_yaml():
    """Check generate_diff for yaml files."""
    generated_str = generate_diff(
        'tests/fixtures/yaml/file1.yaml',
        'tests/fixtures/yaml/file2.yaml',
    )
    file_w_answer = open('tests/fixtures/diff_file1_file2.txt',)

    true_str = file_w_answer.read()
    true_list = true_str.split('\n')
    list4check = generated_str.split('\n')

    assert set(true_list) == set(list4check)


def test_generate_diff_json_recursive():
    """Check generate_diff for nested json format."""
    generated_str = generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
    )
    file_w_answer = open('tests/fixtures/diff_file3_file4_dict.txt',)

    true_str = file_w_answer.read()
    true_list = true_str.split('\n')
    list4check = generated_str.split('\n')

    assert set(true_list) == set(list4check)


def test_generate_diff_plain_output():
    """Check generate_diff with plain output."""
    generated_str = generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
        'plain'
    )
    file_w_answer = open('tests/fixtures/diff_file3_file4_plain.txt',)

    true_str = file_w_answer.read()
    true_list = true_str.split('\n')
    list4check = generated_str.split('\n')

    assert set(true_list) == set(list4check)


def test_generate_diff_json_output():
    """Check generate_diff with json output."""
    generated_str = generate_diff(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
        'json'
    ).replace(',','')
    file_w_answer = open('tests/fixtures/diff_file3_file4_json.json')

    true_str = file_w_answer.read().replace(',','')
    true_list = true_str.split('\n')
    list4check = generated_str.split('\n')

    assert set(true_list) == set(list4check)