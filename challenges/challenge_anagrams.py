def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    dictionary = dict()

    for letter in first_string:
        try:
            dictionary[letter] += 1
        except KeyError:
            dictionary[letter] = 1

    for letter in second_string:
        try:
            dictionary[letter] -= 1
        except KeyError:
            return False

        if dictionary[letter] == -1:
            return False

    return True


first_string = ""
second_string = ""
print(is_anagram(first_string, second_string))
