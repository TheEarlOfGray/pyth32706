from app import myfunc


def test_myfunc():
    assert myfunc(2, 4) == 4
    assert myfunc(2, 7) == 7
def test_myfunc2():
    assert myfunc(2, 17) == 17
def test_myfunc3():
    assert myfunc(1, 4) == "it's a 1!!!"