from ipuz.structures import (
    validate_enumeration,
    validate_enumeration_field,
)
from ipuz.validators import (
    validate_bool,
    validate_dict_of_strings,
    validate_list,
    validate_list_of_strings,
    validate_non_negative_int,
    validate_string,
)


def validate_enumerations(field_name, field_data):
    validate_list(field_name, field_data, "Enumeration", validate_enumeration)


IPUZ_ANSWER_VALIDATORS = {
    "choices": validate_list_of_strings,
    "randomize": validate_bool,
    "answer": validate_string,
    "answers": validate_list_of_strings,
    "enumeration": validate_enumeration_field,
    "enumerations": validate_enumerations,
    "requiredanswers": validate_non_negative_int,
    "misses": validate_dict_of_strings,
    "guesses": validate_list_of_strings,
}
