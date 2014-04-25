from datetime import datetime

from ipuz.exceptions import IPUZException
from ipuz.structures import validate_stylespec


def validate_bool(field_name, field_data):
    if type(field_data) is not bool:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_int(field_name, field_data):
    if type(field_data) is not int:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_dict_of_strings(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for key, value in field_data.items():
        if type(key) not in [str, unicode] or type(value) not in [str, unicode]:
            raise IPUZException("Invalid {} value found".format(field_name))


def validate_list_of_strings(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if type(element) not in [str, unicode]:
            raise IPUZException("Invalid {} value found".format(field_name))


def validate_version(field_name, field_data):
    if field_data != "http://ipuz.org/v1":
        raise IPUZException("Invalid or unsupported version value found")


def validate_kind(field_name, field_data):
    if type(field_data) is not list or not field_data:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if type(element) not in [str, unicode]:
            raise IPUZException("Invalid {} value found".format(field_name))


def validate_date(field_name, field_data):
    try:
        datetime.strptime(field_data, '%m/%d/%Y')
    except ValueError:
        raise IPUZException("Invalid date format: {}".format(field_data))


def validate_styles(field_name, field_data):
    for _, stylespec in field_data.items():
        validate_stylespec(stylespec)


IPUZ_FIELD_VALIDATORS = {
    "version": validate_version,
    "kind": validate_kind,
    "date": validate_date,
    "styles": validate_styles,
}
