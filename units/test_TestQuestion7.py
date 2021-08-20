from tests.TestQuestion7 import lines_are_parallel


def test_lines_are_parallel_1():
    assert lines_are_parallel([1, 2, 3], [1, 2, 4]) is True


def test_lines_are_parallel_2():
    assert lines_are_parallel([2, 4, 1], [4, 2, 1]) is False


def test_lines_are_parallel_3():
    assert lines_are_parallel([0, 1, 5], [0, 1, 5]) is True
