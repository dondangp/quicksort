import random
import time
import matplotlib.pyplot as plt

# Iterative quicksort with fixed pivot (last element)
def quicksort_fixed(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition_fixed(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def partition_fixed(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Benchmarking function for different cases
def benchmark_quicksort_fixed(array_sizes):
    best_case_times = []
    worst_case_times = []
    average_case_times = []

    for n in array_sizes:
        print(f"Benchmarking for array size: {n}")

        # Best case: Already sorted array
        best_case_input = list(range(n))
        start_time = time.perf_counter()
        quicksort_fixed(best_case_input)
        best_case_times.append(time.perf_counter() - start_time)

        # Worst case: Already sorted array (last element as pivot)
        worst_case_input = list(range(n))
        start_time = time.perf_counter()
        quicksort_fixed(worst_case_input)
        worst_case_times.append(time.perf_counter() - start_time)

        # Average case: Random array
        avg_times = []
        for _ in range(5):  # Run 5 times for averaging
            average_case_input = [random.randint(0, n) for _ in range(n)]
            start_time = time.perf_counter()
            quicksort_fixed(average_case_input)
            avg_times.append(time.perf_counter() - start_time)
        average_case_times.append(sum(avg_times) / len(avg_times))

        print(f"Completed benchmarking for array size: {n}")

    return best_case_times, worst_case_times, average_case_times

# Driver code
if __name__ == "__main__":
    # Reduced input sizes to prevent excessive runtimes
    array_sizes = [2000, 4000, 6000, 8000, 10000]
    best_case_times, worst_case_times, average_case_times = benchmark_quicksort_fixed(array_sizes)

    # Plotting the benchmark results
    plt.plot(array_sizes, best_case_times, label='Best Case', marker='o')
    plt.plot(array_sizes, worst_case_times, label='Worst Case', marker='o')
    plt.plot(array_sizes, average_case_times, label='Average Case', marker='o')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort (Fixed Pivot) Benchmark - Iterative Version')
    plt.legend()
    plt.grid(True)
    plt.show()
