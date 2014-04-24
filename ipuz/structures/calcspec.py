from ipuz.exceptions import IPUZException
from .stylespec import validate_stylespec


def validate_calcspec(field_data):
    if type(field_data) is not dict or not field_data:
        return False
    valid_keys = ("rect", "cells", "value", "operator", "style")
    if any(key not in valid_keys for key in field_data):
        return False
    if "value" in field_data:
        if type(field_data["value"]) is not int:
            return False
    if "operator" in field_data and field_data["operator"] not in ["+", "-", "*", "/"]:
        return False
    if "style" in field_data:
        try:
            validate_stylespec(field_data["style"])
        except IPUZException:
            return False
    return True
