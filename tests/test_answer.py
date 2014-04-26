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

    def test_choices_is_list(self):
        self.puzzle["choices"] = 3
        self.validate("Invalid choices value found")

    def test_choices_contains_strings(self):
        self.puzzle["choices"] = [3]
        self.validate("Invalid choices value found")

    def test_answer_is_a_string(self):
        self.puzzle["answer"] = 3
        self.validate("Invalid answer value found")

    def test_answers_is_a_list(self):
        self.puzzle["answers"] = 3
        self.validate("Invalid answers value found")

    def test_answers_contains_strings(self):
        self.puzzle["answers"] = [3]
        self.validate("Invalid answers value found")

    def test_requiredanswers_contains_strings(self):
        self.puzzle["requiredanswers"] = "circle"
        self.validate("Invalid requiredanswers value found")

    def test_requiredanswers_must_be_positive(self):
        self.puzzle["requiredanswers"] = -3
        self.validate("Invalid requiredanswers value found")

    def test_guesses_is_a_list(self):
        self.puzzle["guesses"] = 3
        self.validate("Invalid guesses value found")

    def test_guesses_contains_strings(self):
        self.puzzle["guesses"] = [3]
        self.validate("Invalid guesses value found")

    def test_misses_is_dict(self):
        self.puzzle["misses"] = []
        self.validate("Invalid misses value found")

    def test_misses_is_dict_with_non_text_value(self):
        self.puzzle["misses"] = {"A": 3}
        self.validate("Invalid misses value found")

    def test_enumeration_is_string(self):
        self.puzzle["enumeration"] = 3
        self.validate("Invalid enumeration value found")

    def test_enumerations_is_list(self):
        self.puzzle["enumerations"] = 3
        self.validate("Invalid enumerations value found")

    def test_enumerations_is_list_with_strings(self):
        self.puzzle["enumerations"] = [3]
        self.validate("Invalid Enumeration in enumerations element found")
