def removeduplicates(arr : list[int]) -> list[int]:
    return len(list(set(arr)))

x = removeduplicates([1, 1, 2, 2, 2, 3, 3, 4])
print(x)