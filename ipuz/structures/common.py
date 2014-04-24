

def validate_cells(field_data):
    if type(field_data) is not list or not field_data:
        return False
    for element in field_data:
        if type(element) is not list or len(element) != 2 or not all(type(e) is int for e in element):
            return False
    return True


def validate_rect(field_data):
    if type(field_data) is not list:
        return False
    if len(field_data) != 4 or not all(type(c) is int for c in field_data):
        return False
    if field_data[0] > field_data[2] or field_data[1] > field_data[3]:
        return False
    return True
