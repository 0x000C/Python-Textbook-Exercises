prime_total = 0

for i in range(3, 999, 2):
    is_i_prime = True
    for j in range(3, i, 2):
        if (not i % j):
            is_i_prime = False
            break
    if (is_i_prime):
        prime_total += i

print(prime_total)
