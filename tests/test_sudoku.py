from .test_ipuz import IPUZBaseTestCase


class IPUZSampleSudokuTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/sudoku"],
            "puzzle": [],
        }

    def test_charset_must_be_text(self):
        self.puzzle["charset"] = 3
        self.validate("Invalid charset value found")

    def test_displaycharset_is_bool(self):
        self.puzzle["displaycharset"] = 3
        self.validate("Invalid displaycharset value found")

    def test_boxes_is_bool(self):
        self.puzzle["boxes"] = 3
        self.validate("Invalid boxes value found")

    def test_showoperators_is_bool(self):
        self.puzzle["showoperators"] = 3
        self.validate("Invalid showoperators value found")

    def test_cageborder_is_valid_text(self):
        self.puzzle["cageborder"] = "not-a-border"
        self.validate("Invalid cageborder value found")

    def test_cages_is_list(self):
        self.puzzle["cages"] = 3
        self.validate("Invalid cages value found")

    def test_cages_has_invalid_calcspec(self):
        self.puzzle["cages"] = [3]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_key(self):
        self.puzzle["cages"] = [{"invalid_key": 3}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_empty_calcspec(self):
        self.puzzle["cages"] = [{}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_value(self):
        self.puzzle["cages"] = [{"value": "NaN"}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_operator(self):
        self.puzzle["cages"] = [{"operator": "|"}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_style(self):
        self.puzzle["cages"] = [{"style": {"shapebg": "not-a-circle"}}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_rect(self):
        self.puzzle["cages"] = [{"rect": 3}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_cells(self):
        self.puzzle["cages"] = [{"cells": 3}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_puzzle_is_list(self):
        self.puzzle["puzzle"] = 3
        self.validate("Invalid puzzle value found")

    def test_puzzle_contains_list_elements(self):
        self.puzzle["puzzle"] = [3]
        self.validate("Invalid puzzle value found")

    def test_puzzle_contains_invalid_sudokugiven_element(self):
        self.puzzle["puzzle"] = [[[]]]
        self.validate("Invalid SudokuGiven in puzzle element found")

    def test_puzzle_contains_invalid_sudokugiven_element_dict(self):
        self.puzzle["puzzle"] = [[{}]]
        self.validate("Invalid SudokuGiven in puzzle element found")

    def test_puzzle_contains_invalid_sudokugiven_element_key_dict(self):
        self.puzzle["puzzle"] = [[{"invalid_key": "3"}]]
        self.validate("Invalid SudokuGiven in puzzle element found")

    def test_puzzle_contains_invalid_sudokugiven_element_given_dict(self):
        self.puzzle["puzzle"] = [[{"given": []}]]
        self.validate("Invalid SudokuGiven in puzzle element found")

    def test_puzzle_contains_invalid_sudokugiven_element_style_dict(self):
        self.puzzle["puzzle"] = [[{"style": {"shapebg": "not-a-circle"}}]]
        self.validate("Invalid SudokuGiven in puzzle element found")

    def test_solution_contains_list_elements(self):
        self.puzzle["solution"] = [3]
        self.validate("Invalid solution value found")

    def test_solution_contains_invalid_sudokuvalue_element(self):
        self.puzzle["solution"] = [[[]]]
        self.validate("Invalid SudokuValue in solution element found")

    def test_solution_contains_invalid_sudokuvalue_element_dict(self):
        self.puzzle["solution"] = [[{}]]
        self.validate("Invalid SudokuValue in solution element found")

    def test_solution_contains_invalid_sudokuvalue_element_key_dict(self):
        self.puzzle["solution"] = [[{"invalid_key": "3"}]]
        self.validate("Invalid SudokuValue in solution element found")

    def test_solution_contains_invalid_sudokuvalue_element_given_dict(self):
        self.puzzle["solution"] = [[{"given": []}]]
        self.validate("Invalid SudokuValue in solution element found")

    def test_solution_contains_invalid_sudokuvalue_element_style_dict(self):
        self.puzzle["solution"] = [[{"style": {"shapebg": "not-a-circle"}}]]
        self.validate("Invalid SudokuValue in solution element found")

    def test_saved_is_list(self):
        self.puzzle["saved"] = 3
        self.validate("Invalid saved value found")

    def test_saved_contains_lists(self):
        self.puzzle["saved"] = [3]
        self.validate("Invalid saved value found")

    def test_saved_contains_invalid_sudokuguess(self):
        self.puzzle["saved"] = [[True]]
        self.validate("Invalid SudokuGuess in saved element found")

    def test_zones_is_not_int(self):
        self.puzzle["zones"] = 3
        self.validate("Invalid zones value found")

    def test_validate_groupsec_with_invalid_rect(self):
        self.puzzle["zones"] = [{"rect": 3}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_sudoku_mandatory_puzzle_field(self):
        del self.puzzle["puzzle"]
        self.validate_puzzle(self.puzzle, "Mandatory field puzzle is missing")
