def removeduplicates(arr : list[int]) -> list[int]:
    i = 0

    for num in arr:
        if num != arr[i]:
            i += 1
            arr[i] = num
    return i + 1            

x = removeduplicates([1, 1, 2, 2, 2, 3, 3, 4])
print(x)