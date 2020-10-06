def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    sorted_first = sort_list(first_string)
    sorted_second = sort_list(second_string)
    print(sorted_first)
    print(sorted_second)
    if sorted_first == sorted_second:
        return True
    return False


def sort_list(list_to_sort):
    list_size = len(list_to_sort)
    n_loops = 0
    while list_size != 0 and list_size != 1:
        n_loops += 1
        list_size = list_size // 2

    list_to_iterate = list_to_sort
    iteraction = len(list_to_sort)
    new_list = []
    for n in range(1, n_loops + 1):
        for i in range(0, iteraction - 1, 2):
            new_list.append(merge_two_sorted_lists([*list_to_iterate[i]], [*list_to_iterate[i+1]]))
        if iteraction % 2 != 0:
            new_list.append(list_to_iterate[-1])
        list_to_iterate = new_list
        new_list = []
        iteraction = len(list_to_iterate)
    if len(list_to_iterate) == 2:
        return merge_two_sorted_lists(list_to_iterate[0], list_to_iterate[1])
    return list_to_iterate

def merge_two_sorted_lists(list1, list2):
    list_to_return = []
    list1_position, list2_position = 0, 0
    while list1_position <= len(list1) and list2_position <= len(list2):

        if list2_position == len(list2):
            list_to_return.extend(list1[list1_position:])
            list2_position += list2_position + 1
        elif list1_position == len(list1):
            list_to_return.extend(list2[list2_position:])
            list1_position += list1_position + 1
        elif list1[list1_position] <= list2[list2_position]:
            list_to_return.append(list1[list1_position])
            list1_position += 1
        else:
            list_to_return.append(list2[list2_position])
            list2_position += 1

    return list_to_return


first_string = "opoass"
second_string = "aoopss"
print(is_anagram(first_string, second_string))

# sort_list([1,2,3,4])

# merge_two_lists([8], [7])
# print(merge_two_sorted_lists('aabbc','abbcc'))

# print(sort_list("feaaaaadmjp"))


