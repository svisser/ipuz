from ipuz.exceptions import IPUZException
from ipuz.stylespec import validate_stylespec


def validate_groupspec(field_data):
    if type(field_data) is not dict or not field_data:
        return False
    if not all(key in ["rect", "cells", "style"] for key in field_data.keys()):
        return False
    if "style" in field_data:
        validate_stylespec(field_data["style"])
    if "cells" in field_data:
        if type(field_data["cells"]) is not list or not field_data["cells"]:
            return False
        for element in field_data["cells"]:
            if type(element) is not list or len(element) != 2 or not all(type(e) is int for e in element):
                return False
    return True
