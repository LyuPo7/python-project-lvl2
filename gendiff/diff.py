# This Python file uses the following encoding: utf-8

"""Functions for work with json files."""


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

    Args:
        file_path1(str): path to 1st file,
        file_path2(str): path to 2st file,
        format(str): file format,

    Returns:
        diff(str) - the difference between two given files.
    """
    skeys1 = set(data1.keys())
    skeys2 = set(data2.keys())
    diff = {}
    for key in skeys1.intersection(skeys2):
        if data1[key] == data2[key]:
            diff[key] = {' ': data2[key]}
        else:
            cond1 = isinstance(data1[key], dict)
            cond2 = isinstance(data2[key], dict)
            if cond1 and cond2:
                diff[key] = make_diff(data1[key], data2[key])
            elif not cond1 and cond2:
                diff[key] = {'+': check_dict(data2[key]), '-': data1[key]}
            elif cond1 and not cond2:
                diff[key] = {'+': data2[key], '-': check_dict(data1[key])}
            else:
                diff[key] = {'+': data2[key], '-': data1[key]}
    for key in skeys1.difference(skeys2):
        diff[key] = {'-': data1[key]}
    for key in skeys2.difference(skeys1):
        diff[key] = {'+': data2[key]}
    return diff
