# What would the code in Figure 3-5 do if x=-25

# Because x < 0, ans**2 < x is always false, and the low range estimate
# stays bound to zero. ans will approach zero, so the while loop will run
# infinitely, with the high estimate approaching zero. Therefore this
# program as written can only search for positive square roots.

x = -25

epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)
