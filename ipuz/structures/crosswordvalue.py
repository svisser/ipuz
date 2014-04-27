import types

from ipuz.exceptions import IPUZException
from .direction import validate_direction
from .stylespec import validate_stylespec


def validate_crosswordvalue(field_data):
    if type(field_data) not in [types.NoneType, str, unicode, int, list, dict]:
        return False
    if type(field_data) is int and field_data != 0:
        return False
    if type(field_data) is list:
        for element in field_data:
            if not validate_crosswordvalue(element):
                return False
    if type(field_data) is dict:
        if not field_data:
            return False
        for key, value in field_data.items():
            if key not in ("style", "value") and not validate_direction(key):
                return False
            if key == "value" and not validate_crosswordvalue(value):
                return False
            elif key == "style":
                try:
                    validate_stylespec(value)
                except IPUZException:
                    return False
            elif not validate_crosswordvalue(value):
                return False
    return True


def validate_crosswordvalues(field_name, field_data):
    if type(field_data) is not list or any(type(e) is not list for e in field_data):
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        for element in line:
            if not validate_crosswordvalue(element):
                raise IPUZException("Invalid CrosswordValue in {} element found".format(field_name))
