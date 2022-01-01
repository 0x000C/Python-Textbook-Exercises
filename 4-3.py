# Write a function to test is_in.
import string
import random


def is_in(string_1, string_2):
    return string_1 in string_2 or string_2 in string_1


def is_in_test():
    # Tests is_in with several true and false inputs. Returns -1 if is_in
    # passes, 0 if is_in fails

    def random_string(string_length):
        return ''.join(random.choices(string.ascii_letters, k=string_length))

    test_count, string_length = 10, 10

    is_in_correct = -1

    print("True testing...")
    for i in range(test_count):
        string_1 = random_string(string_length)
        string_2 = string_1[1:3]
        if not (is_in(string_1, string_2) and is_in(string_2, string_1)):
            print(
                f"Incorrect result from is_in. Should be True, returned False. Strings used: {string_1}, {string_2}")
            is_in_correct = 0

    print("False testing...")
    for i in range(test_count):
        string_1 = random_string(string_length)
        string_2 = "123"
        if (is_in(string_1, string_2) or is_in(string_2, string_1)):
            print(
                f"Incorrect result from is_in. Should be False, returned True Strings used: {string_1}, {string_2}")
            is_in_correct = 0

    return is_in_correct


is_in_test()
