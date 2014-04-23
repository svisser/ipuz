from ipuz.exceptions import IPUZException
from .stylespec import validate_stylespec


def validate_groupspec(field_data):
    if type(field_data) is not dict or not field_data:
        return False
    if not all(key in ["rect", "cells", "style"] for key in field_data.keys()):
        return False
    if "style" in field_data:
        try:
            validate_stylespec(field_data["style"])
        except IPUZException:
            return False
    if "cells" in field_data:
        if type(field_data["cells"]) is not list or not field_data["cells"]:
            return False
        for element in field_data["cells"]:
            if type(element) is not list or len(element) != 2 or not all(type(e) is int for e in element):
                return False
    if "rect" in field_data:
        if type(field_data["rect"]) is not list:
            return False
        if len(field_data["rect"]) != 4 or not all(type(c) is int for c in field_data["rect"]):
            return False
        if field_data["rect"][0] > field_data["rect"][2] or field_data["rect"][1] > field_data["rect"][3]:
            return False
    return True
