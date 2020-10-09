# This Python file uses the following encoding: utf-8

"""Plain view module."""


def convert2plain(value):
    """Convert value to plain format.

    Returns output in dependence of type of value.

    Args:
        value(): value for convert

    Returns:
        value(str): converted value.
        """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return "'{}'".format(value)


def view(diff):
    """View in plain format difference between 2 files.

    Views in plain format difference between 2 files.

    Args:
        diff(dict): difference between 2 files in plain format

    Returns:
        str - difference between 2 files in str format.
    """
    special_keys = {'+', '-'}
    diff_list = []
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
        if special_keys.intersection(dict4view.keys()) == {'+'}:
            diff_list.append(
                "Property '{a1}' was added with value: {a2}".format(
                    a1=path,
                    a2=convert2plain(dict4view['+']),
                ),
            )
        elif special_keys.intersection(dict4view.keys()) == {'-'}:
            diff_list.append(
                "Property '{}' was removed".format(path),
            )
        elif special_keys.intersection(dict4view.keys()) == special_keys:
            if not isinstance(dict4view['+'], dict) or not isinstance(dict4view['-'], dict):
                diff_list.append(
                    "Property '{a}' was updated. From {b} to {c}".format(
                        a=path,
                        b=convert2plain(dict4view['-']),
                        c=convert2plain(dict4view['+']),
                    ),
                )
            else:
                view_plain(dict4view['+'], path)
        else:
            for key in sorted(dict4view.keys()):
                new_path = path + key
                if isinstance(dict4view[key], dict):
                    if not special_keys.intersection(dict4view[key].keys()):
                        new_path += '.'
                    view_plain(dict4view[key], new_path)
    view_plain(diff, path)
    return '\n'.join(diff_list)
