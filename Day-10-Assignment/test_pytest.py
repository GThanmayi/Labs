import pytest


def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def test_mul():
    assert mul(3,5)==15

def test_div():
    assert div(10,2)==5

def test_div_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        assert div(3,0)