from ipuz.validators import validate_dict
from .common import validate_cells, validate_rect
from .stylespec import validate_stylespec_value


def validate_calcspec(field_data):
    def validate_value_key(value):
        return type(value) is int

    def validate_operator_key(value):
        return value in ["+", "-", "*", "/"]

    return validate_dict(field_data, {
        "rect": validate_rect,
        "cells": validate_cells,
        "value": validate_value_key,
        "operator": validate_operator_key,
        "style": validate_stylespec_value,
    })
