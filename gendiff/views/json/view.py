# This Python file uses the following encoding: utf-8

"""Json view function."""


def json_view_diff(diff):
    diff_list = []
    offset = '  '
    diff_list.append('{')

    def view_dict(dict4view, offset):
        key_counter = 1
        keys_number = len(dict4view.keys())
        for key, value in dict4view.items():
            if type(value) is not dict:
                if isinstance(value, bool):
                    str2write = "{arg1}\"{arg2}\": {arg3}".format(
                        arg1=offset,
                        arg2=key,
                        arg3=str(value).lower(),
                    )
                elif isinstance(value, str):
                    str2write = "{arg1}\"{arg2}\": \"{arg3}\"".format(
                        arg1=offset,
                        arg2=key,
                        arg3=str(value).lower(),
                    )
                else:
                    str2write = "{}\"{}\": {}".format(offset, key, value)
                if key_counter < keys_number:
                    str2write += ','
                diff_list.append(str2write)
                key_counter += 1
            else:
                diff_list.append("{}\"{}\": {}".format(offset, key, '{'))
                new_offset = offset + '    '
                view_dict(value, new_offset)
                str2write = '{}{}'.format(offset + '  ', '}')
                if key_counter < keys_number:
                    str2write += ','
                diff_list.append(str2write)
                key_counter += 1
    view_dict(diff, offset)
    diff_list.append('}')
    return '\n'.join(diff_list)