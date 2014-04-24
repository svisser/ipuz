from .test_ipuz import IPUZBaseTestCase


class IPUZSampleWordSearchTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/wordsearch"],
            "dimensions": {"width": 3, "height": 3},
        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)


class IPUZWordSearchValueTestCase(IPUZSampleWordSearchTestCase):

    def test_useall_is_bool(self):
        self.puzzle["useall"] = 3
        self.validate("Invalid useall value found")

    def test_retrace_is_bool(self):
        self.puzzle["retrace"] = 3
        self.validate("Invalid retrace value found")

    def test_zigzag_is_bool(self):
        self.puzzle["zigzag"] = 3
        self.validate("Invalid zigzag value found")

    def test_misses_is_dict(self):
        self.puzzle["misses"] = []
        self.validate("Invalid misses value found")

    def test_misses_is_dict_with_non_text_key(self):
        self.puzzle["misses"] = {3: "A"}
        self.validate("Invalid misses value found")

    def test_misses_is_dict_with_non_text_key(self):
        self.puzzle["misses"] = {"A": 3}
        self.validate("Invalid misses value found")

    def test_points_is_text(self):
        self.puzzle["points"] = 3
        self.validate("Invalid points value found")

    def test_time_is_integer(self):
        self.puzzle["time"] = "time"
        self.validate("Invalid time value found")

    def test_time_is_non_negative_integer(self):
        self.puzzle["time"] = -1
        self.validate("Invalid time value found")

    def test_showanswers_is_text(self):
        self.puzzle["showanswers"] = 3
        self.validate("Invalid showanswers value found")

    def test_dictionary_is_text_or_false(self):
        self.puzzle["dictionary"] = 3
        self.validate("Invalid dictionary value found")

    def test_dictionary_is_non_empty_string(self):
        self.puzzle["dictionary"] = ""
        self.validate("Invalid dictionary value found")

    def test_dictionary_is_not_true(self):
        self.puzzle["dictionary"] = True
        self.validate("Invalid dictionary value found")


class IPUZWordSearchKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/wordsearch"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_wordsearch_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate_puzzle(self.puzzle, "Mandatory field dimensions is missing")
