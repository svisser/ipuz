import six

from ipuz.exceptions import IPUZException
from .direction import validate_direction
from .stylespec import validate_stylespec
from ipuz.validators import validate_list_of_lists


def validate_crosswordvalue(field_data):
    if field_data is not None and type(field_data) not in [int, list, dict] and not isinstance(field_data, six.string_types):
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
    validate_list_of_lists(field_name, field_data, "CrosswordValue", validate_crosswordvalue)
