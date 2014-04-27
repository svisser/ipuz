import json

from ipuz.exceptions import IPUZException
from ipuz.puzzlekinds import IPUZ_PUZZLEKINDS
from ipuz.structures import (
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


def read(data, puzzlekinds=None):
    try:
        if data.endswith(')'):
            data = data[data.index('(') + 1:-1]
        json_data = json.loads(data)
        if type(json_data) is not dict:
            raise ValueError
    except (AttributeError, ValueError):
        raise IPUZException("No valid JSON could be found")
    for field in IPUZ_MANDATORY_FIELDS:
        if field not in json_data:
            raise IPUZException("Mandatory field {} is missing".format(field))
    for field, value in json_data.items():
        if field in IPUZ_FIELD_VALIDATORS:
            IPUZ_FIELD_VALIDATORS[field](field, value)
    for kind in json_data["kind"]:
        if puzzlekinds is not None and kind not in puzzlekinds:
            raise IPUZException("Unsupported kind value found")
    for kind in json_data["kind"]:
        for official_kind, kind_details in IPUZ_PUZZLEKINDS.items():
            if not kind.startswith(official_kind):
                continue
            for field in kind_details["mandatory"]:
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
