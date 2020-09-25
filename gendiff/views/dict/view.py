# This Python file uses the following encoding: utf-8

"""Json view function."""


def dict_view_diff(diff):
    diff_list = []
    offset = '  '
    diff_list.append('{')

    def view_dict(dict4view, offset):
        for key, value in dict4view.items():
            if type(value) is not dict:
                if isinstance(value, bool):
                    diff_list.append( 
                        '{arg1}{arg2}: {arg3}'.format(
                            arg1=offset,
                            arg2=key,
                            arg3=str(value).lower(),
                        ),
                    )
                else:
                    diff_list.append('{}{}: {}'.format(offset, key, value))
            else:
                diff_list.append('{}{}: {}'.format(offset, key, '{'))
                new_offset = offset + '    '
                view_dict(value, new_offset)
                diff_list.append('{}{}'.format(offset + '  ', '}'))
    view_dict(diff, offset)
    diff_list.append('}')
    return '\n'.join(diff_list)