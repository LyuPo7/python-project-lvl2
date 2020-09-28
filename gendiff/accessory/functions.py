# This Python file uses the following encoding: utf-8

"""Supporting functions module."""


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


def create_type_dependedent_output4plain(value):
    """Convert value to plain format.

    Returns output in dependence of type of value.

    Args:
        value(): value for convert

    Returns:
        value(str): converted value.
        """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return "'{}'".format(value)


def create_type_dependedent_output4json(value):
    """Convert value to json format.

    Returns output in dependence of type of value.

    Args:
        value(): value for convert

    Returns:
        value(str): converted value.
        """
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return "\"{}\"".format(str(value).lower())
    else:
        return value
