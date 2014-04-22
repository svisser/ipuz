from datetime import datetime
import json

from ipuz.exceptions import IPUZException
from ipuz.groupspec import validate_groupspec
from ipuz.stylespec import validate_stylespec


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


def validate_styles(field_data):
    for _, stylespec in field_data.items():
        validate_stylespec(stylespec)


def validate_zones(field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid zones value found")
    for element in field_data:
        if not validate_groupspec(element):
            raise IPUZException("Invalid GroupSpec in zones element found")


IPUZ_FIELD_VALIDATORS = {
    "dimensions": validate_dimensions,
    "date": validate_date,
    "styles": validate_styles,
}
IPUZ_CROSSWORD_VALIDATORS = {
    "zones": validate_zones,
}
IPUZ_PUZZLEKIND_VALIDATORS = {
    "http://ipuz.org/crossword": IPUZ_CROSSWORD_VALIDATORS,
    "http://ipuz.org/sudoku": {},
    "http://ipuz.org/block": {},
    "http://ipuz.org/wordsearch": {},
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
                if field in IPUZ_PUZZLEKIND_VALIDATORS[official_kind]:
                    IPUZ_PUZZLEKIND_VALIDATORS[official_kind][field](value)
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
