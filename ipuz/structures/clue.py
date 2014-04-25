from .cluenum import validate_cluenum
from .enumeration import validate_enumeration


def validate_clue(field_data):
    if type(field_data) not in [str, unicode, list, dict]:
        return False
    if type(field_data) is list:
        if len(field_data) != 2:
            return False
        if not validate_cluenum(field_data[0]):
            return False
        if type(field_data[1]) not in [str, unicode]:
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
            elif key == "numbers":
                if type(value) is not list:
                    return False
                for element in value:
                    if not validate_cluenum(element):
                        return False
            elif key == "clue" and type(value) not in [str, unicode]:
                return False
            elif key == "hints":
                if type(value) is not list:
                    return False
                for element in value:
                    if type(element) not in [str, unicode]:
                        return False
            elif key == "image" and type(value) not in [str, unicode]:
                return False
            elif key == "answer" and type(value) not in [str, unicode]:
                return False
            elif key == "enumeration" and not validate_enumeration(value):
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
