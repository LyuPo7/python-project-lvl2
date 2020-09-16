# This Python file uses the following encoding: utf-8

"""Functions of project."""
import argparse
import json

def create_parser ():
    parser = argparse.ArgumentParser(
		prog = 'gendiff',
		description = '''Description: The program finds difference between two files.''',
		epilog = '''(c) March 2019. The developer isn't responsible for any problems which might result from work of this program.'''
		)
    parser.add_argument('first_file',
        metavar='first_file',
        type=str,
        help='first file'
    )
    parser.add_argument('second_file',
        metavar='second_file',
        type=str,
        help='first file'
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default="",
        help="set format of output",
        metavar="FORMAT")
    
    return parser


def generate_diff(file_path1, file_path2):
    data_file1 = json.load(open(file_path1))
    data_file2 = json.load(open(file_path2))

    keys_in_f1 = data_file1.keys()
    keys_in_f2 = data_file2.keys()
    all_keys = set(keys_in_f1).union(keys_in_f2)
    result = []

    for key in all_keys:
        if key in keys_in_f1 and key in keys_in_f2:
            if data_file1[key] == data_file2[key]:
                result.append("  {arg1}: {arg2}".format(arg1=key, arg2=data_file1[key]))
            else:
                result.append("- {arg1}: {arg2}".format(arg1=key, arg2=data_file1[key]))
                result.append("+ {arg1}: {arg2}".format(arg1=key, arg2=data_file2[key]))
        elif key in keys_in_f1 and key not in keys_in_f2:
            result.append("- {arg1}: {arg2}".format(arg1=key, arg2=data_file1[key]))
        elif key not in keys_in_f1 and key in keys_in_f2:
            result.append("+ {arg1}: {arg2}".format(arg1=key, arg2=data_file2[key]))
    return '\n'.join(result)