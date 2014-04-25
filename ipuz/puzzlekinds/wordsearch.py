from ipuz.exceptions import IPUZException
from ipuz.validators import validate_bool, validate_dict_of_strings


def validate_dictionary(field_name, field_data):
    if field_data in [True, ""] or type(field_data) not in [str, unicode]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_showanswers(field_name, field_data):
    if field_data not in ["during", "after", None]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_time(field_name, field_data):
    if type(field_data) is not int or field_data < 0:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_points(field_name, field_data):
    if field_data not in ["linear", "log", None]:
        raise IPUZException("Invalid {} value found".format(field_name))


IPUZ_WORDSEARCH_VALIDATORS = {
    "dictionary": validate_dictionary,
    "showanswers": validate_showanswers,
    "time": validate_time,
    "points": validate_points,
    "zigzag": validate_bool,
    "retrace": validate_bool,
    "useall": validate_bool,
    "misses": validate_dict_of_strings,
}
