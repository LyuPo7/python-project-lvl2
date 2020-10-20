# This Python file uses the following encoding: utf-8

"""Main file of project."""
from gendiff.cli import create_parser
from gendiff import formats


def main():
    """Run project."""
    parser = create_parser()
    namespace = parser.parse_args()
    diff = formats.generate(
        namespace.first_file,
        namespace.second_file,
        namespace.format,
    )
    print(diff)


if __name__ == '__main__':
    main()
