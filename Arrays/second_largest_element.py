"""Edge case: the array can have duplicates
which means that even after getting the 
second last element of a sorted array it doesn't 
needs to be second largest."""

def secondlargensmall(arr: List[int]) -> int:
    largest = arr[0]
    secondlargest = float('-inf')
    smallest = arr[0]
    secondsmallest = float('inf')

    for i in range(len(arr)):
        if arr[i] > largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secondlargest:
            secondlargest = arr[i]

    for i in range(len(arr)):
        if arr[i] < smallest:
            secondsmallest = smallest
            smallest = arr[i]
        elif arr[i] > smallest and arr[i] < secondsmallest:
            secondsmallest = arr[i]

    print(secondsmallest, secondlargest)    

secondlargensmall([1, 2, 4, 7, 7, 5])