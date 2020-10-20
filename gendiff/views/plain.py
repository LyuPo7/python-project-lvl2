# This Python file uses the following encoding: utf-8

"""Plain view module."""
from gendiff import diff

# Constants
COMPLEX_VALUE = '[complex value]'


def plain(value):
    """Convert value to plain format.

    Returns output in dependence of type of value.

    Args:
        value(): value for convert

    Returns:
        value(str): converted value.
        """
    if isinstance(value, dict):
        return COMPLEX_VALUE
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return "'{}'".format(value)


def view(diffs):
    """View in plain format difference between 2 files.

    Views in plain format difference between 2 files.

    Args:
        diff(dict): difference between 2 files in plain format

    Returns:
        str - difference between 2 files in str format.
    """
    diffl = []
    path = ''

    def view_plain(dict4view, path):
        """Check and print dictionary in plain format.

        Checks if value of the dictionary was updated, removed or added:
        if it was removed prints info about it,
        if it was added prints info about it,
        if it was updated checks if this value is dictionary:
        if so recursively checks every value in it.

        Args:
            dict4view(dict): dictionary for check,
            path(str): path to every value in the dictionary.
        """
        for key, node in sorted(dict4view.items()):
            node_type = node[diff.TYPE]
            node_value = node[diff.VALUE]
            new_path = path + key
            if node_type == diff.REMOVED:
                diffl.append(
                    "Property '{}' was removed".format(new_path),
                )
            elif node_type == diff.ADDED:
                diffl.append(
                    "Property '{}' was added with value: {}".format(
                        new_path,
                        plain(node_value),
                    ),
                )
            elif node_type == diff.CHANGED:
                node_value_old = node.get(diff.OLD_VALUE)
                diffl.append(
                    "Property '{}' was updated. From {} to {}".format(
                        new_path,
                        plain(node_value_old),
                        plain(node_value),
                    ),
                )
            elif node_type == diff.NESTED:
                new_path = path + key
                new_path += '.'
                view_plain(node_value, new_path)
    view_plain(diffs, path)
    return '\n'.join(diffl)
