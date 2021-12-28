# Write a program that prints the sum of the prime numbers greater than 2
# and less than 1000. Hint: you probably want to have a loop that is a
# primality test nested inside a loop that iterates over the odd integers
# between 3 and 999.

def is_Prime(x):
    if (x % 2):
        for i in range(3, x, 2):
            if (not x % i):
                return False
        return True
    else:
        return False


prime_sum = 0

for i in range(3, 999, 2):
    if is_Prime(i):
        prime_sum += i

print("The sum of all prime numbers greater than 2 and less than 1000 is", prime_sum)
