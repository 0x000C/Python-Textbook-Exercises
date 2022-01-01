# Add some code to the implementation of Newton–Raphson that keeps track
# of the number of iterations used to find the root. Use that code as part
# of a program that compares the efficiency of Newton–Raphson and
# bisection search. (You should discover that Newton–Raphson is far more
# efficient.)

k = 11230481703

epsilon = 0.01

newton_guess = k / 2
newton_tries = 0
while abs(newton_guess**2 - k) >= epsilon:
    newton_tries += 1
    newton_guess = newton_guess - \
        (((newton_guess**2) - k) / (2 * newton_guess))

print(f'Newton    - Estimate: {round(newton_guess,6)} | Tries: {newton_tries}')

bisection_guess, bisection_tries, low = 0, 0, 0
high = max(1, k)
bisection_guess = (high + low) / 2
while abs(bisection_guess**2 - k) >= epsilon:
    bisection_tries += 1
    if bisection_guess**2 < k:
        low = bisection_guess
    else:
        high = bisection_guess
    bisection_guess = (high + low) / 2

print(
    f'Bisection - Estimate: {round(bisection_guess,6)} | Tries: {bisection_tries}')
