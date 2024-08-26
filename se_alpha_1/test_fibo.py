# test_fibo_recurs.py
import pytest
from fibonacci import fib

def test_fibo_recurs():
    assert fib(4) == 3  # This should pass because the correct result is 3
    assert fib(4) == 5  # This should fail because the correct result is 3
