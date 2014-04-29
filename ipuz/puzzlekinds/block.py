from ipuz.structures import (
    validate_dimensions,
    validate_groupspec_dict,
    validate_styledcell,
)
from ipuz.validators import (
    validate_bool,
    validate_list_of_lists,
)


IPUZ_BLOCK_VALIDATORS = {
    "dimensions": validate_dimensions,
    "slide": validate_bool,
    "move": validate_bool,
    "rotatable": validate_bool,
    "flippable": validate_bool,
    "field": (validate_list_of_lists, "StyledCell", validate_styledcell),
    "enter": validate_groupspec_dict,
    "start": validate_groupspec_dict,
    "saved": validate_groupspec_dict,
    "end": validate_groupspec_dict,
    "exit": validate_groupspec_dict,
}
