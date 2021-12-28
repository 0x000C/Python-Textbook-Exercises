# Implement a function that satisfies the specification

def find_an_even(L):
    """Assumes L is a list of integers
       Returns the first even number in L
       Raises ValueError if L does not contain an even number"""
    for i in L:
        if i % 2 == 0:
            return i
    raise ValueError
