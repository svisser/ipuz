import six

from .cluenum import validate_cluenum
from .enumeration import validate_enumeration


def validate_clue(field_data):
    def validate_list_of_cluenum(value):
        if type(value) is not list:
            return False
        for element in value:
            if not validate_cluenum(element):
                return False
        return True

    if type(field_data) not in [list, dict] and not isinstance(field_data, six.string_types):
        return False
    if type(field_data) is list:
        if len(field_data) != 2:
            return False
        if not validate_cluenum(field_data[0]):
            return False
        if not isinstance(field_data[1], six.string_types):
            return False
    if type(field_data) is dict:
        for key, value in field_data.items():
            if key not in (
                "number",
                "numbers",
                "clue",
                "hints",
                "image",
                "answer",
                "enumeration",
                "references",
                "see",
                "highlight",
                "location",
            ):
                return False
            if key == "number" and not validate_cluenum(value):
                return False
            elif key == "numbers" and not validate_list_of_cluenum(value):
                return False
            elif key == "clue" and not isinstance(value, six.string_types):
                return False
            elif key == "hints":
                if type(value) is not list:
                    return False
                for element in value:
                    if not isinstance(element, six.string_types):
                        return False
            elif key == "image" and not isinstance(value, six.string_types):
                return False
            elif key == "answer" and not isinstance(value, six.string_types):
                return False
            elif key == "enumeration" and not validate_enumeration(value):
                return False
            elif key == "references" and not validate_list_of_cluenum(value):
                return False
            elif key == "see" and not validate_cluenum(value):
                return False
            elif key == "highlight" and type(value) is not bool:
                return False
            elif key == "location":
                if (type(value) is not list or
                    len(value) != 2 or
                    any(type(e) is not int for e in value)):
                    return False
    return True
