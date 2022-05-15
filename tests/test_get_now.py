import sys
from datetime import datetime

from pytest import raises

sys.path.append("../dateutils/")
from utils.dateutils import (AWS_DATE_TIME_JST, AWS_DATE_TIME_UTC, HYPHEN_YMD,
                             HYPHEN_YMD_HMS, JST, SLASH_YMD, SLASH_YMD_HMS,
                             UTC, YMD, YMDHMS, DatetimeParseError, get_jts_now,
                             get_utc_now)


def test_get_utc_now():
    assert get_utc_now() is not None
    assert isinstance(get_utc_now(), datetime)
    assert get_utc_now().tzinfo is UTC


def test_get_jst_now():
    assert get_jts_now() is not None
    assert isinstance(get_jts_now(), datetime)
    assert get_jts_now().tzinfo is JST
