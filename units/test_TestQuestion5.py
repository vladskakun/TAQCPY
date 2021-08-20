from tests.TestQuestion5 import list_of_multiples


def test_list_of_multiples_5elements():
    assert list_of_multiples(7, 5) == [7, 14, 21, 28, 35]


def test_list_of_multiples_10elements():
    assert list_of_multiples(12, 10) == [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]


def test_list_of_multiples_6elements():
    assert list_of_multiples(17, 6) == [17, 34, 51, 68, 85, 102]
