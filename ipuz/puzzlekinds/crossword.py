from ipuz.structures import (
    validate_clues,
    validate_crosswordvalues,
    validate_dimensions,
    validate_enumeration,
    validate_enumeration_field,
    validate_groupspec,
    validate_labeledcell,
)
from ipuz.validators import (
    validate_bool,
    validate_dict_of_strings,
    validate_elements,
    validate_list,
    validate_list_of_lists,
    validate_list_of_strings,
    validate_string,
)


IPUZ_CROSSWORD_VALIDATORS = {
    "dimensions": validate_dimensions,
    "puzzle": (validate_list_of_lists, "LabeledCell", validate_labeledcell),
    "saved": validate_crosswordvalues,
    "solution": validate_crosswordvalues,
    "zones": (validate_list, "GroupSpec", validate_groupspec),
    "clues": validate_clues,
    "showenumerations": validate_bool,
    "clueplacement": (validate_elements, [None, "before", "after", "blocks"]),
    "answer": validate_string,
    "answers": validate_list_of_strings,
    "enumeration": validate_enumeration_field,
    "enumerations": (validate_list, "Enumeration", validate_enumeration),
    "misses": validate_dict_of_strings,
}
