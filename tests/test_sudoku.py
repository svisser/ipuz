from .test_ipuz import IPUZBaseTestCase


class IPUZSampleSudokuTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/sudoku"],
            "puzzle": [],
        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)


class IPUZSudokuValueTestCase(IPUZSampleSudokuTestCase):

    def test_charset_must_be_text(self):
        self.puzzle["charset"] = 3
        self.validate("Invalid charset value found")

    def test_charset_must_have_length_nine(self):
        self.puzzle["charset"] = "12345"
        self.validate("Invalid charset value found")

    def test_displaycharset_is_bool(self):
        self.puzzle["displaycharset"] = 3
        self.validate("Invalid displaycharset value found")

    def test_boxes_is_bool(self):
        self.puzzle["boxes"] = 3
        self.validate("Invalid boxes value found")

    def test_showoperators_is_bool(self):
        self.puzzle["showoperators"] = 3
        self.validate("Invalid showoperators value found")

    def test_cageborder_is_valid_text(self):
        self.puzzle["cageborder"] = "not-a-border"
        self.validate("Invalid cageborder value found")

    def test_cages_is_list(self):
        self.puzzle["cages"] = 3
        self.validate("Invalid cages value found")

    def test_cages_has_invalid_calcspec(self):
        self.puzzle["cages"] = [3]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_key(self):
        self.puzzle["cages"] = [{"invalid_key": 3}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_empty_calcspec(self):
        self.puzzle["cages"] = [{}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_value(self):
        self.puzzle["cages"] = [{"value": "NaN"}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_operator(self):
        self.puzzle["cages"] = [{"operator": "|"}]
        self.validate("Invalid CalcSpec in cages element found")

    def test_cages_has_calcspec_with_invalid_operator(self):
        self.puzzle["cages"] = [{"style": {"shapebg": "not-a-circle"}}]
        self.validate("Invalid CalcSpec in cages element found")


class IPUZSudokuKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/sudoku"],
            "puzzle": [],
        }

    def test_validate_sudoku_mandatory_puzzle_field(self):
        del self.puzzle["puzzle"]
        self.validate_puzzle(self.puzzle, "Mandatory field puzzle is missing")
