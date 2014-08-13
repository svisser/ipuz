import string

import six

from ipuz.exceptions import IPUZException
from ipuz.validators import validate_string


def validate_stylespec_shapebg(field_data):
    return field_data in ["circle"]


def validate_stylespec_highlight(field_data):
    return isinstance(field_data, bool)


def validate_stylespec_named(field_data):
    return field_data is False or isinstance(field_data, six.string_types)


def validate_stylespec_border(field_data):
    return type(field_data) is int and field_data >= 0


def validate_stylespec_divided(field_data):
    return field_data in ["-", "|", "/", "\\", "+", "x"]


def validate_stylespec_mark(field_data):
    return (isinstance(field_data, dict) and
            all(key in ["TL", "TR", "BL", "BR"] for key in field_data.keys()))


def validate_stylespec_slice(field_data):
    return (isinstance(field_data, list) and
            len(field_data) == 4 and
            all(type(c) is int for c in field_data))


def validate_stylespec_side(field_data):
    return (isinstance(field_data, six.string_types) and
            all(c in "TRBL" for c in field_data) and
            0 <= len(field_data) <= 4)


def validate_stylespec_color(field_data):
    if type(field_data) is int:
        return True
    if (isinstance(field_data, six.string_types) and
            len(field_data) == 6 and
            all(c in string.hexdigits for c in field_data)):
        return True
    return False


def validate_stylespec_string(field_data):
    try:
        validate_string("", field_data)
    except IPUZException:
        return False
    return True


IPUZ_STYLESPEC_VALIDATORS = {
    "shapebg": validate_stylespec_shapebg,
    "highlight": validate_stylespec_highlight,
    "named": validate_stylespec_named,
    "border": validate_stylespec_border,
    "divided": validate_stylespec_divided,
    "label": validate_stylespec_string,
    "mark": validate_stylespec_mark,
    "imagebg": validate_stylespec_string,
    "image": validate_stylespec_string,
    "slice": validate_stylespec_slice,
    "barred": validate_stylespec_side,
    "dotted": validate_stylespec_side,
    "dashed": validate_stylespec_side,
    "lessthan": validate_stylespec_side,
    "greaterthan": validate_stylespec_side,
    "equal": validate_stylespec_side,
    "color": validate_stylespec_color,
    "colortext": validate_stylespec_color,
    "colorborder": validate_stylespec_color,
    "colorbar": validate_stylespec_color,
}


def validate_stylespec(style_spec):
    if (style_spec is not None and
            not isinstance(style_spec, (dict, six.string_types))):
        raise IPUZException("StyleSpec is not a name, dictionary or None")
    if isinstance(style_spec, dict):
        for key, value in style_spec.items():
            if key not in IPUZ_STYLESPEC_VALIDATORS:
                raise IPUZException(
                    "StyleSpec contains invalid specifier: {}".format(key)
                )
            if not IPUZ_STYLESPEC_VALIDATORS[key](value):
                raise IPUZException(
                    "StyleSpec has an invalid {} value".format(key)
                )


def validate_stylespec_value(value):
    try:
        validate_stylespec(value)
    except IPUZException:
        return False
    return True
