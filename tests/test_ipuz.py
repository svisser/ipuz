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

    def test_read_raises_for_invalid_version_field(self):
        self.validate_puzzle({
            "version": "invalid_version",
            "kind": ["http://ipuz.org/invalid",]
        }, "Invalid or unsupported version value found")

    def test_read_raises_for_unsupported_version_field(self):
        self.validate_puzzle({
            "version": "http://ipuz.org/v2",
            "kind": ["http://ipuz.org/invalid",]
        }, "Invalid or unsupported version value found")

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

    def test_invalid_kind_type(self):
        self.validate_puzzle({
            "version": "http://ipuz.org/v1",
            "kind": 3,
        }, "Invalid kind value found")

    def test_invalid_empty_kind(self):
        self.validate_puzzle({
            "version": "http://ipuz.org/v1",
            "kind": [],
        }, "Invalid kind value found")


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
