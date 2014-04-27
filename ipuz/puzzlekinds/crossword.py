from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_clue,
    validate_crosswordvalue,
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
    validate_list_of_strings,
    validate_string,
)


def validate_puzzle(field_name, field_data):
    if type(field_data) is not list or any(type(e) is not list for e in field_data):
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        for element in line:
            if not validate_labeledcell(element):
                raise IPUZException("Invalid LabeledCell in {} element found".format(field_name))


def validate_crosswordvalues(field_name, field_data):
    if type(field_data) is not list or any(type(e) is not list for e in field_data):
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        for element in line:
            if not validate_crosswordvalue(element):
                raise IPUZException("Invalid CrosswordValue in {} element found".format(field_name))


def validate_zones(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if not validate_groupspec(element):
            raise IPUZException("Invalid GroupSpec in {} element found".format(field_name))


def validate_clueplacement(field_name, field_data):
    if field_data not in [None, "before", "after", "blocks"]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_clues(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for direction, clues in field_data.items():
        if not validate_direction(direction) or type(clues) is not list or not clues:
            raise IPUZException("Invalid {} value found".format(field_name))
        for clue in clues:
            if not validate_clue(clue):
                raise IPUZException("Invalid Clue in {} element found".format(field_name))


def validate_enumerations(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if not validate_enumeration(element):
            raise IPUZException("Invalid Enumeration in {} element found".format(field_name))


IPUZ_CROSSWORD_VALIDATORS = {
    "dimensions": validate_dimensions,
    "puzzle": validate_puzzle,
    "saved": validate_crosswordvalues,
    "solution": validate_crosswordvalues,
    "zones": validate_zones,
    "clues": validate_clues,
    "showenumerations": validate_bool,
    "clueplacement": validate_clueplacement,
    "answer": validate_string,
    "answers": validate_list_of_strings,
    "enumeration": validate_enumeration_field,
    "enumerations": validate_enumerations,
    "misses": validate_dict_of_strings,
}
