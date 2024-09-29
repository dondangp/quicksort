import random

def quicksort_random(arr, low, high):
    if low < high:
        # Partitioning index
        pivot_index = partition_random(arr, low, high)
        # Recursively sort elements
        quicksort_random(arr, low, pivot_index - 1)
        quicksort_random(arr, pivot_index + 1, high)

def partition_random(arr, low, high):
    # Select a random pivot index and swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Proceed with partitioning (same as the fixed pivot version)
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Driver code
arr = [10, 7, 8, 9, 1, 5]
quicksort_random(arr, 0, len(arr) - 1)
print("Sorted array with random pivot:", arr)
