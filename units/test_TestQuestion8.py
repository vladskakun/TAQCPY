from tests.TestQuestion8 import vol_shell


def test_vol_shell_1():
    assert vol_shell(3, 3) == 0


def test_vol_shell_2():
    assert vol_shell(7, 2) == 1403.245


def test_vol_shell_3():
    assert vol_shell(3, 800) == 2144660471.753
