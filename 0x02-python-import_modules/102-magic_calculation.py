#!/usr/bin/python3

def magic_calculation(a, b, c):
    from magic_calculation_102 import add, sub
    if a < b:
        return (c)
    if b < c:
        return (a + b)
    else:
        return ((a * b) - c)
