def find_duplicate(nums):
    nums.sort()
    for i, _ in enumerate(nums):
        i1 = nums[i]
        i2 = nums[i + 1]
        if i1 == i2:
            return i1


nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
print(find_duplicate(nums))
