from ipuz.exceptions import IPUZException
from ipuz.structures import validate_enumeration
from ipuz.validators import (
    validate_bool,
    validate_dict_of_strings,
    validate_int,
    validate_list_of_strings,
    validate_string,
)


def validate_enumeration_field(field_name, field_data):
    if not validate_enumeration(field_data):
        raise IPUZException("Invalid {} value found".format(field_name))


IPUZ_ANSWER_VALIDATORS = {
    "choices": validate_list_of_strings,
    "randomize": validate_bool,
    "answer": validate_string,
    "answers": validate_list_of_strings,
    "enumeration": validate_enumeration_field,
    "requiredanswers": validate_int,
    "misses": validate_dict_of_strings,
    "guesses": validate_list_of_strings,
}
