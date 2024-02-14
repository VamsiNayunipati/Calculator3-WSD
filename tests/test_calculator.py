'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(4,2) == 6

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(4,2) == 2

def test_multiply():
    '''Test that addition function works '''    
    assert multiply(2,4) == 8

def test_divide():
    '''Test that addition function works '''    
    assert divide(2,2) == 1
    