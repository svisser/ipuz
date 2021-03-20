import json

from ipuz.exceptions import IPUZException
from ipuz.puzzlekinds import IPUZ_PUZZLEKINDS
from ipuz.validators import (
    IPUZ_FIELD_VALIDATORS,
    validate_version,
    get_version_number,
    get_kind_version_number,
)

# The versions of the ipuz standard that this library supports
IPUZ_VERSIONS = list(sorted(IPUZ_FIELD_VALIDATORS.keys()))

# NOTE(maiamcc): currently mandatory fields are the same across all versions;
#   in future, this might need to be broken down into "mandatory fields by version"
IPUZ_MANDATORY_FIELDS = [
    "version",
    "kind",
]


def read(data, puzzlekinds=None):
    try:
        if data.endswith(')'):
            data = data[data.index('(') + 1:-1]
        json_data = json.loads(data)
        if not isinstance(json_data, dict):
            raise ValueError
    except (AttributeError, ValueError):
        raise IPUZException("No valid JSON could be found")
    for field in IPUZ_MANDATORY_FIELDS:
        if field not in json_data:
            raise IPUZException("Mandatory field {} is missing".format(field))

    validate_version("version", json_data["version"], IPUZ_VERSIONS)
    version = get_version_number(json_data["version"])

    for field, value in json_data.items():
        if field in IPUZ_FIELD_VALIDATORS[version]:
            IPUZ_FIELD_VALIDATORS[version][field](field, value)

    for kind in json_data["kind"]:
        if puzzlekinds is not None and kind not in puzzlekinds:
            raise IPUZException("Unsupported kind value found")

    for kind in json_data["kind"]:
        for official_kind, kind_details in IPUZ_PUZZLEKINDS.items():
            if not kind.startswith(official_kind):
                continue
            for field in kind_details["mandatory"]:
                if field not in json_data:
                    raise IPUZException(
                        "Mandatory field {} is missing".format(field)
                    )

            kind_version = get_kind_version_number(kind)
            kind_details_for_version = kind_details["validators"].get(kind_version)
            if not kind_details_for_version:
                raise IPUZException("Unsupported version %s for kind %s found" % (version, kind))

            for field, value in json_data.items():
                if field in kind_details_for_version:
                    validator = kind_details_for_version[field]
                    try:
                        validator(field, value)
                    except TypeError:
                        validator[0](field, value, *validator[1:])
    return json_data


def write(data, jsonp=False, callback_name=None):
    json_string = json.dumps(data)
    if not jsonp:
        return json_string
    if callback_name is None:
        callback_name = "ipuz"
    return ''.join([callback_name, '(', json_string, ')'])
