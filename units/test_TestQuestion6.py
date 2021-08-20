from tests.TestQuestion6 import format_date


def test_format_date_1():
    assert format_date("11/12/2019") == "20191211"


def test_format_date_2():
    assert format_date("12/31/2019") == "20193112"


def test_format_date_3():
    assert format_date("01/15/2019") == "20191501"