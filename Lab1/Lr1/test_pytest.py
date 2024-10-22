from main import calculate

def test_plus1():
    assert calculate(999, 1, '+') == 1000

def test_minus1():
    assert calculate(1, -1, '-') == 0
    