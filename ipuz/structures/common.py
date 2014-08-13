from ipuz.exceptions import IPUZException


def validate_dimensions(field_name, field_data):
    if not isinstance(field_data, dict):
        raise IPUZException("Invalid {} value found".format(field_name))
    for key, value in field_data.items():
        if key not in ("width", "height"):
            raise IPUZException("Invalid {} value found".format(field_name))
    for key in ["width", "height"]:
        if key not in field_data:
            raise IPUZException(
                "Mandatory field {} of dimensions is missing".format(key)
            )
        if type(field_data[key]) is not int:
            raise IPUZException(
                "Invalid {} value in dimensions field found".format(key)
            )
        if field_data[key] < 1:
            raise IPUZException(
                "Field {} of dimensions is less than one".format(key)
            )


def validate_cells(field_data):
    if not isinstance(field_data, list) or not field_data:
        return False
    for element in field_data:
        if (not isinstance(element, list) or
                len(element) != 2 or
                not all(type(e) is int for e in element)):
            return False
    return True


def validate_rect(field_data):
    if not isinstance(field_data, list):
        return False
    if len(field_data) != 4 or not all(type(c) is int for c in field_data):
        return False
    if field_data[0] > field_data[2] or field_data[1] > field_data[3]:
        return False
    return True
