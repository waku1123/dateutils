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
    string_to_datetime,
)


def test_hyphen_ymd1():
    """
    Hyphen YMD tz省略
    :return:
    """
    dt_str: str = "1970-01-01"
    answer: datetime = datetime(year=1970, month=1, day=1, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=HYPHEN_YMD) == answer


def test_hyphen_ymd2():
    """
    Hyphen YMD tz指定(JST)
    :return:
    """
    dt_str: str = "1970-01-01"
    answer: datetime = datetime(year=1970, month=1, day=1, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=HYPHEN_YMD, tz=JST) == answer


def test_hyphen_ymd3():
    """
    Hyphen YMD tz指定(UTC)
    :return:
    """
    dt_str: str = "1970-01-01"
    answer: datetime = datetime(year=1970, month=1, day=1, tzinfo=UTC)

    assert string_to_datetime(date_string=dt_str, format_string=HYPHEN_YMD, tz=UTC) == answer


def test_hyphen_ymdhms1():
    """
    Hyphen YMDHMS tz省略
    :return:
    """
    dt_str: str = "1970-01-01 00:00:00"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=HYPHEN_YMD_HMS) == answer


def test_hyphen_ymdhms2():
    """
    Hyphen YMDHMS tz指定(JST)
    :return:
    """
    dt_str: str = "1970-01-01 00:00:00"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=HYPHEN_YMD_HMS, tz=JST) == answer


def test_hyphen_ymdhms3():
    """
    Slash YMDHMS tz指定(UTC)
    :return:
    """
    dt_str: str = "1970-01-01 00:00:00"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)

    assert string_to_datetime(date_string=dt_str, format_string=HYPHEN_YMD_HMS, tz=UTC) == answer


def test_slash_ymd1():
    """
    Slash YMD tz省略
    :return:
    """
    dt_str: str = "1970/01/01"
    answer: datetime = datetime(year=1970, month=1, day=1, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=SLASH_YMD) == answer


def test_slash_ymd2():
    """
    Slash YMD tz指定(JST)
    :return:
    """
    dt_str: str = "1970/01/01"
    answer: datetime = datetime(year=1970, month=1, day=1, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=SLASH_YMD, tz=JST) == answer


def test_slash_ymd3():
    """
    Slash YMD tz指定(UTC)
    :return:
    """
    dt_str: str = "1970/01/01"
    answer: datetime = datetime(year=1970, month=1, day=1, tzinfo=UTC)

    assert string_to_datetime(date_string=dt_str, format_string=SLASH_YMD, tz=UTC) == answer


def test_slash_ymdhms1():
    """
    Slash YMDHMS tz省略
    :return:
    """
    dt_str: str = "1970/01/01 00:00:00"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=SLASH_YMD_HMS) == answer


def test_slash_ymdhms2():
    """
    Slash YMDHMS tz指定(JST)
    :return:
    """
    dt_str: str = "1970/01/01 00:00:00"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=SLASH_YMD_HMS, tz=JST) == answer


def test_slash_ymdhms3():
    """
    Slash YMDHMS tz指定(UTC)
    :return:
    """
    dt_str: str = "1970/01/01 00:00:00"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)

    assert string_to_datetime(date_string=dt_str, format_string=SLASH_YMD_HMS, tz=UTC) == answer


def test_ymd1():
    """
    YMD tz省略
    :return:
    """
    dt_str: str = "19700101"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=YMD) == answer


def test_ymd2():
    """
    YMD tz指定(JST)
    :return:
    """
    dt_str: str = "19700101"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=YMD, tz=JST) == answer


def test_ymd3():
    """
    YMD tz指定(UTC)
    :return:
    """
    dt_str: str = "19700101"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)

    assert string_to_datetime(date_string=dt_str, format_string=YMD, tz=UTC) == answer


