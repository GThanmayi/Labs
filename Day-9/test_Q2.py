def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(3, 5) == -2

def test_mul():
    assert mul(5, 3) == 15
    assert mul(0, 10) == 0

def test_div():
    assert div(5, 3) == 1
    assert div(10, 2) == 5
