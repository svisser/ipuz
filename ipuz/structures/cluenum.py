

def validate_cluenum(field_data):
    return type(field_data) is int or isinstance(field_data, str)
