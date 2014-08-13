import six

from .direction import validate_direction
from .stylespec import validate_stylespec_value
from ipuz.validators import validate_list_of_lists


def validate_crosswordvalue(field_data):
    if (field_data is not None and
            type(field_data) not in [int, list, dict] and
            not isinstance(field_data, six.string_types)):
        return False
    if type(field_data) is int and field_data != 0:
        return False
    if isinstance(field_data, list):
        for element in field_data:
            if not validate_crosswordvalue(element):
                return False
    if isinstance(field_data, dict):
        if not field_data:
            return False
        for key, value in field_data.items():
            if key not in ("style", "value") and not validate_direction(key):
                return False
            if key == "value" and (
                    isinstance(value, dict) or
                    not validate_crosswordvalue(value)):
                return False
            elif key == "style" and not validate_stylespec_value(value):
                return False
            elif not validate_crosswordvalue(value):
                return False
    return True


def validate_crosswordvalues(field_name, field_data):
    validate_list_of_lists(
        field_name, field_data, "CrosswordValue", validate_crosswordvalue
    )
