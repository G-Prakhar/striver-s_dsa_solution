def rotateArray(nums, k : int) -> None:
    temp = nums[:k]

    for i in range(k, len(nums)):
        nums[i - k] = nums[i]

    for i in range(k):
        nums[-k + i] = temp[i]

    return nums

x = rotateArray([1,2,3,4,5,6], 2)
print(x)