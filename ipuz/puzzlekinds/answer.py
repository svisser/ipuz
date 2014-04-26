from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_enumeration,
    validate_enumeration_field,
)
from ipuz.validators import (
    validate_bool,
    validate_dict_of_strings,
    validate_int,
    validate_list_of_strings,
    validate_string,
)


def validate_enumerations(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if not validate_enumeration(element):
            raise IPUZException("Invalid Enumeration in {} element found".format(field_name))


IPUZ_ANSWER_VALIDATORS = {
    "choices": validate_list_of_strings,
    "randomize": validate_bool,
    "answer": validate_string,
    "answers": validate_list_of_strings,
    "enumeration": validate_enumeration_field,
    "enumerations": validate_enumerations,
    "requiredanswers": validate_int,
    "misses": validate_dict_of_strings,
    "guesses": validate_list_of_strings,
}
