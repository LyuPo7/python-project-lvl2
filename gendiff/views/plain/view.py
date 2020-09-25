# This Python file uses the following encoding: utf-8

"""Plain view function."""


def plain_view_diff(diff):
    diff_list = []
    path = ''

    def view_dict(dict4view, path):
        key_list = [key[2:] for key in dict4view.keys()]
        old_values = {}
        new_values = {}
        for key, value in dict4view.items():
            if key.startswith('+ '):
                if type(value) is dict:
                    new_values[key[2:]] = '[complex value]'
                elif isinstance(value, bool):
                    new_values[key[2:]] = str(value).lower()
                else:
                    new_values[key[2:]] = "'{}'".format(value)
            if key.startswith('- '):
                if type(value) is dict:
                    old_values[key[2:]] = '[complex value]'
                elif isinstance(value, bool):
                    old_values[key[2:]] = str(value).lower()
                else:
                    old_values[key[2:]] = "'{}'".format(value)
        for key, value in dict4view.items():
            new_path = path + key[2:]
            if key.startswith(' '):
                if type(value) is dict:
                    new_path += '.'
                    view_dict(value, new_path)
            elif key.startswith('+ '):
                if key_list.count(key[2:]) == 1:
                    if type(value) is not dict:
                        if isinstance(value, bool):
                            diff_list.append(
                                "Property '{arg1}' was added with value: {arg2}".format(
                                    arg1=new_path,
                                    arg2=str(value).lower(),
                                )
                            )
                        else:
                            diff_list.append(
                                "Property '{arg1}' was added with value: '{arg2}'".format(
                                    arg1=new_path,
                                    arg2=value,
                                )
                            )
                    else:
                        diff_list.append(
                            "Property '{}' was added with value: [complex value]".format(
                                new_path,
                            )
                        )
                else:
                    diff_list.append(
                        "Property '{arg1}' was updated. From {arg2} to {arg3}".format(
                            arg1=new_path,
                            arg2=old_values[key[2:]],
                            arg3=new_values[key[2:]],
                        ),
                    )
            elif key.startswith('- '):
                if key_list.count(key[2:]) == 1:
                    diff_list.append(
                        "Property '{}' was removed".format(new_path),
                    )
    view_dict(diff, path)
    return '\n'.join(diff_list)