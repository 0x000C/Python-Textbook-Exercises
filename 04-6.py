def find_root_bounds(x, power):
    """x a float, power a positive int
    return low, high such that low**power <= x and high**power >= x
    """
    low = min(-1, x)
    high = max(1, x)
    return low, high


def bisection_solve(x, eval_ans, epsilon, low, high):
    """x, epsilon, low, high are floats
    epsilon > 0
    eval_ans a function mapping a float to a float
    low <= high and there is an ans between low and high s.t.
        eval(ans) is within epsilon of x
    returns ans s.t. eval(ans) within epsilon of x"""
    ans = (high + low) / 2
    while abs(eval_ans(ans) - x) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


def square(ans):
    return ans**2


low, high = find_root_bounds(99, 2)
print(bisection_solve(99, lambda ans: ans**2, .01, low, high))
