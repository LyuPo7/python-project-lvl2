# This Python file uses the following encoding: utf-8

"""Json view module."""
import json


def view(diff):
    """View in json format difference between 2 files.

    Views in json format difference between 2 files.

    Args:
        diff(dict): difference between 2 files in json format

    Returns:
        str - difference between 2 files in str format.
    """
    return json.dumps(diff, sort_keys=True, indent=4)
