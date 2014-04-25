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

    def test_enter_is_dict(self):
        self.puzzle["enter"] = 3
        self.validate("Invalid enter value found")

    def test_enter_has_non_empty_keys(self):
        self.puzzle["enter"] = { "": {"cells": [[1, 1]]}}
        self.validate("Invalid enter value found")

    def test_enter_has_invalid_groupspec(self):
        self.puzzle["enter"] = { "name": {"invalid_key": 3}}
        self.validate("Invalid enter value found")

    def test_start_is_dict(self):
        self.puzzle["start"] = 3
        self.validate("Invalid start value found")

    def test_start_has_non_empty_keys(self):
        self.puzzle["start"] = { "": {"cells": [[1, 1]]}}
        self.validate("Invalid start value found")

    def test_start_has_invalid_groupspec(self):
        self.puzzle["start"] = { "name": {"invalid_key": 3}}
        self.validate("Invalid start value found")

    def test_saved_is_dict(self):
        self.puzzle["saved"] = 3
        self.validate("Invalid saved value found")

    def test_saved_has_non_empty_keys(self):
        self.puzzle["saved"] = { "": {"cells": [[1, 1]]}}
        self.validate("Invalid saved value found")

    def test_saved_has_invalid_groupspec(self):
        self.puzzle["saved"] = { "name": {"invalid_key": 3}}
        self.validate("Invalid saved value found")

    def test_end_is_dict(self):
        self.puzzle["end"] = 3
        self.validate("Invalid end value found")

    def test_end_has_non_empty_keys(self):
        self.puzzle["end"] = { "": {"cells": [[1, 1]]}}
        self.validate("Invalid end value found")

    def test_end_has_invalid_groupspec(self):
        self.puzzle["end"] = { "name": {"invalid_key": 3}}
        self.validate("Invalid end value found")

    def test_exit_is_dict(self):
        self.puzzle["exit"] = 3
        self.validate("Invalid exit value found")

    def test_exit_has_non_empty_keys(self):
        self.puzzle["exit"] = { "": {"cells": [[1, 1]]}}
        self.validate("Invalid exit value found")

    def test_exit_has_invalid_groupspec(self):
        self.puzzle["exit"] = { "name": {"invalid_key": 3}}
        self.validate("Invalid exit value found")


class IPUZBlockKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/block"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_validate_block_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate_puzzle(
            self.puzzle,
            "Mandatory field dimensions is missing"
        )
