from ipuz.exceptions import IPUZException
from ipuz.validators import validate_dict
from .common import validate_cells, validate_rect
from .stylespec import validate_stylespec


def validate_calcspec(field_data):
    def validate_value_key(value):
        return type(value) is int
    
    def validate_operator_key(value):
        return value in ["+", "-", "*", "/"]
    
    def validate_style_key(value):
        try:
            validate_stylespec(field_data["style"])
        except IPUZException:
            return False
        return True

    return validate_dict(field_data, {
        "rect": validate_rect,
        "cells": validate_cells,
        "value": validate_value_key,
        "operator": validate_operator_key,
        "style": validate_style_key,
    })
