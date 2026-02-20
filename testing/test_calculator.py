from calculator import add, division
def test_add1():
    assert add(5, 6) == 11
def test_add2():
    assert add(1, 1) == 3
def test_division1():
    assert division(10, 2) == 5.0
def test_division2():
    assert division(10, 2) == 5.1
