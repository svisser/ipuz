from ipuz.exceptions import IPUZException
from .common import (
    validate_cells,
    validate_rect,
)
from .stylespec import validate_stylespec_value
from ipuz.validators import validate_dict, validate_string


def validate_groupspec(field_data):
    return validate_dict(field_data, {
        "rect": validate_rect,
        "cells": validate_cells,
        "style": validate_stylespec_value,
    })


def validate_groupspec_dict(field_name, field_data):
    if not isinstance(field_data, dict):
        raise IPUZException("Invalid {} value found".format(field_name))
    for key, value in field_data.items():
        validate_string(field_name, key)
        if not key:
            raise IPUZException("Invalid {} value found".format(field_name))
        if not validate_groupspec(value):
            raise IPUZException("Invalid {} value found".format(field_name))
