"""Bunch of functions that do square root"""

def lazy_sqrt(x: int):
    """simplest way to do square root"""
    return x**0.5

def builtin_sqrt(x: int):
    """use the math library to get the square root"""
    from math import sqrt
    return sqrt(x)

def newton_sqrt(x: int):
    """uses the Newton method to return square root"""
    val = x
    while True:
        last = val
        val = (val + x /val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val
