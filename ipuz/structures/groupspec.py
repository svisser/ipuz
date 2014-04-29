from ipuz.exceptions import IPUZException
from .common import (
    validate_cells,
    validate_rect,
)
from .stylespec import validate_stylespec
from ipuz.validators import validate_string


def validate_groupspec(field_data):
    if type(field_data) is not dict or not field_data:
        return False
    if not all(key in ["rect", "cells", "style"] for key in field_data):
        return False
    if "style" in field_data:
        try:
            validate_stylespec(field_data["style"])
        except IPUZException:
            return False
    if "cells" in field_data and not validate_cells(field_data["cells"]):
        return False
    if "rect" in field_data and not validate_rect(field_data["rect"]):
        return False
    return True


def validate_groupspec_dict(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for key, value in field_data.items():
        validate_string(field_name, key)
        if not key:
            raise IPUZException("Invalid {} value found".format(field_name))
        if not validate_groupspec(value):
            raise IPUZException("Invalid {} value found".format(field_name))
