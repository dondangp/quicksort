def quicksort_fixed(arr, low, high):
    if low < high:
        # Partitioning index
        pivot_index = partition_fixed(arr, low, high)
        # Recursively sort elements
        quicksort_fixed(arr, low, pivot_index - 1)
        quicksort_fixed(arr, pivot_index + 1, high)

def partition_fixed(arr, low, high):
    # Pivot as the last element
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Using the function
arr = [10, 7, 8, 9, 1, 5]
quicksort_fixed(arr, 0, len(arr) - 1)
print("Sorted array with fixed pivot:", arr)
