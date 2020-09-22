# This Python file uses the following encoding: utf-8

"""Functions load files."""

import json
import yaml
yaml.warnings({'YAMLLoadWarning': False})


def json_loader(file_path1, file_path2):
    """Load json 2 files."""
    return (json.load(open(file_path1)), json.load(open(file_path2)))


def yaml_loader(file_path1, file_path2):
    """Load yaml 2 files."""
    return (yaml.load(open(file_path1)), yaml.load(open(file_path2)))