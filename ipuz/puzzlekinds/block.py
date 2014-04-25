from ipuz.exceptions import IPUZException
from ipuz.structures import validate_groupspec
from ipuz.validators import validate_bool


def validate_groupspec_dict(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for key, value in field_data.items():
        if type(key) not in [str, unicode] or not key:
            raise IPUZException("Invalid {} value found".format(field_name))
        if not validate_groupspec(value):
            raise IPUZException("Invalid {} value found".format(field_name))


IPUZ_BLOCK_VALIDATORS = {
    "slide": validate_bool,
    "move": validate_bool,
    "rotatable": validate_bool,
    "flippable": validate_bool,
    "enter": validate_groupspec_dict,
    "start": validate_groupspec_dict,
    "saved": validate_groupspec_dict,
    "end": validate_groupspec_dict,
    "exit": validate_groupspec_dict,
}
