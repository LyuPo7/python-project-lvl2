# -*- coding:utf-8 -*-

"""Tests for gendiff."""

from gendiff.scripts import formater
import json


def test_generate_diff_json():
    """Check generate_diff for json files."""
    generated_str = formater.generate(
        'tests/fixtures/json/file1.json',
        'tests/fixtures/json/file2.json',
    )
    with open('tests/fixtures/diff_file1_file2.txt', 'r') as file_w_answer:
        true_str = file_w_answer.read()

    assert true_str == generated_str


def test_generate_diff_yaml():
    """Check generate_diff for yaml files."""
    generated_str = formater.generate(
        'tests/fixtures/yaml/file1.yaml',
        'tests/fixtures/yaml/file2.yaml',
    )

    with open('tests/fixtures/diff_file1_file2.txt', 'r') as file_w_answer:
        true_str = file_w_answer.read()

    assert true_str == generated_str


def test_generate_diff_json_recursive():
    """Check generate_diff for nested json format."""
    generated_str = formater.generate(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
    )

    with open('tests/fixtures/diff_file3_file4_default.txt', 'r') as file_w_answer:
        true_str = file_w_answer.read()

    assert true_str == generated_str


def test_generate_diff_plain_output():
    """Check generate_diff with plain output."""
    generated_str = formater.generate(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
        'plain'
    )
    with open('tests/fixtures/diff_file3_file4_plain.txt', 'r') as file_w_answer:
        true_str = file_w_answer.read()

    assert true_str == generated_str


def test_generate_diff_json_output():
    """Check generate_diff with json output."""
    generated_str = formater.generate(
        'tests/fixtures/json/file3.json',
        'tests/fixtures/json/file4.json',
        'json'
    )

    with open('tests/fixtures/diff_file3_file4_json.json') as file_w_answer:
        true_json = json.load(file_w_answer)

    generated_json = json.loads(generated_str)
    assert true_json == generated_json