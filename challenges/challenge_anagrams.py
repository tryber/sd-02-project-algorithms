def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    def merge_sort(first, second=""):
        array = list(first)
        array.extend(second)
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
        return merge(left, right, array)

    merged = merge_sort(first_string, second_string)
    for index in range(len(merged)):
        if index % 2 > 0 and merged[index] != merged[index - 1]:
            return False
    return True


first_string = "pato"
second_string = "tapo"
print(is_anagram(first_string, second_string))
