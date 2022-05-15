import sys
from datetime import datetime

from pytest import raises

sys.path.append("../dateutils/")
from utils.dateutils import JST, UTC, DatetimeParseError, aws_to_dt, ymd_to_dt, ymdhms_to_dt


def test_hyphen():
    dt_str: str = "1970-01-01"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)

    assert ymd_to_dt(dt_str) == answer


def test_slash():
    dt_str: str = "1970/01/01"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)

    assert ymd_to_dt(dt_str) == answer


def test_ymd():
    dt_str: str = "19700101"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)

    assert ymd_to_dt(dt_str) == answer


def test_hyphen_ymd_utc():
    dt_str: str = "1970-01-01"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=UTC)

    assert ymd_to_dt(dt_str, UTC) == answer


def test_slash_ymd_utc():
    dt_str: str = "1970/01/01"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=UTC)

    assert ymd_to_dt(dt_str, UTC) == answer


def test_ymd_utc():
    dt_str: str = "19700101"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=UTC)

    assert ymd_to_dt(dt_str, UTC) == answer


def test_hyphen_ymdhms():
    dt_str: str = "1970-01-01 00:00:00"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)

    assert ymdhms_to_dt(dt_str) == answer


def test_slash_ymdhms():
    dt_str: str = "1970/01/01 00:00:00"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)

    assert ymdhms_to_dt(dt_str) == answer


def test_ymdhms():
    dt_str: str = "19700101000000"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)

    assert ymdhms_to_dt(dt_str) == answer


def test_hyphen_ymdhms_utc():
    dt_str: str = "1970-01-01 00:00:00"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=UTC)

    assert ymdhms_to_dt(dt_str, UTC) == answer


def test_slash_ymdhms_utc():
    dt_str: str = "1970/01/01 00:00:00"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=UTC)

    assert ymdhms_to_dt(dt_str, UTC) == answer


def test_ymdhms_utc():
    dt_str: str = "19700101000000"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=UTC)

    assert ymdhms_to_dt(dt_str, UTC) == answer


def test_aws_utc():
    dt_str: str = "1970-01-01T00:00:00.000Z"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=UTC)

    assert aws_to_dt(dt_str) == answer


def test_aws_jst():
    dt_str: str = "1970-01-01T00:00:00+09"
    answer: datetime = datetime(1970, 1, 1, 0, 0, 0, tzinfo=JST)

    assert aws_to_dt(dt_str) == answer


def test_aws_invalid1():
    dt_str: str = "1970-01-01T00:00:00"
    with raises(DatetimeParseError):
        aws_to_dt(dt_str)


def test_aws_invalid2():
    dt_str: str = "1970-01-01T"
    with raises(DatetimeParseError):
        aws_to_dt(dt_str)
