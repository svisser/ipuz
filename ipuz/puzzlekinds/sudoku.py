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


def validate_cageborder(field_name, field_data):
    validate_elements(field_name, field_data, ["thick", "dashed"])


def validate_cages(field_name, field_data):
    validate_list(field_name, field_data, "CalcSpec", validate_calcspec)


def validate_puzzle(field_name, field_data):
    validate_list_of_lists(field_name, field_data, "SudokuGiven", validate_sudokugiven)


def validate_saved(field_name, field_data):
    validate_list_of_lists(field_name, field_data, "SudokuGuess", validate_sudokuguess)


def validate_solution(field_name, field_data):
    validate_list_of_lists(field_name, field_data, "SudokuValue", validate_sudokuvalue)


def validate_zones(field_name, field_data):
    validate_list(field_name, field_data, "GroupSpec", validate_groupspec)


IPUZ_SUDOKU_VALIDATORS = {
    "charset": validate_string,
    "displaycharset": validate_bool,
    "boxes": validate_bool,
    "showoperators": validate_bool,
    "cageborder": validate_cageborder,
    "puzzle": validate_puzzle,
    "saved": validate_saved,
    "solution": validate_solution,
    "zones": validate_zones,
    "cages": validate_cages,
}
