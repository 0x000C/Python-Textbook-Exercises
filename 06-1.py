# The harmonic sum of an integer, n > 0, can be calculated using the
# formula . Write a recursive function that computes this.

def harmonic_sum_recursive(n):
    """Assumes n an int > 0
       Returns the sum of 1/k from k=1 to k=n"""
    if n == 1:
        return n
    else:
        return (1 / n) + harmonic_sum_recursive(n - 1)
