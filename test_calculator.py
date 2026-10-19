from calculator import add,substract,multiply

def test_add():
    assert add(5, 3) == 8

def test_substract():
    assert substract(5,3) == 2

def test_multiply():
    assert multiply(5,3) == 15