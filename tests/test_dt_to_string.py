import sys
from datetime import datetime

from pytest import raises

sys.path.append("../dateutils/")
from dateutils import (
    AWS_DATE_TIME_JST,
    AWS_DATE_TIME_UTC,
    HYPHEN_YMD,
    HYPHEN_YMD_HMS,
    JST,
    SLASH_YMD,
    SLASH_YMD_HMS,
    UTC,
    YMD,
    YMDHMS,
    DatetimeParseError,
    dt_to_string,
)

dt: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)


def test_to_hyphen_ymd():
    answer: str = "1970-01-01"
    assert dt_to_string(dt=dt, fmt=HYPHEN_YMD) == answer


def test_to_slash_ymd():
    answer: str = "1970/01/01"
    assert dt_to_string(dt=dt, fmt=SLASH_YMD) == answer


def test_to_ymd():
    answer: str = "19700101"
    assert dt_to_string(dt=dt, fmt=YMD) == answer


def test_to_hyphen_ymdhms():
    answer: str = "1970-01-01 00:00:00"
    assert dt_to_string(dt=dt, fmt=HYPHEN_YMD_HMS) == answer


def test_to_slash_ymdhms():
    answer: str = "1970/01/01 00:00:00"
    assert dt_to_string(dt=dt, fmt=SLASH_YMD_HMS) == answer


def test_to_ymdhms():
    answer: str = "19700101000000"
    assert dt_to_string(dt=dt, fmt=YMDHMS) == answer


def test_to_aws_utc():
    answer: str = "1970-01-01T00:00:00.000000Z"
    assert dt_to_string(dt=dt, fmt=AWS_DATE_TIME_UTC) == answer


def test_to_aws_jst():
    answer: str = "1970-01-01T00:00:00+09"
    assert dt_to_string(dt=dt, fmt=AWS_DATE_TIME_JST) == answer


def test_to_string_invalid1():
    with raises(DatetimeParseError):
        dt_to_string(dt=None, fmt=HYPHEN_YMD)


def test_to_string_invalid2():
    with raises(DatetimeParseError):
        dt_to_string(dt=dt, fmt=None)


def test_to_string_invalid3():
    with raises(DatetimeParseError):
        dt_to_string(dt="", fmt=HYPHEN_YMD)


def test_to_string_invalid4():
    with raises(DatetimeParseError):
        dt_to_string(dt=dt, fmt=5)


def test_to_string_invalid5():
    answer: str = ""
    assert dt_to_string(dt=dt, fmt="") == answer
