from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_crosswordvalues,
    validate_dimensions,
    validate_groupspec_dict,
)
from ipuz.validators import (
    validate_bool,
    validate_dict_of_strings,
    validate_list_of_strings,
    validate_non_negative_int,
)


def validate_dictionary(field_name, field_data):
    if field_data in [True, ""] or type(field_data) not in [str, unicode]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_showanswers(field_name, field_data):
    if field_data not in ["during", "after", None]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_points(field_name, field_data):
    if field_data not in ["linear", "log", None]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_solution(field_name, field_data):
    if type(field_data) not in [str, unicode, dict, list]:
        raise IPUZException("Invalid {} value found".format(field_name))
    if type(field_data) is list:
        validate_list_of_strings(field_name, field_data)
    if type(field_data) is dict:
        validate_groupspec_dict(field_name, field_data)


IPUZ_WORDSEARCH_VALIDATORS = {
    "dimensions": validate_dimensions,
    "puzzle": validate_crosswordvalues,
    "solution": validate_solution,
    "dictionary": validate_dictionary,
    "saved": validate_list_of_strings,
    "showanswers": validate_showanswers,
    "time": validate_non_negative_int,
    "points": validate_points,
    "zigzag": validate_bool,
    "retrace": validate_bool,
    "useall": validate_bool,
    "misses": validate_dict_of_strings,
}
