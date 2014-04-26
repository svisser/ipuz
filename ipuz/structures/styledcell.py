import types

from ipuz.exceptions import IPUZException
from .stylespec import validate_stylespec


def validate_styledcell(field_data):
    if type(field_data) not in [types.NoneType, int, str, unicode, dict]:
        return False
    if type(field_data) is dict:
        if not field_data:
            return False
        if not all(key in ("cell", "style") for key in field_data):
            return False
        if "cell" in field_data and type(field_data["cell"]) not in [types.NoneType, int, str, unicode]:
            return False
        if "style" in field_data:
            try:
                validate_stylespec(field_data["style"])
            except IPUZException:
                return False
    return True
