from ipuz.structures import (
    validate_clues,
    validate_crosswordvalues,
    validate_labeledcell,
)
from ipuz.validators import validate_list_of_lists


IPUZ_ACROSTIC_VALIDATORS = {
    "puzzle": (validate_list_of_lists, "LabeledCell", validate_labeledcell),
    "solution": validate_crosswordvalues,
    "clues": validate_clues,
}
