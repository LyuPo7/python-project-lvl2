# This Python file uses the following encoding: utf-8

"""Default view module."""


def bool2json(value):
    """Convert Python bool to json bool

    Args:
        value(str): value for convert

    Returns:
        value(str): converted value.
        """
    if isinstance(value, bool):
        return str(value).lower()
    return value


def check_spec_symb(data):
    special_keys = {'-', '+', ' '}
    if special_keys.intersection(data.keys()):
        return True
    return False


def view(diff):
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

    def view_default(dict4view, offset):
        """Check and print dictionary in dict format.

        Checks if values of the dictionary are dictionaries too:
        if so calls recursively itself,
        in other case print value in dict format.

        Args:
            dict4view(dict): dictionary for check,
            offset(str): offset for print value.
        """
        for key in sorted(dict4view.keys()):
            if not isinstance(dict4view[key], dict):
                diff_list.append(
                    '{arg1}  {arg2}: {arg3}'.format(
                        arg1=offset,
                        arg2=key,
                        arg3=bool2json(dict4view[key]),
                    ),
                )
            else:
                if check_spec_symb(dict4view[key]):
                    for k in sorted(dict4view[key].keys()):
                        if isinstance(dict4view[key][k], dict):
                            diff_list.append(
                                '{arg1}{arg2}{arg3}: {arg4}'.format(
                                    arg1=offset,
                                    arg2=k.ljust(2),
                                    arg3=key,
                                    arg4='{',
                                ),
                            )
                            new_offset = offset + ' ' * 4
                            view_default(dict4view[key][k], new_offset)
                            diff_list.append(
                                '{arg1}{arg2}'.format(
                                    arg1=offset + ' ' * 2,
                                    arg2='}'
                                ),
                            )
                        else:
                            diff_list.append(
                                '{arg1}{arg2}{arg3}: {arg4}'.format(
                                    arg1=offset,
                                    arg2=k.ljust(2),
                                    arg3=key,
                                    arg4=bool2json(dict4view[key][k]),
                                ),
                            )
                else:
                    diff_list.append(
                        '{arg1}  {arg2}: {arg3}'.format(
                            arg1=offset,
                            arg2=key,
                            arg3='{',
                        ),
                    )
                    new_offset = offset + ' ' * 4
                    view_default(dict4view[key], new_offset)
                    diff_list.append(
                        '{arg1}{arg2}'.format(
                            arg1=offset + ' ' * 2,
                            arg2='}'
                        ),
                    )
    view_default(diff, offset)
    diff_list.append('}')
    return '\n'.join(diff_list)
