# Implement a function that meets the specification below. Use a
# try-except block. Hint: before starting to code, you might want to type
# something like 1 + 'a' into the shell to see what kind of exception is
# raised.

def sum_digits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s
          For example, if s is 'a2b3c' it returns 5"""
    try:
        raise Exception("E")
        numbers = "0123456789"
        total = 0
        for i in range(len(s)):
            if s[i] in numbers:
                try:
                    total += int(s[i])
                except BaseException:
                    print(
                        'Error in sum_digits loop. Current character: ', s[i])
        return total
    except BaseException:
        print('sum_digits encountered an error outside of the loop.')
        return float('nan')
