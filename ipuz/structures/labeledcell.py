import six

from ipuz.exceptions import IPUZException
from .stylespec import validate_stylespec


def validate_labeledcell(field_data):
    def validate_cell(cell):
        if (cell is not None and
                type(cell) not in [int, dict] and
                not isinstance(cell, six.string_types)):
            return False
        if isinstance(cell, dict) and not cell:
            return False
        return True
    if not validate_cell(field_data):
        return False
    if isinstance(field_data, dict):
        if not all(key in ("cell", "style", "value") for key in field_data):
            return False
        if ("cell" in field_data and
                (isinstance(field_data["cell"], dict) or
                 not validate_cell(field_data["cell"]))):
            return False
        if ("value" in field_data and
                not isinstance(field_data["value"], six.string_types)):
            return False
        if "style" in field_data:
            try:
                validate_stylespec(field_data["style"])
            except IPUZException:
                return False
    return True
