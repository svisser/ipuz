import types

from ipuz.exceptions import IPUZException
from ipuz.structures import validate_stylespec


def validate_sudokugiven(field_data):
    def validate_given(given):
        if type(given) not in [types.NoneType, int, str, unicode]:
            return False
        return True
    
    if type(field_data) not in [types.NoneType, int, str, unicode, dict]:
        return False
    if type(field_data) is dict:
        if not field_data:
            return False
        if not all(key in ("given", "style") for key in field_data):
            return False
        if "given" in field_data and not validate_given(field_data["given"]):
            return False
        if "style" in field_data:
            try:
                validate_stylespec(field_data["style"])
            except IPUZException:
                return False
    return True
