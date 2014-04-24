from ipuz.exceptions import IPUZException
from ipuz.validators import validate_bool


def validate_dictionary(field_name, field_data):
    if field_data in [True, ""] or type(field_data) not in [str, unicode]:
        raise IPUZException("Invalid dictionary value found")


def validate_showanswers(field_name, field_data):
    if field_data not in ["during", "after", None]:
        raise IPUZException("Invalid showanswers value found")


def validate_time(field_name, field_data):
    if type(field_data) is not int or field_data < 0:
        raise IPUZException("Invalid time value found")


def validate_points(field_name, field_data):
    if field_data not in ["linear", "log", None]:
        raise IPUZException("Invalid points value found")


def validate_misses(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid misses value found")
    for key, value in field_data.items():
        if type(key) not in [str, unicode] or type(value) not in [str, unicode]:
            raise IPUZException("Invalid misses value found")


IPUZ_WORDSEARCH_VALIDATORS = {
    "dictionary": validate_dictionary,
    "showanswers": validate_showanswers,
    "time": validate_time,
    "points": validate_points,
    "zigzag": validate_bool,
    "retrace": validate_bool,
    "useall": validate_bool,
    "misses": validate_misses,
}
