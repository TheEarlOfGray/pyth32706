from programs.factorial import fact

def test_factorial_1():
    assert fact(5) == 120

def test_factorial_2():
    assert fact(8) == 40320

def test_factorial_3():
    assert fact(11) == 39916800

def test_factorial_4():
    assert fact(1) == 1