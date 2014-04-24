import json

from ipuz.exceptions import IPUZException
from ipuz.puzzlekinds.answer import IPUZ_ANSWER_VALIDATORS
from ipuz.puzzlekinds.block import IPUZ_BLOCK_VALIDATORS
from ipuz.puzzlekinds.crossword import IPUZ_CROSSWORD_VALIDATORS
from ipuz.puzzlekinds.sudoku import IPUZ_SUDOKU_VALIDATORS
from ipuz.puzzlekinds.wordsearch import IPUZ_WORDSEARCH_VALIDATORS
from ipuz.structures import (
    validate_crosswordvalue,
    validate_groupspec,
    validate_stylespec,
)
from ipuz.validators import IPUZ_FIELD_VALIDATORS


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
IPUZ_PUZZLEKINDS = {
    "http://ipuz.org/crossword": {
        "mandatory": (
            "dimensions",
            "puzzle",
        ),
        "validators": IPUZ_CROSSWORD_VALIDATORS,
    },
    "http://ipuz.org/sudoku": {
        "mandatory": (
            "puzzle",
        ),
        "validators": IPUZ_SUDOKU_VALIDATORS,
    },
    "http://ipuz.org/block": {
        "mandatory": (
            "dimensions",
        ),
        "validators": IPUZ_BLOCK_VALIDATORS,
    },
    "http://ipuz.org/answer": {
        "mandatory": (),
        "validators": IPUZ_ANSWER_VALIDATORS,
    },
    "http://ipuz.org/wordsearch": {
        "mandatory": (
            "dimensions",
        ),
        "validators": IPUZ_WORDSEARCH_VALIDATORS,
    },
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
    for field, value in json_data.items():
        if field in IPUZ_FIELD_VALIDATORS:
            IPUZ_FIELD_VALIDATORS[field](field, value)
    for kind in json_data["kind"]:
        for official_kind, kind_details in IPUZ_PUZZLEKINDS.items():
            fields = kind_details["mandatory"]
            if not kind.startswith(official_kind):
                continue
            for field in fields:
                if field not in json_data:
                    raise IPUZException("Mandatory field {} is missing".format(field))
            for field, value in json_data.items():
                if field in kind_details["validators"]:
                    kind_details["validators"][field](field, value)
    return json_data


def write(data, callback_name=None, json_only=False):
    json_string = json.dumps(data)
    if json_only:
        return json_string
    if callback_name is None:
        callback_name = "ipuz"
    return ''.join([callback_name, '(', json_string, ')'])
