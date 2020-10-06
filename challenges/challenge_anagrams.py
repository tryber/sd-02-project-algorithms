def merge_sort(string):
    if len(string) < 2:
        return string
    final_arr = []
    mid = int(len(string)/2)
    left_string = merge_sort(string[:mid])
    right_string = merge_sort(string[mid:])
    i = 0
    j = 0
    while i < len(left_string) and j < len(right_string):
        if left_string[i] > right_string[j]:
            final_arr.append(right_string[j])
            j += 1
        else:
            final_arr.append(left_string[i])
            i += 1
    final_arr += left_string[i:]
    final_arr += right_string[j:]
    print(final_arr)
    return final_arr


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return (merge_sort(first_string) == merge_sort(second_string))


first_string = "pedra"
second_string = "perda"
print(is_anagram(first_string, second_string))
