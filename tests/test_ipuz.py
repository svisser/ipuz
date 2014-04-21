import json
import unittest

import ipuz


class IPUZReadTestCase(unittest.TestCase):

    def test_read_detects_invalid_ipuz_data(self):
        with self.assertRaises(ipuz.IPUZException):
            ipuz.read("this is wrong")

    def test_read_raises_for_missing_version_field(self):
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read(json.dumps({}))
        self.assertEqual(str(cm.exception), "Mandatory field version is missing")

    def test_read_raises_for_missing_kind_field(self):
        with self.assertRaises(ipuz.IPUZException) as cm:
            ipuz.read(json.dumps({
                "version": "http://ipuz.org/v1",
            }))
        self.assertEqual(str(cm.exception), "Mandatory field kind is missing")

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


class IPUZCrosswordTestCase(unittest.TestCase):

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
        with self.assertRaises(ipuz.IPUZException) as cm:
            result = ipuz.read(json.dumps(json_data))
        self.assertEqual(str(cm.exception), "Mandatory field dimensions is missing")

    def test_validate_crossword_mandatory_puzzle_field(self):
        json_data = self._create_puzzle()
        del json_data["puzzle"]
        with self.assertRaises(ipuz.IPUZException) as cm:
            result = ipuz.read(json.dumps(json_data))
        self.assertEqual(str(cm.exception), "Mandatory field puzzle is missing")


class IPUZSudokuTestCase(unittest.TestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/sudoku"],
            "puzzle": [],
        }

    def test_validate_sudoku_mandatory_puzzle_field(self):
        json_data = self._create_puzzle()
        del json_data["puzzle"]
        with self.assertRaises(ipuz.IPUZException) as cm:
            result = ipuz.read(json.dumps(json_data))
        self.assertEqual(str(cm.exception), "Mandatory field puzzle is missing")


class IPUZBlockTestCase(unittest.TestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/block"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_block_mandatory_dimensions_field(self):
        json_data = self._create_puzzle()
        del json_data["dimensions"]
        with self.assertRaises(ipuz.IPUZException) as cm:
            result = ipuz.read(json.dumps(json_data))
        self.assertEqual(str(cm.exception), "Mandatory field dimensions is missing")


class IPUZWordSearchTestCase(unittest.TestCase):

    def _create_puzzle(self):
        return {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/wordsearch"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_wordsearch_mandatory_dimensions_field(self):
        json_data = self._create_puzzle()
        del json_data["dimensions"]
        with self.assertRaises(ipuz.IPUZException) as cm:
            result = ipuz.read(json.dumps(json_data))
        self.assertEqual(str(cm.exception), "Mandatory field dimensions is missing")


class IPUZWriteTestCase(unittest.TestCase):

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
