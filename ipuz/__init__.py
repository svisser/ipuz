import json

from exceptions import IPUZException


IPUZ_MANDATORY_FIELDS = (
    "version",
    "kind",
)


def read(data):
    if data.startswith('ipuz(') and data.endswith(')'):
        data = data[5:-1]
    try:
        json_data = json.loads(data)
    except ValueError:
        raise IPUZException("No valid JSON could be found")

    for field in IPUZ_MANDATORY_FIELDS:
        if field not in json_data:
            raise IPUZException("Mandatory field {} is missing".format(field))

    return json_data


def write(data, json_only=False):
    pass
