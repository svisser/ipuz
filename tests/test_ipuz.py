import json
import unittest

import ipuz


class IPUZBaseTestCase(unittest.TestCase):

    def validate_puzzle(self, json_data, expected_exception):
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read(json.dumps(json_data))
        self.assertEqual(str(cm.exception), expected_exception)


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
                "highlight": True,
            }
        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)


class IPUZSampleSudokuTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/sudoku"],
            "puzzle": [],
        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)


class IPUZSampleWordSearchTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/wordsearch"],
            "dimensions": {"width": 3, "height": 3},
        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)


class IPUZReadTestCase(IPUZBaseTestCase):

    def test_read_detects_invalid_ipuz_data(self):
        with self.assertRaises(ipuz.IPUZException):
            ipuz.read("this is wrong")

    def test_read_raises_for_missing_version_field(self):
        self.validate_puzzle({}, "Mandatory field version is missing")

    def test_read_raises_for_missing_kind_field(self):
        self.validate_puzzle({
            "version": "http://ipuz.org/v1",
        }, "Mandatory field kind is missing")

    def test_read_allows_jsonp_callback_function(self):
        result = ipuz.read("ipuz(" + json.dumps({
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid",]
        }) + ")")
        self.assertEqual(result['version'], "http://ipuz.org/v1")

        result = ipuz.read("ipuz_callback_function(" + json.dumps({
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid",]
        }) + ")")
        self.assertEqual(result['version'], "http://ipuz.org/v1")


class IPUZCrosswordKindTestCase(IPUZSampleCrosswordTestCase):

    def test_validate_crossword_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate("Mandatory field dimensions is missing")

    def test_validate_crossword_mandatory_puzzle_field(self):
        del self.puzzle["puzzle"]
        self.validate("Mandatory field puzzle is missing")


class IPUZSudokuKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/sudoku"],
            "puzzle": [],
        }

    def test_validate_sudoku_mandatory_puzzle_field(self):
        del self.puzzle["puzzle"]
        self.validate_puzzle(self.puzzle, "Mandatory field puzzle is missing")


class IPUZBlockKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/block"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_block_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate_puzzle(self.puzzle, "Mandatory field dimensions is missing")


class IPUZWordSearchKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/wordsearch"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_wordsearch_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate_puzzle(self.puzzle, "Mandatory field dimensions is missing")


class IPUZFieldDimensionsValidatorTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_incomplete_dimensions(self):
        del self.puzzle["dimensions"]["width"]
        self.validate_puzzle(self.puzzle, "Mandatory field width of dimensions is missing")

    def test_validate_dimensions_negative_or_zero(self):
        self.puzzle["dimensions"]["width"] = 0
        self.validate_puzzle(self.puzzle, "Field width of dimensions is less than one")


class IPUZFieldDateValidatorTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid"],
            "date": "14/01/2014",
        }

    def test_validate_date_invalid_format(self):
        self.validate_puzzle(self.puzzle, "Invalid date format: 14/01/2014")


class IPUZFieldStylesValidatorTestCase(IPUZSampleCrosswordTestCase):

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


