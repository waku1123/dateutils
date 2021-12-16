from datetime import datetime, timedelta, timezone
from typing import Final

HYPHEN_YMD: Final[str] = "%Y-%m-%d"
HYPHEN_YMD_HMS: Final[str] = "%Y-%m-%d %H:%M:%S"
SLASH_YMD: Final[str] = "%Y/%m/%d"
SLASH_YMD_HMS: Final[str] = "%Y/%m/%d %H:%M:%S"
YMD: Final[str] = "%Y%m%d"
YMDHMS: Final[str] = "%Y%m%d%H%M%S"
AWS_DATE_TIME_UTC: Final[str] = "%Y-%m-%dT%H:%M:%S.%fZ"
AWS_DATE_TIME_JST: Final[str] = "%Y-%m-%dT%H:%M:%S+09"

JST: timezone = timezone(timedelta(hours=+9), "JST")
UTC: timezone = timezone(timedelta(0), "UTC")


class DatetimeParseError(Exception):
    pass


def string_to_datetime(date_string: str, format_string: str, tz: timezone = JST) -> datetime:
    if date_string is None:
        raise DatetimeParseError("date_string is require")
    if format_string is None:
        raise DatetimeParseError("format_string is require")
    if tz is None:
        raise DatetimeParseError("tz is require")

    try:
        if not isinstance(date_string, str):
            raise TypeError(f"date_string must be a string, but {type(date_string).__name__}")
        if not isinstance(format_string, str):
            raise TypeError(f"format_string must be a string, but {type(format_string).__name__}")
        if not isinstance(tz, timezone):
            raise TypeError(f"tz must be a timezone, but {type(tz).__name__}")

        return datetime.strptime(date_string, format_string).replace(tzinfo=tz)
    except (ValueError, TypeError) as e:
        raise DatetimeParseError(f"{e}")


def ymd_to_dt(date_string: str, tz=JST) -> datetime:
    """
    "19701231" → datetime(1970, 12, 31)
    "1970/12/31" → datetime(1970, 12, 31)
    "1970-12-31" → datetime(1970, 12, 31)
    :param: date_string: YYYY(-|/)?mm(-|/)?dd
    :param: tz: timezone
    :return: datetime
    """
    fmt = YMD
    if "/" in date_string:
        fmt = SLASH_YMD
    if "-" in date_string:
        fmt = HYPHEN_YMD
    return string_to_datetime(date_string=date_string, format_string=fmt, tz=tz)


def ymdhms_to_dt(date_string: str, tz=JST) -> datetime:
    """
    "19701231123456" → datetime(1970, 12, 31, 12, 34, 56)
    "1970/12/31 12:34:56" → datetime(1970, 12, 31, 12, 34, 56)
    "1970-12-31 12:34:56" → datetime(1970, 12, 31, 12, 34, 56)
    :param date_string: YYYY(-|/)?mm(-|/)?dd ?HH:?MM:?SS
    :param tz: timezone
    :return: datetime
    """
    fmt = YMDHMS
    if "/" in date_string:
        fmt = SLASH_YMD_HMS
    if "-" in date_string:
        fmt = HYPHEN_YMD_HMS
    return string_to_datetime(date_string=date_string, format_string=fmt, tz=tz)


def aws_utc_to_dt(date_string: str, tz: timezone = UTC) -> datetime:
    """
    "1970-12-31T12:34:56.789Z" → datetime(1970, 12, 31, 12, 34, 56, 789, timezone=UTC)
    :param date_string:
    :param tz: timezone
    :return:
    """
    return string_to_datetime(date_string=date_string, format_string=AWS_DATE_TIME_UTC, tz=tz)


def aws_jst_to_dt(date_string: str, tz: timezone = JST) -> datetime:
    """
    "1970-12-31T12:34:56+09" → datetime(1970, 12, 31, 12, 34, 56, timezone=JST)
    :param date_string:
    :param tz:
    :return:
    """
    return string_to_datetime(date_string=date_string, format_string=AWS_DATE_TIME_JST, tz=tz)


def dt_to_string(dt: datetime, fmt: str) -> str:
    """
    convert datetime to formatted string
    :param dt: datetime
    :param fmt: format string
    :return: formatted datetime string
    """
    if dt is None:
        raise DatetimeParseError("dt is require")
    if fmt is None:
        raise DatetimeParseError("fmt is require")
    if not isinstance(fmt, str):
        raise DatetimeParseError("fmt must be a string")
    return dt.strftime(fmt)


def get_utc_now() -> datetime:
    """
    current datetime at UTC
    :return: datetime
    """
    return datetime.now(tz=UTC)


def get_jts_now() -> datetime:
    """
    current datetime at JST
    :return:
    """
    return datetime.now(tz=JST)


# TODO: UTC to JST
# TODO: add x days
# TODO: add x hours
# TODO: get weekday
# TODO: unix time offset
if __name__ == "__main__":

    utc_now = get_utc_now()
    jst_now = get_jts_now()
    print(utc_now)
    print(jst_now)
