from tests.TestQuestion3 import solutions


def test_solutions_2roots():
    assert solutions(1, 0, -1) == 2


def test_solutions_1root():
    assert solutions(1, 0, 0) == 1


def test_solutions_0root():
    assert solutions(1, 0, 1) == 0
