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
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read("this is wrong")
        self.assertEqual(str(cm.exception), "No valid JSON could be found")

    def test_read_detects_empty_input(self):
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read(None)
        self.assertEqual(str(cm.exception), "No valid JSON could be found")
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read("")
        self.assertEqual(str(cm.exception), "No valid JSON could be found")

    def test_read_detects_non_string_input(self):
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read(3)
        self.assertEqual(str(cm.exception), "No valid JSON could be found")

    def test_read_detects_valid_json_but_not_dict_json(self):
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read('["version", "kind"]')
        self.assertEqual(str(cm.exception), "No valid JSON could be found")

    def test_read_raises_for_missing_version_field(self):
        self.validate_puzzle({}, "Mandatory field version is missing")

    def test_read_raises_for_missing_kind_field(self):
        self.validate_puzzle({
            "version": "http://ipuz.org/v1",
        }, "Mandatory field kind is missing")

    def test_read_raises_for_invalid_version_field(self):
        self.validate_puzzle({
            "version": "invalid_version",
            "kind": ["http://ipuz.org/invalid", ]
        }, "Invalid or unsupported version value found")

    def test_read_raises_for_unsupported_version_field(self):
        self.validate_puzzle({
            "version": "http://ipuz.org/v2",
            "kind": ["http://ipuz.org/invalid", ]
        }, "Invalid or unsupported version value found")

    def test_read_allows_jsonp_callback_function(self):
        result = ipuz.read("ipuz(" + json.dumps({
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid", ]
        }) + ")")
        self.assertEqual(result['version'], "http://ipuz.org/v1")

        result = ipuz.read("ipuz_callback_function(" + json.dumps({
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid", ]
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

    def test_invalid_kind_is_not_a_string(self):
        self.validate_puzzle({
            "version": "http://ipuz.org/v1",
            "kind": [3],
        }, "Invalid kind value found")


class IPUZFieldValidatorTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/invalid"],

        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)

    def test_validate_date_invalid_format(self):
        self.puzzle["date"] = "14/01/2014"
        self.validate("Invalid date format: 14/01/2014")

    def test_copyright_is_string(self):
        self.puzzle["copyright"] = 3
        self.validate("Invalid copyright value found")

    def test_publisher_is_string(self):
        self.puzzle["publisher"] = 3
        self.validate("Invalid publisher value found")

    def test_publication_is_string(self):
        self.puzzle["publication"] = 3
        self.validate("Invalid publication value found")

    def test_url_is_string(self):
        self.puzzle["url"] = 3
        self.validate("Invalid url value found")

    def test_uniqueid_is_string(self):
        self.puzzle["uniqueid"] = 3
        self.validate("Invalid uniqueid value found")

    def test_title_is_string(self):
        self.puzzle["title"] = 3
        self.validate("Invalid title value found")

    def test_intro_is_string(self):
        self.puzzle["intro"] = 3
        self.validate("Invalid intro value found")

    def test_explanation_is_string(self):
        self.puzzle["explanation"] = 3
        self.validate("Invalid explanation value found")

    def test_annotation_is_string(self):
        self.puzzle["annotation"] = 3
        self.validate("Invalid annotation value found")

    def test_author_is_string(self):
        self.puzzle["author"] = 3
        self.validate("Invalid author value found")

    def test_editor_is_string(self):
        self.puzzle["editor"] = 3
        self.validate("Invalid editor value found")

    def test_notes_is_string(self):
        self.puzzle["notes"] = 3
        self.validate("Invalid notes value found")

    def test_difficulty_is_string(self):
        self.puzzle["difficulty"] = 3
        self.validate("Invalid difficulty value found")

    def test_origin_is_string(self):
        self.puzzle["origin"] = 3
        self.validate("Invalid origin value found")

    def test_block_is_string(self):
        self.puzzle["block"] = 3
        self.validate("Invalid block value found")

    def test_empty_is_string_or_int(self):
        self.puzzle["empty"] = True
        self.validate("Invalid empty value found")

    def test_checksum_is_list_(self):
        self.puzzle["checksum"] = 3
        self.validate("Invalid checksum value found")

    def test_checksum_is_list_of_strings(self):
        self.puzzle["checksum"] = [3]
        self.validate("Invalid checksum value found")


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

    def test_example_ipuz_file_with_json(self):
        with open("fixtures/example.ipuz") as f:
            data = f.read()

        output = ipuz.read(data)
        output_string = ipuz.write(output, json_only=True)
        second_output = ipuz.read(output_string)
        self.assertEqual(output, second_output)

    def test_example_ipuz_file_with_jsonp(self):
        with open("fixtures/example.ipuz") as f:
            data = f.read()

        output = ipuz.read(data)
        output_string = ipuz.write(output)
        second_output = ipuz.read(output_string)
        self.assertEqual(output, second_output)
