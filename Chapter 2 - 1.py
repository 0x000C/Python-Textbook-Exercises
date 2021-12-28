# Write a program that examines three variables - x, y, and z - and prints
# the largest odd number among them. If none of them are odd, it should
# print the smallest value of the three

x, y, z = 6, 2, 4

answer = min(x, y, z)

for i in (x, y, z):
    if (i % 2 and i > answer):
        answer = i

print(answer)
