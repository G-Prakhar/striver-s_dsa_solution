def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

x = linearSearch([1, 3, 2, 5, 3], 3)
print(x)