import json

from exceptions import IPUZException


IPUZ_MANDATORY_FIELDS = (
    "version",
    "kind",
)
IPUZ_CROSSWORD_MANDATORY_FIELDS = (
    "dimensions",
    "puzzle",
)


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
        if "http://ipuz.org/crossword" in kind:
            for field in IPUZ_CROSSWORD_MANDATORY_FIELDS:
                if field not in json_data:
                    raise IPUZException("Mandatory field {} is missing".format(field))
    return json_data


def write(data, callback_name=None, json_only=False):
    if callback_name is None:
        callback_name = "ipuz"
    json_string = json.dumps(data)
    if json_only:
        return json_string
    return ''.join([callback_name, '(', json_string, ')'])
