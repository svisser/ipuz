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


IPUZ_ANSWER_VALIDATORS = {
    "choices": validate_list_of_strings,
    "randomize": validate_bool,
    "answer": validate_string,
    "answers": validate_list_of_strings,
    "enumeration": validate_enumeration_field,
    "enumerations": (validate_list, "Enumeration", validate_enumeration),
    "requiredanswers": validate_non_negative_int,
    "misses": validate_dict_of_strings,
    "guesses": validate_list_of_strings,
}
