from ipuz.exceptions import IPUZException
from .common import (
    validate_cells,
    validate_rect,
)
from .stylespec import validate_stylespec
from ipuz.validators import validate_dict, validate_string


def validate_groupspec(field_data):
    def validate_style_key(value):
        try:
            validate_stylespec(field_data["style"])
        except IPUZException:
            return False
        return True

    return validate_dict(field_data, {
        "rect": validate_rect,
        "cells": validate_cells,
        "style": validate_style_key,
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
