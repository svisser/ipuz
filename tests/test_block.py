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

    def test_field_is_not_a_list(self):
        self.puzzle["field"] = 3
        self.validate("Invalid field value found")

    def test_field_contains_not_a_list(self):
        self.puzzle["field"] = [[], [], 3]
        self.validate("Invalid field value found")

    def test_field_contains_invalid_styledcell(self):
        self.puzzle["field"] = [[[]]]
        self.validate("Invalid StyledCell in field element found")

    def test_field_contains_invalid_styledcell_empty_dict(self):
        self.puzzle["field"] = [[{}]]
        self.validate("Invalid StyledCell in field element found")

    def test_field_contains_invalid_styledcell_invalid_dict_key(self):
        self.puzzle["field"] = [[{"invalid_key": 3}]]
        self.validate("Invalid StyledCell in field element found")

    def test_field_contains_invalid_styledcell_invalid_cell(self):
        self.puzzle["field"] = [[{"cell": []}]]
        self.validate("Invalid StyledCell in field element found")

    def test_field_contains_invalid_styledcell_invalid_style(self):
        self.puzzle["field"] = [[{"style": {"shapebg": "not-a-circle"}}]]
        self.validate("Invalid StyledCell in field element found")


class IPUZBlockKindTestCase(IPUZBaseTestCase):

    def setUp(self):
        self.puzzle = {
            "version": "http://ipuz.org/v1",
            "kind": ["http://ipuz.org/block"],
            "dimensions": {"width": 3, "height": 3},
        }

    def test_invalid_dimensions_field_type(self):
        self.puzzle["dimensions"] = ["width", "height"]
        self.validate_puzzle(
            self.puzzle,
            "Invalid dimensions value found"
        )

    def test_validate_block_mandatory_dimensions_field(self):
        del self.puzzle["dimensions"]
        self.validate_puzzle(
            self.puzzle,
            "Mandatory field dimensions is missing"
        )

    def test_validate_incomplete_dimensions(self):
        del self.puzzle["dimensions"]["width"]
        self.validate_puzzle(
            self.puzzle,
            "Mandatory field width of dimensions is missing"
        )

    def test_validate_dimensions_not_an_int(self):
        self.puzzle["dimensions"]["width"] = "not an integer"
        self.validate_puzzle(
            self.puzzle,
            "Invalid width value in dimensions field found"
        )

    def test_validate_dimensions_negative_or_zero(self):
        self.puzzle["dimensions"]["width"] = 0
        self.validate_puzzle(
            self.puzzle,
            "Field width of dimensions is less than one"
        )
