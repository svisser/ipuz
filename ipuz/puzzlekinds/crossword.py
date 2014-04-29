from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_clue,
    validate_crosswordvalues,
    validate_dimensions,
    validate_direction,
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


def validate_clues(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for direction, clues in field_data.items():
        if not validate_direction(direction) or type(clues) is not list or not clues:
            raise IPUZException("Invalid {} value found".format(field_name))
        for clue in clues:
            if not validate_clue(clue):
                raise IPUZException("Invalid Clue in {} element found".format(field_name))


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
