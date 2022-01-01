# What would have to be changed to make the code in Figure 3-5 work for
# finding an approximation to the cube root of both negative and positive
# numbers? Hint: think about changing low to ensure that the answer lies
# within the region being searched.

# low needs to be able to bind to negative numbers, the bisection
# search loop needs to account for negative x values in it's test, and
# bisection search loop needs changes to allow low to be changed
# appropriately when x is negative

x = 102

epsilon = 0.01
num_guesses = 0
low = min(0, x)
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - abs(x)) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if (ans > 0 and ans**2 < x):
        low = ans
    elif (ans < 0 and ans**2 > abs(x)):
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)
