import pytest

@pytest.mark.parametrize("a,b,result",[(1,2,3),(3,4,7)])
def test_add(a,b,result):
    print(a+b)
    assert a+b==result

@pytest.mark.smoke
def test_smoke1():
    assert True

@pytest.mark.skip(reason="not ready")
def test_skip():
    pass
