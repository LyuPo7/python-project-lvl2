# This Python file uses the following encoding: utf-8

"""Main file of project."""
from gendiff.cli import create_parser
from gendiff.cli import generate_diff
import sys


def main():
    """Run project."""
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    diff = generate_diff(namespace.first_file, namespace.second_file)
    print(diff)


if __name__ == '__main__':
    main()
