# This Python file uses the following encoding: utf-8

"""Main file of project."""
from gendiff.cli import create_parser
import sys

def main():
    """Run project."""
    PARSER = create_parser()
    NAMESPACE = PARSER.parse_args(sys.argv[1:])	
    print("I'm not here!")


if __name__ == '__main__':
    main()