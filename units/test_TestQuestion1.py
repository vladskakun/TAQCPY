import pytest
from tests.TestQuestion1 import fizz_buzz


def test_fizz_buzz_3():
    assert fizz_buzz(3) == "Fizz"


def test_fizz_buzz_5():
    assert fizz_buzz(5) == "Buzz"


def test_fizz_buzz_15():
    assert fizz_buzz(15) == "FizzBuzz"
