x, y = 0, 1
filename = '7-3.py Output.txt'

with open(filename, 'w') as outfile:
    outfile.write('0\n1\n')
    for i in range(10):
        z = x+y
        x = y
        y = z
        outfile.write(str(z)+'\n')
        