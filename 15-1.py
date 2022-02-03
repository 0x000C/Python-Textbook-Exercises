
# Use the tabular method to implement a dynamic programming solution that
# meets the specification


def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1
       change is a positive int,
       return the minimum number of coins needed to have a set of
       coins the values of which sum to change. Coins may be used
       more than once. For example, make_change([1, 5, 8], 11)
       should return 3."""
    coins = []
    while coin_vals:
        while coin_vals and max(coin_vals) > (change - sum(coins)):
            coin_vals.remove(max(coin_vals))
        if coin_vals:
            coins.append(max(coin_vals))
    return len(coins)