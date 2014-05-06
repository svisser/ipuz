from .test_ipuz import IPUZBaseTestCase


class IPUZSampleAcrosticTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/acrostic"],
            "puzzle": []
        }

    def test_validate_mandatory_puzzle_field(self):
        del self.puzzle["puzzle"]
        self.validate("Mandatory field puzzle is missing")

