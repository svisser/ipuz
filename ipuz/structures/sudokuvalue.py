import six

from ipuz.exceptions import IPUZException
from ipuz.structures import validate_stylespec


def validate_sudokuvalue(field_data):
    def validate_value(value):
        if value is not None and type(value) is not int and not isinstance(value, six.string_types):
            return False
        return True

    if field_data is not None and type(field_data) is not int and not isinstance(field_data, six.string_types):
        return False
    if type(field_data) is dict:
        if not field_data:
            return False
        if not all(key in ("value", "style") for key in field_data):
            return False
        if "value" in field_data and not validate_value(field_data["value"]):
            return False
        if "style" in field_data:
            try:
                validate_stylespec(field_data["style"])
            except IPUZException:
                return False
    return True
