def twoSum(nums: List[int], target: int) -> List[int]:
    mpp = {}
    for i in nums:
        more_needed = target - i
        if more_needed in mpp:
            if more_needed == i:
                first = nums.index(i)
                return [mpp[more_needed], nums.index(i, first + 1)]
            return [mpp[more_needed], nums.index(i)]
        mpp[i] = nums.index(i)

x = twoSum([2, 7, 6, 5, 8, 11], 19)
print(x)
