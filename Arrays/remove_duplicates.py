"""the brute force approach is to use a tree-based Set data structure 
and the complexity is O(NlogN + N) as ALL the elements were first
put into a set and then back into the array."""

"""whereas in Python I just converted the array into a hash-based Set
then back to the array so the complexity was just O(N)
which the same as the optimal solution."""

"""But the optimal solution still wins
as it takes O(1) space complextiy."""

def removeduplicates(arr : list[int]) -> list[int]:
    i = 0

    for num in arr:
        if num != arr[i]:
            i += 1
            arr[i] = num
    return i + 1            

x = removeduplicates([1, 1, 2, 2, 2, 3, 3, 4])
print(x)