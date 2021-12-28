# Implement a function that satisfies the specification

def find_an_even(L):
    """Assumes L is a list of integers
       Returns the first even number in L
       Raises ValueError if L does not contain an even number"""
    for i in L:
        if not i & 1:
            return i
    raise ValueError

print(find_an_even([1,2,3,4,5]))