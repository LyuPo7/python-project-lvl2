# This Python file uses the following encoding: utf-8

"""Dict view module."""

from gendiff.accessory.functions import bool2json


def dict_view_diff(diff):
    """View in dict format difference between 2 files.

    Views in dict format difference between 2 files.

    Args:
        diff(dict): difference between 2 files in dict format

    Returns:
        str - difference between 2 files in str format.
    """
    diff_list = []
    offset = '  '
    diff_list.append('{')

    def view_dict(dict4view, offset):
        """Check and print dictionary in dict format.

        Checks if values of the dictionary are dictionaries too:
        if so calls recursively itself,
        in other case print value in dict format.

        Args:
            dict4view(dict): dictionary for check,
            offset(str): offset for print value.
        """
        for key, value in dict4view.items():
            if type(value) is not dict:
                diff_list.append(
                    '{arg1}{arg2}: {arg3}'.format(
                        arg1=offset,
                        arg2=key,
                        arg3=bool2json(value),
                    ),
                )
            else:
                diff_list.append(
                    '{arg1}{arg2}: {arg3}'.format(
                        arg1=offset,
                        arg2=key,
                        arg3='{',
                    ),
                )
                new_offset = offset + ' ' * 4
                view_dict(value, new_offset)
                diff_list.append(
                    '{arg1}{arg2}'.format(
                        arg1=offset + ' ' * 2,
                        arg2='}'
                    ),
                )
    view_dict(diff, offset)
    diff_list.append('}')
    return '\n'.join(diff_list)
