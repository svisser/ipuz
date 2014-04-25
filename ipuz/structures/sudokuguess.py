

def validate_sudokuguess(field_data):
    if type(field_data) not in [int, str, unicode, list]:
        return False
    return True
