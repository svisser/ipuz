import types

from ipuz.exceptions import IPUZException
from .stylespec import validate_stylespec


def validate_labeledcell(field_data):
    def validate_cell(cell):
        if type(cell) not in [types.NoneType, int, str, unicode, dict]:
            return False
        if type(cell) is dict and not cell:
            return False
        return True
    if not validate_cell(field_data):
        return False
    if type(field_data) is dict:
        if not all(key in ["cell", "style", "value"] for key in field_data):
            return False
        if "cell" in field_data and not validate_cell(field_data["cell"]):
            return False
        if "value" in field_data and type(field_data["value"]) not in [str, unicode]:
            return False
        if "style" in field_data:
            try:
                validate_stylespec(field_data["style"])
            except IPUZException:
                return False
    return True
