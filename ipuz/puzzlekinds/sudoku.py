from ipuz.exceptions import IPUZException
from ipuz.validators import validate_bool


def validate_charset(field_name, field_data):
    if type(field_data) not in [str, unicode] or (len(field_data) != 9):
        raise IPUZException("Invalid charset value found")


def validate_cageborder(field_name, field_data):
    if field_data not in ["thick", "dashed"]:
        raise IPUZException("Invalid cageborder value found")


IPUZ_SUDOKU_VALIDATORS = {
    "charset": validate_charset,
    "displaycharset": validate_bool,
    "boxes": validate_bool,
    "showoperators": validate_bool,
    "cageborder": validate_cageborder,
}
