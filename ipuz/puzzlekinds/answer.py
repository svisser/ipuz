from ipuz.exceptions import IPUZException
from ipuz.validators import (
    validate_bool,
    validate_dict_of_strings,
    validate_int,
    validate_list_of_strings,
)


def validate_answer(field_name, field_data):
    if type(field_data) not in [str, unicode]:
        raise IPUZException("Invalid {} value found".format(field_name))


IPUZ_ANSWER_VALIDATORS = {
    "choices": validate_list_of_strings,
    "randomize": validate_bool,
    "answer": validate_answer,
    "answers": validate_list_of_strings,
    "requiredanswers": validate_int,
    "misses": validate_dict_of_strings,
    "guesses": validate_list_of_strings,
}
