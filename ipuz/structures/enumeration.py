
def validate_enumeration(field_data):
    if type(field_data) not in [str, unicode]:
        return False
    return True
