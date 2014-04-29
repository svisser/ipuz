import six

from ipuz.exceptions import IPUZException
from ipuz.structures import validate_stylespec


def validate_sudokugiven(field_data):
    def validate_given(given):
        if given is not None and type(given) is not int and not isinstance(given, six.string_types):
            return False
        return True
    if field_data is not None and type(field_data) is not int and not isinstance(field_data, six.string_types):
        return False
    if type(field_data) is dict:
        if not field_data:
            return False
        if not all(key in ("given", "style") for key in field_data):
            return False
        if "given" in field_data and not validate_given(field_data["given"]):
            return False
        if "style" in field_data:
            try:
                validate_stylespec(field_data["style"])
            except IPUZException:
                return False
    return True
