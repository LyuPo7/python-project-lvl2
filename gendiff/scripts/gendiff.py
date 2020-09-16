# This Python file uses the following encoding: utf-8

"""Main file of project."""
from gendiff.cli import create_parser
from gendiff.cli import generate_diff
import sys

def main():
    """Run project."""
    PARSER = create_parser()
    NAMESPACE = PARSER.parse_args(sys.argv[1:])
    diff = generate_diff(NAMESPACE.first_file, NAMESPACE.second_file)
    print(diff)


if __name__ == '__main__':
    main()