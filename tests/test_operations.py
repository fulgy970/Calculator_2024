import pytest
from app.opperations import addition, division, multiplication, subtraction



# Parameterized addition test
@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (2, 3, 5), (-1, -1, -2), (0, 0, 0)])
def test_addition(a, b, expected):
    '''Addition function'''
    assert addition(a, b) == expected

# Parameterized subtraction test
@pytest.mark.parametrize("a, b, expected", [(1, 1, 0), (5, 3, 2), (-1, -1, 0), (0, 5, -5)])
def test_subtraction(a, b, expected):
    '''Subtraction function'''
    assert subtraction(a, b) == expected

# Parameterized multiplication test
@pytest.mark.parametrize("a, b, expected", [(2, 2, 4), (3, 5, 15), (0, 5, 0), (-1, 1, -1)])
def test_multiplication(a, b, expected):
    '''Multiplication function'''
    assert multiplication(a, b) == expected

# Parameterized division test
@pytest.mark.parametrize("a, b, expected", [(2, 2, 1), (10, 5, 2), (9, 3, 3)])
def test_division(a, b, expected):
    '''Positive Division Test'''
    assert division(a, b) == expected

# Test for division by zero with fixture
def test_division_by_Zero_expection():
    '''Division function testing that I get the expection divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
