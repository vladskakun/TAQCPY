from tests.TestQuestion2 import profit


def test_profit_1():
    assert profit(32.67, 45, 1200) == 14796


def test_profit_2():
    assert profit(225.89, 550, 100) == 32411


def test_profit_3():
    assert profit(2.77, 7.95, 8500) == 44030
