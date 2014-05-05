import six

from ipuz.exceptions import IPUZException
from ipuz.structures import validate_stylespec
from ipuz.validators import validate_dict


def validate_sudokuvalue(field_data):
    def validate_value(value):
        if value is not None and type(value) is not int and not isinstance(value, six.string_types):
            return False
        return True
    
    def validate_style_key(value):
        try:
            validate_stylespec(value)
        except IPUZException:
            return False
        return True

    if field_data is not None and type(field_data) is not int and not isinstance(field_data, six.string_types):
        return False
    if isinstance(field_data, dict):
        return validate_dict(field_data, {
            "value": validate_value,
            "style": validate_style_key,
        })
    return True
