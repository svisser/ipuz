from ipuz.structures import (
    validate_calcspec,
    validate_groupspec,
    validate_sudokugiven,
    validate_sudokuguess,
    validate_sudokuvalue,
)
from ipuz.validators import (
    validate_bool,
    validate_elements,
    validate_list,
    validate_list_of_lists,
    validate_string,
)


IPUZ_SUDOKU_VALIDATORS = {
    "charset": validate_string,
    "displaycharset": validate_bool,
    "boxes": validate_bool,
    "showoperators": validate_bool,
    "cageborder": (validate_elements, ["thick", "dashed"]),
    "puzzle": (validate_list_of_lists, "SudokuGiven", validate_sudokugiven),
    "saved": (validate_list_of_lists, "SudokuGuess", validate_sudokuguess),
    "solution": (validate_list_of_lists, "SudokuValue", validate_sudokuvalue),
    "zones": (validate_list, "GroupSpec", validate_groupspec),
    "cages": (validate_list, "CalcSpec", validate_calcspec),
}
