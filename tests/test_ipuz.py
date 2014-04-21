import json
import unittest

import ipuz


class IPUZTestCase(unittest.TestCase):

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
