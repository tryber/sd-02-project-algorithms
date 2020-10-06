def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    sorted_first = merge_sort(list(first_string))
    sorted_second = merge_sort(list(second_string))

    if sorted_first == sorted_second:
        return True
    return False


def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


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


first_string = "oafgieef"
second_string = "foieeagsfgsa"
print(is_anagram(first_string, second_string))

# Porque a complexidade é nlog n?
# O número de divisões é sempre log n:
# Se a lista tiver entre 1 e 2^1 elementos -> 1
# Se a lista tiver entre 1 e 2^2 elementos -> 2
# Se a lista tiver entre 1 e 2^3 elementos -> 3
# Se a lista tiver entre 1 e 2^4 elementos -> 4
# Se a lista tiver entre 1 e 2^5 elementos -> 5
# Como temos n elementos cada um deles terá que ser lido 1 vez
# logo teremos nlog n
