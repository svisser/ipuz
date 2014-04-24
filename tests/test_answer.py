from .test_ipuz import IPUZBaseTestCase


class IPUZSampleAnswerTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/answer"],
        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)


class IPUZAnswerValueTestCase(IPUZSampleAnswerTestCase):

    def test_randomize_is_bool(self):
        self.puzzle["randomize"] = 3
        self.validate("Invalid randomize value found")
