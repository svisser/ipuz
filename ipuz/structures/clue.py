

def validate_clue(field_data):
    if type(field_data) not in [str, unicode, list, dict]:
        return False
    if type(field_data) is list:
        if len(field_data) != 2:
            return False
        if type(field_data[0]) not in [int, str, unicode]:
            return False
        if type(field_data[1]) not in [str, unicode]:
            return False
    return True
