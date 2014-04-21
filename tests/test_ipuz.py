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
            "Style highlight in field styles is not a name, dictionary or None"
        )

    def test_validate_invalid_style_specifier(self):
        json_data = self._create_puzzle({"invalid_specifier": None})
        self.validate_puzzle(
            json_data,
            "Style highlight in field styles contains invalid specifier: invalid_specifier"
        )

    def test_validate_invalid_stylespec_shapebg(self):
        json_data = self._create_puzzle({"shapebg": "not-a-circle"})
        self.validate_puzzle(
            json_data,
            "Style with invalid shapebg value found: not-a-circle"
        )

    def test_validate_invalid_stylespec_barred(self):
        json_data = self._create_puzzle({"barred": "TRSBL"})
        self.validate_puzzle(
            json_data,
            "Style with invalid barred value found: TRSBL"
        )

    def test_validate_invalid_stylespec_dotted(self):
        json_data = self._create_puzzle({"dotted": "TRSBL"})
        self.validate_puzzle(
            json_data,
            "Style with invalid dotted value found: TRSBL"
        )

    def test_validate_invalid_stylespec_dashed(self):
        json_data = self._create_puzzle({"dashed": "TRSBL"})
        self.validate_puzzle(
            json_data,
            "Style with invalid dashed value found: TRSBL"
        )

    def test_validate_invalid_stylespec_lessthan(self):
        json_data = self._create_puzzle({"lessthan": None})
        self.validate_puzzle(
            json_data,
            "Style with invalid lessthan value found: None"
        )

    def test_validate_invalid_stylespec_greaterthan(self):
        json_data = self._create_puzzle({"greaterthan": "3"})
        self.validate_puzzle(
            json_data,
            "Style with invalid greaterthan value found: 3"
        )

    def test_validate_invalid_stylespec_equal(self):
        json_data = self._create_puzzle({"equal": "a"})
        self.validate_puzzle(
            json_data,
            "Style with invalid equal value found: a"
        )

    def test_validate_invalid_stylespec_color(self):
        json_data = self._create_puzzle({"color": None})
        self.validate_puzzle(
            json_data,
            "Style with invalid color value found: None"
        )

    def test_validate_invalid_stylespec_colortext(self):
        json_data = self._create_puzzle({"colortext": "AABBCCDDEEFF"})
        self.validate_puzzle(
            json_data,
            "Style with invalid colortext value found: AABBCCDDEEFF"
        )

    def test_validate_invalid_stylespec_colorborder(self):
        json_data = self._create_puzzle({"colorborder": "ABC"})
        self.validate_puzzle(
            json_data,
            "Style with invalid colorborder value found: ABC"
        )

    def test_validate_invalid_stylespec_colorbar(self):
        json_data = self._create_puzzle({"colorbar": "AABBCZ"})
        self.validate_puzzle(
            json_data,
            "Style with invalid colorbar value found: AABBCZ"
        )

    def test_validate_invalid_stylespec_divided(self):
        json_data = self._create_puzzle({"divided": "AA"})
        self.validate_puzzle(
            json_data,
            "Style with invalid divided value found: AA"
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
