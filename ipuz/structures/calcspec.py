

def validate_calcspec(field_data):
    if type(field_data) is not dict:
        return False
    valid_keys = ("rect", "cells", "value", "operator", "style")
    if any(key not in valid_keys for key in field_data):
        return False
    return True
