# This Python file uses the following encoding: utf-8

"""Functions for work with json files."""
# Constants
ADDED = 'added'
REMOVED = 'removed'
CHANGED = 'changed'
SAVED = 'saved'
NESTED = 'nested'

TYPE = 'type'
VALUE = 'value'
OLD_VALUE = 'old_value'


def check_dict(data):
    """Check and print dictionary in dict format.

    Checks for every key if its value is dictionary:
    if so calls recursively itself,
    in other case add value to new dictionary.

    Args:
        data(dict): dictionary for check.

    Returns:
        data_dict(dict): dictionary for check.
    """
    if isinstance(data, dict):
        data_dict = {}
        for key in data.keys():
            data_dict[key] = check_dict(data[key])
        return data_dict
    return data


def make_diff(data1, data2):
    """Generate difference function.

    Finds difference between two given files.

    Args:indents
        file_path1(str): path to 1st file,
        file_path2(str): path to 2st file,
        format(str): file format,

    Returns:
        diff(str) - the difference between two given files.
    """
    all_keys = data1.keys() & data2.keys()
    only_data1_keys = data1.keys() - data2.keys()
    only_data2_keys = data2.keys() - data1.keys()
    diff = {}
    for key in all_keys:
        cond1 = isinstance(data1[key], dict)
        cond2 = isinstance(data2[key], dict)
        if data1[key] == data2[key]:
            diff[key] = {TYPE: SAVED, VALUE: data2[key]}
        else:
            if cond1 and cond2:
                diff[key] = {TYPE: NESTED, VALUE: make_diff(data1[key], data2[key])}
            elif not cond1 and cond2:
                diff[key] = {TYPE: CHANGED, VALUE: check_dict(data2[key]), OLD_VALUE: data1[key]}
            elif cond1 and not cond2:
                diff[key] = {TYPE: CHANGED, VALUE: data2[key], OLD_VALUE: check_dict(data1[key])}
            else:
                diff[key] = {TYPE: CHANGED, VALUE: data2[key], OLD_VALUE: data1[key]}
    for key in only_data1_keys:
        diff[key] = {TYPE: REMOVED, VALUE: data1[key]}
    for key in only_data2_keys:
        diff[key] = {TYPE: ADDED, VALUE: data2[key]}
    return diff
