# This Python file uses the following encoding: utf-8

"""Functions load files."""

import json
import yaml
yaml.warnings({'YAMLLoadWarning': False})


def generate_formats_dict():
    """Generate dictionary of the formats.

    Returns:
        dictionary(dict) - dictionary of the formats,
    """
    return {
        'json': json.load,
        'yaml': yaml.load,
    }


def file_loader(file_path1, file_path2, format):
    """Load yaml 2 files."""
    loaders = generate_formats_dict()
    return (
        loaders[format](open(file_path1)),
        loaders[format](open(file_path2))
    )
