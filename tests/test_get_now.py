from datetime import datetime

from libs.dateutils import JST, UTC, get_jts_now, get_utc_now


def test_get_utc_now():
    assert get_utc_now() is not None
    assert isinstance(get_utc_now(), datetime)
    assert get_utc_now().tzinfo is UTC


def test_get_jst_now():
    assert get_jts_now() is not None
    assert isinstance(get_jts_now(), datetime)
    assert get_jts_now().tzinfo is JST
