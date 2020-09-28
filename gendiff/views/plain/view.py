# This Python file uses the following encoding: utf-8

"""Plain view module."""

from gendiff.accessory.functions import create_type_dependedent_output4plain


def plain_view_diff(diff):
    """View in plain format difference between 2 files.

    Views in plain format difference between 2 files.

    Args:
        diff(dict): difference between 2 files in plain format

    Returns:
        str - difference between 2 files in str format.
    """
    diff_list = []
    path = ''

    def view_dict(dict4view, path):
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
        key_list = [key[2:] for key in dict4view.keys()]
        old_values = {}
        new_values = {}
        for key, value in dict4view.items():
            if key.startswith('+ '):
                new_values[key[2:]] = create_type_dependedent_output4plain(
                    value,
                )
            if key.startswith('- '):
                old_values[key[2:]] = create_type_dependedent_output4plain(
                    value,
                )
        for key, value in dict4view.items():
            new_path = path + key[2:]
            if key.startswith(' '):
                if type(value) is dict:
                    new_path += '.'
                    view_dict(value, new_path)
            elif key.startswith('+ '):
                if key_list.count(key[2:]) == 1:
                    diff_list.append(
                        "Property '{a1}' was added with value: {a2}".format(
                            a1=new_path,
                            a2=create_type_dependedent_output4plain(value),
                        ),
                    )
                else:
                    diff_list.append(
                        "Property '{a}' was updated. From {b} to {c}".format(
                            a=new_path,
                            b=old_values[key[2:]],
                            c=new_values[key[2:]],
                        ),
                    )
            elif key.startswith('- '):
                if key_list.count(key[2:]) == 1:
                    diff_list.append(
                        "Property '{}' was removed".format(new_path),
                    )
    view_dict(diff, path)
    return '\n'.join(diff_list)
