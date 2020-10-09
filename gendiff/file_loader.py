# This Python file uses the following encoding: utf-8

"""Functions load files."""

import json
import yaml
import os


def generate_formats_dict():
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
    loaders = generate_formats_dict()
    file_name1, ext = os.path.splitext(file_path)
    loader = loaders[ext.lower()]
    return loader(open(file_path))
