# This Python file uses the following encoding: utf-8

"""Functions for work with json files."""

from gendiff.file_loader.file_loader import file_loader


def check_dict(data):
    data_dict = {}
    for key in data.keys():
        if type(data[key]) is dict:
            data_dict['  {}'.format(key)] = check_dict(data[key])
        else:
            data_dict['  {}'.format(key)] = data[key]
    return data_dict


def make_diff(data_file1, data_file2):
    """Generate difference function.

    Finds difference between two given files.

    Args:
        file_path1(str): path to 1st file,
        file_path2(str): path to 2st file,
        format(str): file format,

    Returns:
        diff(str) - the difference between two given files.
    """
    def check_key(data1, data2):
        keys1 = data1.keys()
        keys2 = data2.keys()
        all_keys = set(keys1).union(keys2)
        diff = {}
        for key in all_keys:
            if key in keys1 and key in keys2:
                if data1[key] == data2[key]:
                    diff['  {}'.format(key)] = data1[key]
                else:
                    if type(data2[key]) is dict and type(data1[key]) is dict:
                        diff['  {}'.format(key)] = check_key(
                            data1[key],
                            data2[key],
                        )
                    else:
                        cond1 = type(data1[key]) is not dict
                        cond2 = type(data2[key]) is not dict
                        if cond1 and cond2:
                            diff['+ {}'.format(key)] = data2[key]
                            diff['- {}'.format(key)] = data1[key]
                        elif not cond2 and cond1:
                            diff['- {}'.format(key)] = data1[key]
                            diff['+ {}'.format(key)] = check_dict(data2[key])
                        elif cond2 and not cond1:
                            diff['+ {}'.format(key)] = data2[key]
                            diff['- {}'.format(key)] = check_dict(data1[key])
            elif key in keys1 and key not in keys2:
                if type(data1[key]) is dict:
                    diff['- {}'.format(key)] = check_dict(data1[key])
                else:
                    diff['- {}'.format(key)] = data1[key]
            elif key not in keys1 and key in keys2:
                if type(data2[key]) is dict:
                    diff['+ {}'.format(key)] = check_dict(data2[key])
                else:
                    diff['+ {}'.format(key)] = data2[key]
        return diff
    return check_key(data_file1, data_file2)


def view_diff(diff):
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


def generate_diff(file_path1, file_path2, format):
    data_file1, data_file2 = file_loader(file_path1, file_path2, format)
    return view_diff(make_diff(data_file1, data_file2))
