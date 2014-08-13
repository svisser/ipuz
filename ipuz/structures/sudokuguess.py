import six


def validate_sudokuguess(field_data):
    if (type(field_data) not in [int, list] and
            not isinstance(field_data, six.string_types)):
        return False
    return True
