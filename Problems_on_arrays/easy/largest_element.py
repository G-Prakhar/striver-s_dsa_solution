def largestelement(arr: List[int]) -> int:
    largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    print(largest)

largestelement([1, 2, 4, 7, 7, 5])
