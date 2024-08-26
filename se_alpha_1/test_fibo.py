# test_fibo_recurs.py
import pytest
from fibonacci import fib

#def test_fail():
    #n = -4
    #assert n >= 0, "n should be greater than equal to 0"  

def test_pass():
    n = 4
    assert fib(n) == 3  # pass

