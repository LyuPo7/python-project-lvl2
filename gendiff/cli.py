# This Python file uses the following encoding: utf-8

"""Functions of project."""
import argparse
import json


def create_parser():
    """Create parser.

    Returns:
        parser - parser.
    """
    parser = argparse.ArgumentParser(
        prog='gendiff',
		description="""Description: 
            The program finds difference between two files.
            """,
		epilog="""(c) September 2020. 
            The developer isn't responsible for any problems
            which might result from work of this program.
            """,
    )
    parser.add_argument(
        'first_file',
        metavar='first_file',
        type=str,
        help='first file',
    )
    parser.add_argument(
        'second_file',
        metavar='second_file',
        type=str,
        help='first file',
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='',
        help='set format of output',
        metavar='FORMAT',
    )

    return parser


def generate_diff(file_path1, file_path2):
    """Generate difference function.

    Finds difference between two given files.

    Args:
        file_path1(str): path to 1st file,
        file_path2(str): path to 2st file,

    Returns:
        diff(str) - the difference between two given files.
    """
    data_file1 = json.load(open(file_path1))
    data_file2 = json.load(open(file_path2))

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
