import json
import unittest

import ipuz


class IPUZBaseTestCase(unittest.TestCase):

    def validate_puzzle(self, json_data, expected_exception):
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read(json.dumps(json_data))
        self.assertEqual(str(cm.exception), expected_exception)


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


class IPUZCrosswordTestCase(IPUZBaseTestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/crossword#1"],
            "dimensions": {"width": 3, "height": 3},
            "puzzle": [],
        }

    def test_validate_crossword_mandatory_dimensions_field(self):
        json_data = self._create_puzzle()
        del json_data["dimensions"]
        self.validate_puzzle(json_data, "Mandatory field dimensions is missing")

    def test_validate_crossword_mandatory_puzzle_field(self):
        json_data = self._create_puzzle()
        del json_data["puzzle"]
        self.validate_puzzle(json_data, "Mandatory field puzzle is missing")


class IPUZSudokuTestCase(IPUZBaseTestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/sudoku"],
            "puzzle": [],
        }

    def test_validate_sudoku_mandatory_puzzle_field(self):
        json_data = self._create_puzzle()
        del json_data["puzzle"]
        self.validate_puzzle(json_data, "Mandatory field puzzle is missing")


class IPUZBlockTestCase(IPUZBaseTestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/block"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_block_mandatory_dimensions_field(self):
        json_data = self._create_puzzle()
        del json_data["dimensions"]
        self.validate_puzzle(json_data, "Mandatory field dimensions is missing")


class IPUZWordSearchTestCase(IPUZBaseTestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/wordsearch"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_wordsearch_mandatory_dimensions_field(self):
        json_data = self._create_puzzle()
        del json_data["dimensions"]
        self.validate_puzzle(json_data, "Mandatory field dimensions is missing")


class IPUZFieldDimensionsValidatorTestCase(IPUZBaseTestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_incomplete_dimensions(self):
        json_data = self._create_puzzle()
        del json_data["dimensions"]["width"]
        self.validate_puzzle(json_data, "Mandatory field width of dimensions is missing")

    def test_validate_dimensions_negative_or_zero(self):
        json_data = self._create_puzzle()
        json_data["dimensions"]["width"] = 0
        self.validate_puzzle(json_data, "Field width of dimensions is less than one")


class IPUZFieldDateValidatorTestCase(IPUZBaseTestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid"],
            "date": "14/01/2014",
        }

    def test_validate_date_invalid_format(self):
        json_data = self._create_puzzle()
        self.validate_puzzle(json_data, "Invalid date format: 14/01/2014")


class IPUZFieldStylesValidatorTestCase(IPUZBaseTestCase):

    def _create_puzzle(self, style=None):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid"],
            "styles": {
                "highlight": style,
            }
        }

    def test_validate_style_spec_not_string_or_dict(self):
        json_data = self._create_puzzle(3)
        self.validate_puzzle(
            json_data,
            "StyleSpec is not a name, dictionary or None"
        )

    def test_validate_invalid_style_specifier(self):
        json_data = self._create_puzzle({"invalid_specifier": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec contains invalid specifier: invalid_specifier"
        )

    def test_validate_invalid_stylespec_shapebg(self):
        json_data = self._create_puzzle({"shapebg": "not-a-circle"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid shapebg value"
        )

    def test_validate_invalid_stylespec_highlight(self):
        json_data = self._create_puzzle({"highlight": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid highlight value"
        )
        json_data = self._create_puzzle({"highlight": "A"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid highlight value"
        )

    def test_validate_invalid_stylespec_named(self):
        json_data = self._create_puzzle({"named": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid named value"
        )
        json_data = self._create_puzzle({"named": True})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid named value"
        )

    def test_validate_invalid_stylespec_border(self):
        json_data = self._create_puzzle({"border": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid border value"
        )
        json_data = self._create_puzzle({"border": "A"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid border value"
        )
        json_data = self._create_puzzle({"border": -20})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid border value"
        )

    def test_validate_invalid_stylespec_barred(self):
        json_data = self._create_puzzle({"barred": "TRSBL"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid barred value"
        )

    def test_validate_invalid_stylespec_dotted(self):
        json_data = self._create_puzzle({"dotted": "TRSBL"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid dotted value"
        )

    def test_validate_invalid_stylespec_dashed(self):
        json_data = self._create_puzzle({"dashed": "TRSBL"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid dashed value"
        )

    def test_validate_invalid_stylespec_lessthan(self):
        json_data = self._create_puzzle({"lessthan": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid lessthan value"
        )

    def test_validate_invalid_stylespec_greaterthan(self):
        json_data = self._create_puzzle({"greaterthan": "3"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid greaterthan value"
        )

    def test_validate_invalid_stylespec_equal(self):
        json_data = self._create_puzzle({"equal": "a"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid equal value"
        )

    def test_validate_invalid_stylespec_color(self):
        json_data = self._create_puzzle({"color": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid color value"
        )

    def test_validate_invalid_stylespec_colortext(self):
        json_data = self._create_puzzle({"colortext": "AABBCCDDEEFF"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid colortext value"
        )

    def test_validate_invalid_stylespec_colorborder(self):
        json_data = self._create_puzzle({"colorborder": "ABC"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid colorborder value"
        )

    def test_validate_invalid_stylespec_colorbar(self):
        json_data = self._create_puzzle({"colorbar": "AABBCZ"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid colorbar value"
        )

    def test_validate_invalid_stylespec_divided(self):
        json_data = self._create_puzzle({"divided": "AA"})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid divided value"
        )

    def test_validate_invalid_stylespec_mark(self):
        json_data = self._create_puzzle({"mark": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid mark value"
        )
        json_data = self._create_puzzle({"mark": {"key": "text"}})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid mark value"
        )

    def test_validate_invalid_stylespec_slice(self):
        json_data = self._create_puzzle({"slice": None})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid slice value"
        )
        json_data = self._create_puzzle({"slice": [100, 200, None, 300]})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid slice value"
        )
        json_data = self._create_puzzle({"slice": [100, 200, 300]})
        self.validate_puzzle(
            json_data,
            "StyleSpec has an invalid slice value"
        )


class IPUZGroupSpecValidatorTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/crossword"],
            "dimensions": {"width": 3, "height": 3},
            "puzzle": [],
            "zones": [],
        }

    def test_validate_groupspec_is_not_a_list(self):
        self.puzzle["zones"] = 3
        self.validate_puzzle(
            self.puzzle,
            "Invalid zones value found"
        )

    def test_validate_groupspec_invalid_element(self):
        self.puzzle["zones"] = [3]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupspec_invalid_empty_groupspec(self):
        self.puzzle["zones"] = [{}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupspec_invalid_groupspec_key(self):
        self.puzzle["zones"] = [{"invalid_key": 3}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupspec_empty_groupspec_cells(self):
        self.puzzle["zones"] = [{"cells": []}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupspec_empty_groupspec_cell_in_cells(self):
        self.puzzle["zones"] = [{"cells": [ [3] ]}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupspec_empty_groupspec_another_cell_in_cells(self):
        self.puzzle["zones"] = [{"cells": [[3, 4], [5]]}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupspec_with_invalid_stylespec(self):
        self.puzzle["zones"] = [{"style": { "shapebg": "not-a-circle"}}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupsec_with_invalid_rect(self):
        self.puzzle["zones"] = [{"rect": 3}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupsec_with_invalid_rect(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 5]}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupsec_with_invalid_rect_element_not_integer(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 5, None]}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupsec_with_illogical_rect(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 5, 2]}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )

    def test_validate_groupsec_with_illogical_rect_two(self):
        self.puzzle["zones"] = [{"rect": [3, 4, 1, 6]}]
        self.validate_puzzle(
            self.puzzle,
            "Invalid GroupSpec in zones element found"
        )


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
