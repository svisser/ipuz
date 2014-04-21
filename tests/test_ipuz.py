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
            "kind": "http://ipuz.org/crossword#1",
        }) + ")")
        self.assertEqual(result['version'], "http://ipuz.org/v1")

        result = ipuz.read("ipuz_callback_function(" + json.dumps({
            "version": "http://ipuz.org/v1",
            "kind": "http://ipuz.org/crossword#1",
        }) + ")")
        self.assertEqual(result['version'], "http://ipuz.org/v1")


class IPUZWriteTestCase(unittest.TestCase):

    def test_write_produces_jsonp_string_by_default(self):
        json_data = {}
        result = ipuz.write(json_data)
        expected = ''.join(['ipuz(', json.dumps(json_data), ')'])
        self.assertEqual(result, expected)

    def test_write_produces_json_with_json_only_flag(self):
        json_data = {}
        result = ipuz.write(json_data, json_only=True)
        expected = json.dumps(json_data)
        self.assertEqual(result, expected)
