# This Python file uses the following encoding: utf-8

"""Functions for work with json files."""

from gendiff.file_loader.file_loader import json_loader, yaml_loader


def generate_formats_dict():
    """Generate dictionary of the formats.

    Returns:
        dictionary(dict) - dictionary of the formats,
    """
    return {
        'json': json_loader,
        'yaml': yaml_loader,
    }


def generate_diff(file_path1, file_path2, format):
    """Generate difference function.

    Finds difference between two given files.

    Args:
        file_path1(str): path to 1st file,
        file_path2(str): path to 2st file,
        format(str): file format,

    Returns:
        diff(str) - the difference between two given files.
    """
    formats = generate_formats_dict()
    data_file1, data_file2 = formats[format](file_path1, file_path2)

    keys_in_f1 = data_file1.keys()
    keys_in_f2 = data_file2.keys()
    all_keys = set(keys_in_f1).union(keys_in_f2)
    diff = []

    for key in all_keys:
        if key in keys_in_f1 and key in keys_in_f2:
            if data_file1[key] == data_file2[key]:
                diff.append(
                    '  {arg1}: {arg2}'.format(
                        arg1=key,
                        arg2=data_file1[key],
                    ),
                )
            else:
                diff.append(
                    '- {arg1}: {arg2}'.format(
                        arg1=key,
                        arg2=data_file1[key],
                    ),
                )
                diff.append(
                    '+ {arg1}: {arg2}'.format(
                        arg1=key,
                        arg2=data_file2[key],
                    ),
                )
        elif key in keys_in_f1 and key not in keys_in_f2:
            diff.append(
                '- {arg1}: {arg2}'.format(
                    arg1=key,
                    arg2=data_file1[key],
                ),
            )
        elif key not in keys_in_f1 and key in keys_in_f2:
            diff.append(
                '+ {arg1}: {arg2}'.format(
                    arg1=key,
                    arg2=data_file2[key],
                ),
            )
    return '\n'.join(diff)