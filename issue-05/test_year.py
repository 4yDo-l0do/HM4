import urllib.request
import json
import io
import pytest
from unittest.mock import patch

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def test_request():
    actual = what_is_year_now()
    expected = 2021
    assert expected == actual


def test_ymd():
    """тест формата YYYY-MM-DD"""
    data = io.StringIO('{"currentDateTime":"2021-12-01"}')
    expected = 2021
    with patch.object(urllib.request, 'urlopen', return_value=data):
        actual = what_is_year_now()

    assert actual == expected


def test_dmy():
    """тест формата DD.MM.YYYY"""
    data = io.StringIO('{"currentDateTime":"01.12.2021"}')
    expected = 2021
    with patch.object(urllib.request, 'urlopen', return_value=data):
        actual = what_is_year_now()

    assert actual == expected


def test_format():
    """тест на перехват исключения"""
    data = io.StringIO('{"currentDateTime":"01/12/2021"}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_return_type():
    """проверить возвращаемое значение"""
    data = io.StringIO('{"currentDateTime":"01.12.2021"}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        actual = what_is_year_now()

    assert isinstance(actual, int)


def test_key():
    """тест с неверным ключем"""
    data = io.StringIO('{"DateTime":"01/12/2021"}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        with pytest.raises(KeyError):
            what_is_year_now()


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


