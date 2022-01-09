# Write a program that asks the user to enter an integer and prints two
# integers, root and pwr, such that 1 < pwr < 6 and root**pwr is equal to
# the integer entered by the user. If no such pair of integers exists, it
# should print a message to that effect.

x = int(input('Enter an integer: '))

integer_root_found = False

lower_limit, upper_limit = 2, 5

for pwr in range(lower_limit, upper_limit):
    root = x**(1 / pwr)
    if (int(root) == root):
        print(f'{int(root)}**{pwr}={x}')
        integer_root_found = True
        break

if (not integer_root_found):
    print(f'No integer roots exist with a power of \
{lower_limit} - {upper_limit} for the given value.')
