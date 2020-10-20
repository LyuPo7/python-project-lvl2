# This Python file uses the following encoding: utf-8

"""Package of the project."""
from gendiff.views import plain
from gendiff.views import default
from gendiff.views import json
from gendiff import views


FORMATS_DICT = {
    views.DEFAULT: default.view,
    views.JSON: json.view,
    views.PLAIN: plain.view,
}