class IPUZGroupSpecValidatorTestCase(IPUZSampleCrosswordTestCase):

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
        self.puzzle["zones"] = [{"cells": [ [3] ]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_empty_groupspec_another_cell_in_cells(self):
        self.puzzle["zones"] = [{"cells": [[3, 4], [5]]}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupspec_with_invalid_stylespec(self):
        self.puzzle["zones"] = [{"style": { "shapebg": "not-a-circle"}}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupsec_with_invalid_rect(self):
        self.puzzle["zones"] = [{"rect": 3}]
        self.validate("Invalid GroupSpec in zones element found")

    def test_validate_groupsec_with_invalid_rect(self):
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


class IPUZShowEnumerationsTestCase(IPUZSampleCrosswordTestCase):

    def test_showenumerations(self):
        self.puzzle["showenumerations"] = 3
        self.validate("Invalid showenumerations value found")


class IPUZCluePlacementTestCase(IPUZSampleCrosswordTestCase):

    def test_clueplacement(self):
        self.puzzle["clueplacement"] = 3
        self.validate("Invalid clueplacement value found")


class IPUZAnswerTestCase(IPUZSampleCrosswordTestCase):

    def test_answer(self):
        self.puzzle["answer"] = 3
        self.validate("Invalid answer value found")

    def test_answers_not_a_list(self):
        self.puzzle["answers"] = 3
        self.validate("Invalid answers value found")

    def test_answers_empty_list(self):
        self.puzzle["answers"] = []
        self.validate("Invalid answers value found")

    def test_answers_list_with_invalid_content(self):
        self.puzzle["answers"] = [3]
        self.validate("Invalid answers value found")


class IPUZCrosswordValueTestCase(IPUZSampleCrosswordTestCase):

    def test_saved_value_is_not_a_list(self):
        self.puzzle["saved"] = 3
        self.validate("Invalid saved value found")

    def test_solution_value_is_not_a_list(self):
        self.puzzle["solution"] = 3
        self.validate("Invalid solution value found")

    def test_saved_value_is_list(self):
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

    def test_validate_crosswordvalue_with_direction_and_invalid_crosswordvalue(self):
        self.puzzle["saved"] = [[{"Across": 3}]]
        self.validate("Invalid CrosswordValue in saved element found")

    def test_validate_crosswordvalue_with_invalid_direction(self):
        self.puzzle["saved"] = [[{"Across:Horizontal:and_something": "A"}]]
        self.validate("Invalid CrosswordValue in saved element found")


class IPUZSudokuValueTestCase(IPUZSampleSudokuTestCase):

    def test_charset_must_be_text(self):
        self.puzzle["charset"] = 3
        self.validate("Invalid charset value found")

    def test_charset_must_have_length_nine(self):
        self.puzzle["charset"] = "12345"
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


class IPUZWordSearchValueTestCase(IPUZSampleWordSearchTestCase):

    def test_useall_is_bool(self):
        self.puzzle["useall"] = 3
        self.validate("Invalid useall value found")

    def test_retrace_is_bool(self):
        self.puzzle["retrace"] = 3
        self.validate("Invalid retrace value found")

    def test_zigzag_is_bool(self):
        self.puzzle["zigzag"] = 3
        self.validate("Invalid zigzag value found")

    def test_misses_is_dict(self):
        self.puzzle["misses"] = []
        self.validate("Invalid misses value found")

    def test_misses_is_dict_with_non_text_key(self):
        self.puzzle["misses"] = {3: "A"}
        self.validate("Invalid misses value found")

    def test_misses_is_dict_with_non_text_key(self):
        self.puzzle["misses"] = {"A": 3}
        self.validate("Invalid misses value found")

    def test_points_is_text(self):
        self.puzzle["points"] = 3
        self.validate("Invalid points value found")

    def test_time_is_integer(self):
        self.puzzle["time"] = "time"
        self.validate("Invalid time value found")

    def test_time_is_non_negative_integer(self):
        self.puzzle["time"] = -1
        self.validate("Invalid time value found")

    def test_showanswers_is_text(self):
        self.puzzle["showanswers"] = 3
        self.validate("Invalid showanswers value found")

    def test_dictionary_is_text_or_false(self):
        self.puzzle["dictionary"] = 3
        self.validate("Invalid dictionary value found")

    def test_dictionary_is_non_empty_string(self):
        self.puzzle["dictionary"] = ""
        self.validate("Invalid dictionary value found")

    def test_dictionary_is_not_true(self):
        self.puzzle["dictionary"] = True
        self.validate("Invalid dictionary value found")


class IPUZWriteTestCase(IPUZBaseTestCase):

    def test_write_produces_jsonp_string_by_default(self):
        json_data = {}
        result = ipuz.write(json_data)
        expected = ''.join(['ipuz(', json.dumps(json_data), ')'])
        self.assertEqual(result, expected)

    def test_write_supports_different_callback_name(self):
        json_data = {}
        result = ipuz.write(json_data, callback_name="ipuz_function")
        expected = ''.join(['ipuz_function(', json.dumps(json_data), ')'])
        self.assertEqual(result, expected)

    def test_write_produces_json_with_json_only_flag(self):
        json_data = {}
        result = ipuz.write(json_data, json_only=True)
        expected = json.dumps(json_data)
        self.assertEqual(result, expected)

    def test_ignores_callback_name_when_json_only(self):
        json_data = {}
        result = ipuz.write(
            json_data,
            callback_name="ipuz_function",
            json_only=True
        )
        expected = json.dumps(json_data)
        self.assertEqual(result, expected)


class IPUZRoundTripTestCase(IPUZBaseTestCase):

    def test_first_ipuz_file_with_json(self):
        with open("fixtures/first.ipuz") as f:
            data = f.read()

        output = ipuz.read(data)
        output_string = ipuz.write(output, json_only=True)
        second_output = ipuz.read(output_string)
        self.assertEqual(output, second_output)

    def test_first_ipuz_file_with_jsonp(self):
        with open("fixtures/first.ipuz") as f:
            data = f.read()

        output = ipuz.read(data)
        output_string = ipuz.write(output)
        second_output = ipuz.read(output_string)
        self.assertEqual(output, second_output)
