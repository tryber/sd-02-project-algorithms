def get_string(left, right):
    left_cursor, right_cursor = 0, 0
    string = ""
    while left_cursor < len(left) and right_cursor < len(right):
        left_string = left[left_cursor]
        right_string = right[right_cursor]
        if  left_string <= right_string:
            string += left_string
            left_cursor += 1
        else:
            string += right_string
            right_cursor += 1
    left_tail = left[left_cursor:]
    right_tail = right[right_cursor:]
    if left_tail:
        string += left_tail
    if right_tail:
        string += right_tail
    return string

def sort_string(string):
    if len(string) <= 1:
        return string
    middle = len(string) // 2
    left, right = sort_string(string[:middle]), sort_string(string[middle:])

    return get_string(left, right) 

def is_anagram(first_string, second_string):
    # O(n log n)
    first_string_sorted = sort_string(first_string)
    second_string_sorted = sort_string(second_string)
    return first_string_sorted == second_string_sorted

first_string = ""
second_string = ""
print(is_anagram(first_string, second_string))

first_string = "amor"
second_string = "roma"
print(is_anagram(first_string, second_string), True)

first_string = "pedra"
second_string = "perda"
print(is_anagram(first_string, second_string), True)

first_string = "pato"
second_string = "tapo"
print(is_anagram(first_string, second_string), True)

first_string = "coxinha"
second_string = "empada"
print(is_anagram(first_string, second_string), False)
