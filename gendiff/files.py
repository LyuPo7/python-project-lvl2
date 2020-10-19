# This Python file uses the following encoding: utf-8

"""Functions load files."""

import json
import yaml
import os


def formats():
    """Generate dictionary of the formats.

    Returns:
        dictionary(dict) - dictionary of the formats,
    """
    return {
        '.json': json.load,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load,
    }


def load(file_path):
    """Load file in correct format.

    Returns:
        dictionary(tuple) - tuple of dictionaries,
    """
    _, ext = os.path.splitext(file_path)
    loader = formats().get(ext.lower())
    if not loader:
        print('Invalid extension of file: {}'.format(file_path))
    else:
        return loader(open(file_path))
