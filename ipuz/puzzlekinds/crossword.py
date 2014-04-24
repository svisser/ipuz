from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_crosswordvalue,
    validate_groupspec,
    validate_labeledcell,
)
from ipuz.validators import validate_bool



def validate_dimensions(field_name, field_data):
    for key in ["width", "height"]:
        if key not in field_data:
            raise IPUZException(
                "Mandatory field {} of dimensions is missing".format(key)
            )
        if field_data[key] < 1:
            raise IPUZException(
                "Field {} of dimensions is less than one".format(key)
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
        raise IPUZException("Invalid zones value found")
    for element in field_data:
        if not validate_groupspec(element):
            raise IPUZException("Invalid GroupSpec in zones element found")


def validate_clueplacement(field_name, field_data):
    if field_data not in [None, "before", "after", "blocks"]:
        raise IPUZException("Invalid clueplacement value found")


def validate_answer(field_name, field_data):
    if type(field_data) not in [str, unicode] or field_data == "":
        raise IPUZException("Invalid answer value found")


def validate_answers(field_name, field_data):
    if type(field_data) is not list or not field_data:
        raise IPUZException("Invalid answers value found")
    for element in field_data:
        try:
            validate_answer(field_name, element)
        except IPUZException:
            raise IPUZException("Invalid answers value found")


IPUZ_CROSSWORD_VALIDATORS = {
    "dimensions": validate_dimensions,
    "puzzle": validate_puzzle,
    "saved": validate_crosswordvalues,
    "solution": validate_crosswordvalues,
    "zones": validate_zones,
    "showenumerations": validate_bool,
    "clueplacement": validate_clueplacement,
    "answer": validate_answer,
    "answers": validate_answers,
}
