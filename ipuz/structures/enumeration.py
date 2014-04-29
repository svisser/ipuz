import six

from ipuz.exceptions import IPUZException


def validate_enumeration(field_data):
    if not isinstance(field_data, six.string_types):
        return False
    return True


def validate_enumeration_field(field_name, field_data):
    if not validate_enumeration(field_data):
        raise IPUZException("Invalid {} value found".format(field_name))
