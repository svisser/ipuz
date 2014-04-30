from .test_ipuz import IPUZBaseTestCase


class IPUZSampleCrosswordTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/crossword"],
            "dimensions": {"width": 3, "height": 3},
            "puzzle": [],
            "saved": [],
            "solution": [],
            "zones": [],
            "styles": {
                "highlight": None,
            }
        }

    def test_validate_incomplete_dimensions(self):
        del self.puzzle["dimensions"]["width"]
        self.validate_puzzle(
            self.puzzle,
            "Mandatory field width of dimensions is missing"
        )

    def test_validate_dimensions_negative_or_zero(self):
        self.puzzle["dimensions"]["width"] = 0
        self.validate_puzzle(
            self.puzzle,
            "Field width of dimensions is less than one"
        )

    def test_validate_crossword_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate("Mandatory field dimensions is missing")

    def test_validate_crossword_mandatory_puzzle_field(self):
        del self.puzzle["puzzle"]
        self.validate("Mandatory field puzzle is missing")

    def test_validate_styles_is_not_a_dict(self):
        self.puzzle["styles"] = 3
        self.validate("Invalid styles value found")

    def test_validate_style_spec_not_string_or_dict(self):
        self.puzzle["styles"]["highlight"] = 3
        self.validate("StyleSpec is not a name, dictionary or None")

    def test_validate_invalid_style_specifier(self):
        self.puzzle["styles"]["highlight"] = {"invalid_specifier": None}
        self.validate_puzzle(
            self.puzzle,
            "StyleSpec contains invalid specifier: invalid_specifier"
        )

    def test_validate_invalid_stylespec_shapebg(self):
        self.puzzle["styles"]["highlight"] = {"shapebg": "not-a-circle"}
        self.validate("StyleSpec has an invalid shapebg value")

    def test_validate_invalid_stylespec_highlight(self):
        self.puzzle["styles"]["highlight"] = {"highlight": None}
        self.validate("StyleSpec has an invalid highlight value")

        self.puzzle["styles"]["highlight"] = {"highlight": "A"}
        self.validate("StyleSpec has an invalid highlight value")

    def test_validate_invalid_stylespec_named(self):
        self.puzzle["styles"]["highlight"] = {"named": None}
        self.validate("StyleSpec has an invalid named value")
        self.puzzle["styles"]["highlight"] = {"named": True}
        self.validate("StyleSpec has an invalid named value")

    def test_validate_invalid_stylespec_border(self):
        self.puzzle["styles"]["highlight"] = {"border": None}
        self.validate("StyleSpec has an invalid border value")
        self.puzzle["styles"]["highlight"] = {"border": "A"}
        self.validate("StyleSpec has an invalid border value")
        self.puzzle["styles"]["highlight"] = {"border": -20}
        self.validate("StyleSpec has an invalid border value")

    def test_validate_invalid_stylespec_barred(self):
        self.puzzle["styles"]["highlight"] = {"barred": "TRSBL"}
        self.validate("StyleSpec has an invalid barred value")

    def test_validate_invalid_stylespec_dotted(self):
        self.puzzle["styles"]["highlight"] = {"dotted": "TRSBL"}
        self.validate("StyleSpec has an invalid dotted value")

    def test_validate_invalid_stylespec_dashed(self):
        self.puzzle["styles"]["highlight"] = {"dashed": "TRSBL"}
        self.validate("StyleSpec has an invalid dashed value")

    def test_validate_invalid_stylespec_lessthan(self):
        self.puzzle["styles"]["highlight"] = {"lessthan": None}
        self.validate("StyleSpec has an invalid lessthan value")

    def test_validate_invalid_stylespec_greaterthan(self):
        self.puzzle["styles"]["highlight"] = {"greaterthan": "3"}
        self.validate("StyleSpec has an invalid greaterthan value")

    def test_validate_invalid_stylespec_equal(self):
        self.puzzle["styles"]["highlight"] = {"equal": "a"}
        self.validate("StyleSpec has an invalid equal value")

    def test_validate_invalid_stylespec_color(self):
        self.puzzle["styles"]["highlight"] = {"color": None}
        self.validate("StyleSpec has an invalid color value")

    def test_validate_invalid_stylespec_colortext(self):
        self.puzzle["styles"]["highlight"] = {"colortext": "AABBCCDDEEFF"}
        self.validate("StyleSpec has an invalid colortext value")

    def test_validate_invalid_stylespec_colorborder(self):
        self.puzzle["styles"]["highlight"] = {"colorborder": "ABC"}
        self.validate("StyleSpec has an invalid colorborder value")

    def test_validate_invalid_stylespec_colorbar(self):
        self.puzzle["styles"]["highlight"] = {"colorbar": "AABBCZ"}
        self.validate("StyleSpec has an invalid colorbar value")

    def test_validate_invalid_stylespec_divided(self):
        self.puzzle["styles"]["highlight"] = {"divided": "AA"}
        self.validate("StyleSpec has an invalid divided value")

    def test_validate_invalid_stylespec_mark(self):
        self.puzzle["styles"]["highlight"] = {"mark": None}
        self.validate("StyleSpec has an invalid mark value")
        self.puzzle["styles"]["highlight"] = {"mark": {"key": "text"}}
        self.validate("StyleSpec has an invalid mark value")

    def test_validate_invalid_stylespec_slice(self):
        self.puzzle["styles"]["highlight"] = {"slice": None}
        self.validate("StyleSpec has an invalid slice value")
        self.puzzle["styles"]["highlight"] = {"slice": [100, 200, None, 300]}
        self.validate("StyleSpec has an invalid slice value")
        self.puzzle["styles"]["highlight"] = {"slice": [100, 200, 300]}
        self.validate("StyleSpec has an invalid slice value")

    def test_validate_groupspec_is_not_a_list(self):
        self.puzzle["zones"] = 3
        self.validate("Invalid zones value found")

    def test_validate_groupspec_invalid_element(self):
        self.puzzle["zones"] = [3]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_invalid_empty_groupspec(self):
        self.puzzle["zones"] = [{}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_invalid_groupspec_key(self):
        self.puzzle["zones"] = [{"invalid_key": 3}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_empty_groupspec_cells(self):
        self.puzzle["zones"] = [{"cells": []}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_empty_groupspec_cell_in_cells(self):
        self.puzzle["zones"] = [{"cells": [[3]]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_empty_groupspec_another_cell_in_cells(self):
        self.puzzle["zones"] = [{"cells": [[3, 4], [5]]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_with_invalid_stylespec(self):
        self.puzzle["zones"] = [{"style": {"shapebg": "not-a-circle"}}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupsec_with_invalid_rect(self):
        self.puzzle["zones"] = [{"rect": 3}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupsec_with_invalid_rect_length(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 5]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupsec_with_invalid_rect_element_not_integer(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 5, None]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupsec_with_illogical_rect(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 5, 2]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupsec_with_illogical_rect_two(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 1, 6]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_showenumerations(self):
        self.puzzle["showenumerations"] = 3
        self.validate("Invalid showenumerations value found")

    def test_clueplacement(self):
        self.puzzle["clueplacement"] = 3
        self.validate("Invalid clueplacement value found")

    def test_answer(self):
        self.puzzle["answer"] = 3
        self.validate("Invalid answer value found")

    def test_answers_not_a_list(self):
        self.puzzle["answers"] = 3
        self.validate("Invalid answers value found")

    def test_answers_list_with_invalid_content(self):
        self.puzzle["answers"] = [3]
        self.validate("Invalid answers value found")

    def test_misses_is_dict(self):
        self.puzzle["misses"] = []
        self.validate("Invalid misses value found")

    def test_misses_is_dict_with_non_text_value(self):
        self.puzzle["misses"] = {"A": 3}
        self.validate("Invalid misses value found")

    def test_saved_value_is_not_a_list(self):
        self.puzzle["saved"] = 3
        self.validate("Invalid saved value found")

    def test_solution_value_is_not_a_list(self):
        self.puzzle["solution"] = 3
        self.validate("Invalid solution value found")

    def test_saved_value_contains_only_lists(self):
        self.puzzle["saved"] = [[], [], 3]
        self.validate("Invalid saved value found")

    def test_validate_crosswordvalue_with_number(self):
        self.puzzle["saved"] = [[3]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_invalid_nested_crosswordvalue(self):
        self.puzzle["saved"] = [[[3]]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_double_nested_crosswordvalue(self):
        self.puzzle["saved"] = [[[[3]]]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_empty_dict(self):
        self.puzzle["saved"] = [[{}]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_dict_and_invalid_value(self):
        self.puzzle["saved"] = [[{"value": 3}]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_dict_and_invalid_style(self):
        self.puzzle["saved"] = [[{"style": {"shapebg": "not-a-circle"}}]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_dict_and_invalid_key(self):
        self.puzzle["saved"] = [[{"invalid_key": "A"}]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_direction_invalid_crosswordvalue(self):
        self.puzzle["saved"] = [[{"Across": 3}]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_invalid_direction(self):
        self.puzzle["saved"] = [[{"Across:Horizontal:and_something": "A"}]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_enumeration_is_string(self):
        self.puzzle["enumeration"] = 3
        self.validate("Invalid enumeration value found")

    def test_enumerations_is_list(self):
        self.puzzle["enumerations"] = 3
        self.validate("Invalid enumerations value found")

    def test_enumerations_is_list_with_strings(self):
        self.puzzle["enumerations"] = [3]
        self.validate("Invalid Enumeration in enumerations element found")

    def test_puzzle_is_not_a_list(self):
        self.puzzle["puzzle"] = 3
        self.validate("Invalid puzzle value found")

    def test_puzzle_element_is_not_a_list(self):
        self.puzzle["puzzle"] = [3]
        self.validate("Invalid puzzle value found")

    def test_puzzle_contains_only_lists(self):
        self.puzzle["puzzle"] = [[], [], 3]
        self.validate("Invalid puzzle value found")

    def test_puzzle_with_invalid_nested_labeledcell(self):
        self.puzzle["puzzle"] = [[[3]]]
        self.validate("Invalid LabeledCell in puzzle element found")

    def test_puzzle_with_empty_labeledcell(self):
        self.puzzle["puzzle"] = [[{}]]
        self.validate("Invalid LabeledCell in puzzle element found")

    def test_puzzle_with_labeledcell_with_invalid_key(self):
        self.puzzle["puzzle"] = [[{"invalid_key": 3}]]
        self.validate("Invalid LabeledCell in puzzle element found")

    def test_puzzle_with_labeledcell_with_invalid_cell(self):
        self.puzzle["puzzle"] = [[{"cell": {}}]]
        self.validate("Invalid LabeledCell in puzzle element found")

    def test_puzzle_with_labeledcell_with_invalid_value(self):
        self.puzzle["puzzle"] = [[{"value": 3}]]
        self.validate("Invalid LabeledCell in puzzle element found")

    def test_puzzle_with_labeledcell_with_invalid_style(self):
        self.puzzle["puzzle"] = [[{"style": {"shapebg": "not-a-circle"}}]]
        self.validate("Invalid LabeledCell in puzzle element found")

    def test_clues_not_a_dict(self):
        self.puzzle["clues"] = 3
        self.validate("Invalid clues value found")

    def test_clues_key_not_a_direction(self):
        self.puzzle["clues"] = {"Across:Horizontal:Fail": ["clue"]}
        self.validate("Invalid clues value found")

    def test_clues_value_not_a_list(self):
        self.puzzle["clues"] = {"Across": 3}
        self.validate("Invalid clues value found")

    def test_clues_value_not_an_empty_list(self):
        self.puzzle["clues"] = {"Across": []}
        self.validate("Invalid clues value found")

    def test_clues_element_not_a_valid_clue(self):
        self.puzzle["clues"] = {"Across": [3]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_list_clue(self):
        self.puzzle["clues"] = {"Across": [[1, "The clue", "something else"]]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_list_clue_text(self):
        self.puzzle["clues"] = {"Across": [["1", 3]]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_cluenum(self):
        self.puzzle["clues"] = {"Across": [[None, "The clue"]]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_key(self):
        self.puzzle["clues"] = {"Across": [{"invalid_key": None}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_number(self):
        self.puzzle["clues"] = {"Across": [{"number": None}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_not_a_list(self):
        self.puzzle["clues"] = {"Across": [{"numbers": 3}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_numbers(self):
        self.puzzle["clues"] = {"Across": [{"numbers": [None]}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_clue(self):
        self.puzzle["clues"] = {"Across": [{"clue": None}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_hints(self):
        self.puzzle["clues"] = {"Across": [{"hints": None}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_hints_element(self):
        self.puzzle["clues"] = {"Across": [{"hints": [3]}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_image(self):
        self.puzzle["clues"] = {"Across": [{"image": 3}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_answer(self):
        self.puzzle["clues"] = {"Across": [{"answer": 3}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_enumeration(self):
        self.puzzle["clues"] = {"Across": [{"enumeration": 3}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_references_list(self):
        self.puzzle["clues"] = {"Across": [{"references": 3}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_references(self):
        self.puzzle["clues"] = {"Across": [{"references": [True]}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_see(self):
        self.puzzle["clues"] = {"Across": [{"see": None}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_highlight(self):
        self.puzzle["clues"] = {"Across": [{"highlight": 3}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_location(self):
        self.puzzle["clues"] = {"Across": [{"location": 3}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_location_length(self):
        self.puzzle["clues"] = {"Across": [{"location": [3, 6, 7]}]}
        self.validate("Invalid Clue in clues element found")

    def test_clues_element_not_a_valid_clue_dict_invalid_location_values(self):
        self.puzzle["clues"] = {"Across": [{"location": [3, None]}]}
        self.validate("Invalid Clue in clues element found")
