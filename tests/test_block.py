from .test_ipuz import IPUZBaseTestCase


class IPUZSampleBlockTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/block"],
            "dimensions": {"width": 3, "height": 3},
        }

    def validate(self, expected_exception):
        self.validate_puzzle(self.puzzle, expected_exception)


class IPUZBlockValueTestCase(IPUZSampleBlockTestCase):

    def test_slide_is_bool(self):
        self.puzzle["slide"] = 3
        self.validate("Invalid slide value found")

    def test_move_is_bool(self):
        self.puzzle["move"] = 3
        self.validate("Invalid move value found")

    def test_rotatable_is_bool(self):
        self.puzzle["rotatable"] = 3
        self.validate("Invalid rotatable value found")

    def test_flippable_is_bool(self):
        self.puzzle["flippable"] = 3
        self.validate("Invalid flippable value found")


class IPUZBlockKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/block"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_block_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate_puzzle(self.puzzle, "Mandatory field dimensions is missing")
