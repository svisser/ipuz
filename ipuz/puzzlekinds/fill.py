from ipuz.structures import (
    validate_crosswordvalues,
)
from ipuz.validators import (
    validate_dict_of_strings,
    validate_list_of_strings,
    validate_string,
)


IPUZ_FILL_VALIDATORS = {
    "start": validate_crosswordvalues,
    "solution": validate_crosswordvalues,
    "answer": validate_string,
    "answers": validate_list_of_strings,
    "misses": validate_dict_of_strings,
}