def test_ymdhms1():
    """
    YMDHMS tz省略
    :return:
    """
    dt_str: str = "19700101000000"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=YMDHMS) == answer


def test_ymdhms2():
    """
    YMDHMS tz指定(JST)
    :return:
    """
    dt_str: str = "19700101000000"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=JST)

    assert string_to_datetime(date_string=dt_str, format_string=YMDHMS, tz=JST) == answer


def test_ymdhms3():
    """
    YMDHMS tz指定(UTC)
    :return:
    """
    dt_str: str = "19700101000000"
    answer: datetime = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)

    assert string_to_datetime(date_string=dt_str, format_string=YMDHMS, tz=UTC) == answer


def test_aws_utc1():
    """
    YYYY-mm-ddTHH:MM:SS.sssZ tz省略
    :return:
    """
    dt_str: str = "1970-01-01T00:00:00.000Z"
    answer: datetime = datetime(
        year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=JST
    )

    assert string_to_datetime(date_string=dt_str, format_string=AWS_DATE_TIME_UTC) == answer


def test_aws_utc2():
    """
    YYYY-mm-ddTHH:MM:SS.sssZ tz指定(JST)
    :return:
    """
    dt_str: str = "1970-01-01T00:00:00.000Z"
    answer: datetime = datetime(
        year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=JST
    )

    assert string_to_datetime(date_string=dt_str, format_string=AWS_DATE_TIME_UTC, tz=JST) == answer


def test_aws_utc3():
    """
    YYYY-mm-ddTHH:MM:SS.sssZ tz指定(UTC)
    :return:
    """
    dt_str: str = "1970-01-01T00:00:00.000Z"
    answer: datetime = datetime(
        year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=UTC
    )

    assert string_to_datetime(date_string=dt_str, format_string=AWS_DATE_TIME_UTC, tz=UTC) == answer


def test_aws_jst1():
    """
    YYYY-mm-ddTHH:MM:SS+09 tz省略
    :return:
    """
    dt_str: str = "1970-01-01T00:00:00+09"
    answer: datetime = datetime(
        year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=JST
    )

    assert string_to_datetime(date_string=dt_str, format_string=AWS_DATE_TIME_JST) == answer


def test_aws_jst2():
    """
    YYYY-mm-ddTHH:MM:SS+09 tz指定(JST)
    :return:
    """
    dt_str: str = "1970-01-01T00:00:00+09"
    answer: datetime = datetime(
        year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=JST
    )

    assert string_to_datetime(date_string=dt_str, format_string=AWS_DATE_TIME_JST, tz=JST) == answer


def test_aws_jst3():
    """
    YYYY-mm-ddTHH:MM:SS+09 tz指定(UTC)
    :return:
    """
    dt_str: str = "1970-01-01T00:00:00+09"
    answer: datetime = datetime(
        year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=UTC
    )

    assert string_to_datetime(date_string=dt_str, format_string=AWS_DATE_TIME_JST, tz=UTC) == answer


def test_date_string_null():
    """
    date_string is null
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string=None, format_string=YMD)


def test_format_null():
    """
    format string is null
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string="19700101", format_string=None)


def test_tz_null():
    """
    tz is null
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string="19700101", format_string=YMD, tz=None)


def test_invalid_arg_type1():
    """
    argument invalid type1
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string=123, format_string=YMD)


def test_invalid_arg_type2():
    """
    argument invalid type2
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string="19700101", format_string=123)


def test_invalid_arg_type3():
    """
    argument invalid type3
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string="19700101", format_string=YMD, tz=123)


def test_invalid_date_string1():
    """
    invalid date string1
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string="9999", format_string=YMD)


def test_invalid_date_string2():
    """
    invalid date string2
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string="98765432", format_string=YMD)


def test_invalid_date_string3():
    """
    invalid date string3
    :return:
    """
    with raises(DatetimeParseError):
        string_to_datetime(date_string="abcdefghijklmn", format_string=YMD)
