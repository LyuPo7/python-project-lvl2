# This Python file uses the following encoding: utf-8

"""Json view module."""

from gendiff.accessory.functions import create_type_dependedent_output4json


def json_view_diff(diff):
    """View in json format difference between 2 files.

    Views in json format difference between 2 files.

    Args:
        diff(dict): difference between 2 files in json format

    Returns:
        str - difference between 2 files in str format.
    """
    diff_list = []
    offset = '  '
    diff_list.append('{')

    def view_dict(dict4view, offset):
        """Check and print dictionary in json format.

        Checks if values of the dictionary are dictionaries too:
        if so calls recursively itself,
        in other case print value in json format.

        Args:
            dict4view(dict): dictionary for check,
            offset(str): offset for print value.
        """
        key_counter = 1
        keys_number = len(dict4view.keys())
        for key, value in dict4view.items():
            if type(value) is not dict:
                str2write = "{arg1}\"{arg2}\": {arg3}".format(
                    arg1=offset,
                    arg2=key,
                    arg3=create_type_dependedent_output4json(value)
                )
                if key_counter < keys_number:
                    str2write += ','
                diff_list.append(str2write)
                key_counter += 1
            else:
                diff_list.append(
                    "{arg1}\"{arg2}\": {arg3}".format(
                        arg1=offset,
                        arg2=key,
                        arg3='{',
                    ),
                )
                new_offset = offset + ' ' * 4
                view_dict(value, new_offset)
                str2write = '{arg1}{arg2}'.format(
                    arg1=offset + ' ' * 2,
                    arg2='}',
                )
                if key_counter < keys_number:
                    str2write += ','
                diff_list.append(str2write)
                key_counter += 1
    view_dict(diff, offset)
    diff_list.append('}')
    return '\n'.join(diff_list)
