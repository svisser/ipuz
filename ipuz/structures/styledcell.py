import six

from ipuz.exceptions import IPUZException
from .stylespec import validate_stylespec


def validate_styledcell(field_data):
    if (field_data is not None and
            type(field_data) not in [int, dict] and
            not isinstance(field_data, six.string_types)):
        return False
    if isinstance(field_data, dict):
        if not field_data:
            return False
        if not all(key in ("cell", "style") for key in field_data):
            return False
        if ("cell" in field_data and
                field_data["cell"] is not None and
                type(field_data["cell"]) is not int and
                not isinstance(field_data["cell"], six.string_types)):
            return False
        if "style" in field_data:
            try:
                validate_stylespec(field_data["style"])
            except IPUZException:
                return False
    return True
