def arraysorted(n: int, nums : list[int]) -> bool:
    if n <= 1:
        return True

    for i in range(1, n):
        if nums[i] >= nums[i-1]:
            pass
        else:
            return False

    return True

x = arraysorted(3, [1, 2, 3])
print(x)