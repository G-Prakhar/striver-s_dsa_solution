def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
        
    return max_count

x = findMaxConsecutiveOnes([1, 0, 1, 1, 0, 0, 1, 1, 1, 0])
print(x)
