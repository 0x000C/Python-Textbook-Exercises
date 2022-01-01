# Write a function is_in that accepts two strings as arguments and returns
# True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operator in.

def is_in(string_1, string_2):
    return string_1 in string_2 or string_2 in string_1


print(is_in("Python", "Py"))
