from datetime import datetime, timedelta, timezone
from typing import Final, List, Optional, Union

HYPHEN_YMD: Final[str] = "%Y-%m-%d"
HYPHEN_YMD_HMS: Final[str] = "%Y-%m-%d %H:%M:%S"
SLASH_YMD: Final[str] = "%Y/%m/%d"
SLASH_YMD_HMS: Final[str] = "%Y/%m/%d %H:%M:%S"
YMD: Final[str] = "%Y%m%d"
YMDHMS: Final[str] = "%Y%m%d%H%M%S"
AWS_DATE_TIME_UTC: Final[str] = "%Y-%m-%dT%H:%M:%S.%fZ"
AWS_DATE_TIME_JST: Final[str] = "%Y-%m-%dT%H:%M:%S+09"

JST: Final[timezone] = timezone(timedelta(hours=+9), "JST")
UTC: Final[timezone] = timezone(timedelta(hours=+0), "UTC")


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


def aws_to_dt(date_string: str) -> datetime:
    """
    "1970-12-31T12:34:56.789Z" → datetime(1970, 12, 31, 12, 34, 56, 789, timezone=UTC)
    "1970-12-31T12:34:56+09" → datetime(1970, 12, 31, 12, 34, 56, timezone=JST)
    :param date_string:
    :return:
    """
    tz: Optional[timezone] = None
    fmt: Optional[str] = None
    if date_string.endswith("Z"):
        tz = UTC
        fmt = AWS_DATE_TIME_UTC
    if date_string.endswith("+09"):
        tz = JST
        fmt = AWS_DATE_TIME_JST
    return string_to_datetime(date_string=date_string, format_string=fmt, tz=tz)


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
    if not isinstance(dt, datetime):
        raise DatetimeParseError("dt must be a datetime")
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


def convert_tz_utc_jst(dt: datetime) -> datetime:
    """
    convert datetime timezone JST <--> UTC
    :param dt:
    :return:
    """
    if dt is None:
        raise DatetimeParseError("dt is require")
    if not isinstance(dt, datetime):
        raise DatetimeParseError(f"dt must be a datetime, but {type(dt).__name__}")
    tzinfo = dt.tzinfo
    if tzinfo is None:
        raise DatetimeParseError("dt must be a datetime with timezone")
    if tzinfo == JST:
        return dt.astimezone(tz=UTC)
    elif tzinfo == UTC:
        return dt.astimezone(tz=JST)


def add_days(dt: datetime, days: int = 0):
    """
    add x days to datetime
    :param dt:
    :param days:
    :return:
    """
    if dt is None:
        raise DatetimeParseError("dt is require")
    if days is None:
        raise DatetimeParseError("days is require")

    if not isinstance(dt, datetime):
        raise DatetimeParseError("dt must be a datetime")
    if not isinstance(days, int):
        raise DatetimeParseError("days must be a int")
    return dt + timedelta(days=days)


def add_hours(dt: datetime, hours: int = 0):
    """
    add x hours to datetime
    :param dt:
    :param hours:
    :return:
    """
    if dt is None:
        raise DatetimeParseError("dt is require")
    if hours is None:
        raise DatetimeParseError("hours is require")

    if not isinstance(dt, datetime):
        raise DatetimeParseError("dt must be a datetime")
    if not isinstance(hours, int):
        raise DatetimeParseError("days must be a int")
    return dt + timedelta(hours=hours)


def weekday_index(dt: datetime) -> int:
    """
    0: Monday, 1: Tuesday, ..., 6: Sunday
    :param dt:
    :return:
    """
    if dt is None:
        raise DatetimeParseError("dt is require")
    if not isinstance(dt, datetime):
        raise DatetimeParseError("dt must be a datetime")
    return dt.weekday()


def weekday_name_en(dt: datetime):
    """
    get Weekday name in English
    :param dt:
    :return:
    """
    names: List[str] = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return names[weekday_index(dt)]


def weekday_name_jp(dt: datetime):
    """
    get Weekday name in Japanese
    :param dt:
    :return:
    """
    names: List[str] = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    return names[weekday_index(dt)]


def dt_to_unix_time(dt: datetime) -> float:
    """
    get Unix time from datetime
    :param dt:
    :return:
    """
    if dt is None:
        raise DatetimeParseError("dt is require")
    if not isinstance(dt, datetime):
        raise DatetimeParseError("dt must be a datetime")
    return dt.timestamp()


def unix_time_to_dt(ut: Union[float, int], tz=JST) -> datetime:
    """
    get datetime from Unix time
    :param ut:
    :param tz:
    :return:
    """
    if ut is None:
        raise DatetimeParseError("ut is require")
    if not isinstance(ut, float) and not isinstance(ut, int):
        raise DatetimeParseError("ut must be a float or int")
    return datetime.fromtimestamp(ut).replace(tzinfo=tz)
