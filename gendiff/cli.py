# This Python file uses the following encoding: utf-8

"""Functions of project."""
import argparse


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
