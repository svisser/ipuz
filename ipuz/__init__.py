from datetime import datetime
import json
import string
import types

from exceptions import IPUZException


IPUZ_MANDATORY_FIELDS = (
    "version",
    "kind",
)
IPUZ_OPTIONAL_FIELDS = (
    "copyright",
    "publisher",
    "publication",
    "url",
    "uniqueid",
    "title",
    "intro",
    "explanation",
    "annotation",
    "author",
    "editor",
    "date",
    "notes",
    "difficulty",
    "origin",
    "block",
    "empty",
    "styles",
)
IPUZ_CROSSWORD_MANDATORY_FIELDS = (
    "dimensions",
    "puzzle",
)
IPUZ_SUDOKU_MANDATORY_FIELDS = (
    "puzzle",
)
IPUZ_BLOCK_MANDATORY_FIELDS = (
    "dimensions",
)
IPUZ_WORDSEARCH_MANDATORY_FIELDS = (
    "dimensions",
)
IPUZ_PUZZLEKIND_MANDATORY_FIELDS = {
    "http://ipuz.org/crossword": IPUZ_CROSSWORD_MANDATORY_FIELDS,
    "http://ipuz.org/sudoku": IPUZ_SUDOKU_MANDATORY_FIELDS,
    "http://ipuz.org/block": IPUZ_BLOCK_MANDATORY_FIELDS,
    "http://ipuz.org/wordsearch": IPUZ_WORDSEARCH_MANDATORY_FIELDS,
}
IPUZ_STYLESPEC_SPECIFIERS = (
    "shapebg",
    "highlight",
    "named",
    "border",
    "divided",
    "label",
    "mark",
    "imagebg",
    "image",
    "slice",
    "barred",
    "dotted",
    "dashed",
    "lessthan",
    "greaterthan",
    "equal",
    "color",
    "colortext",
    "colorborder",
    "colorbar",
)


def validate_dimensions(field_data):
    for key in ["width", "height"]:
        if key not in field_data:
            raise IPUZException(
                "Mandatory field {} of dimensions is missing".format(key)
            )
        if field_data[key] < 1:
            raise IPUZException(
                "Field {} of dimensions is less than one".format(key)
            )


def validate_date(field_data):
    try:
        datetime.strptime(field_data, '%m/%d/%Y')
    except ValueError:
        raise IPUZException("Invalid date format: {}".format(field_data))


def validate_stylespec_shapebg(name, field_data):
    if field_data not in ["circle"]:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))


def validate_stylespec_highlight(name, field_data):
    if field_data not in [True, False]:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))


def validate_stylespec_named(name, field_data):
    if type(field_data) is bool and field_data:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))
    if type(field_data) not in [str, unicode]:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))


def validate_stylespec_border(name, field_data):
    if type(field_data) not in [int] or field_data < 0:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))


def validate_stylespec_side(name, field_data):
    if not field_data or not all(c in "TRBL" for c in field_data):
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))


def validate_stylespec_color(name, field_data):
    if type(field_data) not in [int, str, unicode]:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))
    if type(field_data) in [str, unicode]:
        if len(field_data) != 6 or not all(c in string.hexdigits for c in field_data):
            raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))


def validate_stylespec_divided(name, field_data):
    if field_data not in ["-", "|", "/", "\\", "+", "x"]:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))


def validate_stylespec_mark(name, field_data):
    if type(field_data) not in [dict]:
        raise IPUZException("Style with invalid {} value found: {}".format(name, field_data))
    for key, value in field_data.items():
        if key not in ["TL", "TR", "BL", "BR"]:
            raise IPUZException("Style with invalid {} corner identifier found: {}".format(name, key))



IPUZ_STYLESPEC_VALIDATORS = {
    "shapebg": validate_stylespec_shapebg,
    "highlight": validate_stylespec_highlight,
    "named": validate_stylespec_named,
    "border": validate_stylespec_border,
    "divided": validate_stylespec_divided,
    "mark": validate_stylespec_mark,
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


def validate_styles(field_data):
    for name, style_spec in field_data.items():
        if type(style_spec) not in [str, unicode, dict, types.NoneType]:
            raise IPUZException("Style {} in field styles is not a name, dictionary or None".format(name))
        if isinstance(style_spec, dict):
            for key, value in style_spec.items():
                if key not in IPUZ_STYLESPEC_SPECIFIERS:
                    raise IPUZException("Style {} in field styles contains invalid specifier: {}".format(name, key))
                if key in IPUZ_STYLESPEC_VALIDATORS:
                    IPUZ_STYLESPEC_VALIDATORS[key](key, value)


IPUZ_FIELD_VALIDATORS = {
    "dimensions": validate_dimensions,
    "date": validate_date,
    "styles": validate_styles,
}


def read(data):
    if data.endswith(')'):
        data = data[data.index('(') + 1:-1]
    try:
        json_data = json.loads(data)
    except ValueError:
        raise IPUZException("No valid JSON could be found")
    for field in IPUZ_MANDATORY_FIELDS:
        if field not in json_data:
            raise IPUZException("Mandatory field {} is missing".format(field))
    for kind in json_data["kind"]:
        for official_kind, fields in IPUZ_PUZZLEKIND_MANDATORY_FIELDS.items():
            if official_kind not in kind:
                continue
            for field in fields:
                if field not in json_data:
                    raise IPUZException("Mandatory field {} is missing".format(field))
    for field, value in json_data.items():
        if field in IPUZ_FIELD_VALIDATORS:
            IPUZ_FIELD_VALIDATORS[field](value)
    return json_data


def write(data, callback_name=None, json_only=False):
    if callback_name is None:
        callback_name = "ipuz"
    json_string = json.dumps(data)
    if json_only:
        return json_string
    return ''.join([callback_name, '(', json_string, ')'])
