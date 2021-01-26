from auto_test.src.add import my_add

def test_add():
    assert my_add(10,2) == 12, "10 + 2 should be 12"
