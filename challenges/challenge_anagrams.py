def count_characters(c, dict1, signal):
    if c in dict1:
        dict1[c] += signal
    else:
        dict1[c] = signal


def is_anagram(first_string, second_string):
    dict1 = {}

    if len(first_string) != len(second_string):
        return False

    for i in range(len(first_string)):
        c1 = first_string[i]
        c2 = second_string[i]
        count_characters(c1, dict1, 1)
        count_characters(c2, dict1, -1)

    for c in dict1.values():
        if c != 0:
            return False
    return True


first_string = "worda"
second_string = "ordwe"
print(is_anagram(first_string, second_string))
