from auto_test_py.src.divide import my_divide

def test_divide():
    assert my_divide(10,2) == 5, "10 / 2 should be 5"

def test_divide_zero():
    assert my_divide(10,0) == 0, "10 / 0 should be 0"

