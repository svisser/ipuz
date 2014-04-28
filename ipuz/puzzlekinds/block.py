from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_dimensions,
    validate_groupspec_dict,
    validate_styledcell,
)
from ipuz.validators import (
    validate_bool,
    validate_string,
)


def validate_field(field_name, field_data):
    if type(field_data) is not list or any(type(e) is not list for e in field_data):
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        for element in line:
            if not validate_styledcell(element):
                raise IPUZException("Invalid StyledCell in {} element found".format(field_name))


IPUZ_BLOCK_VALIDATORS = {
    "dimensions": validate_dimensions,
    "slide": validate_bool,
    "move": validate_bool,
    "rotatable": validate_bool,
    "flippable": validate_bool,
    "field": validate_field,
    "enter": validate_groupspec_dict,
    "start": validate_groupspec_dict,
    "saved": validate_groupspec_dict,
    "end": validate_groupspec_dict,
    "exit": validate_groupspec_dict,
}
