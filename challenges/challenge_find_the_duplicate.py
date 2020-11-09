def find_duplicate(nums):
    sorted_nums = sorted(nums)
    for index, num in enumerate(sorted_nums):
        if num == sorted_nums[index + 1]:
            return num
    return False

nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
print(find_duplicate(nums))


nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))
# saída: 2

nums = [3, 1, 3, 4, 2]
print(find_duplicate(nums))
# saída: 3

nums = [1, 1]
print(find_duplicate(nums))
# saída: 1

nums = [1, 1, 2]
print(find_duplicate(nums))