# Benchmark 

![Figure_1](https://github.com/user-attachments/assets/55833ecc-ed0d-4a8a-a4ad-14932a9e0d82)

### Benchmark Environment
- **Operating System**: macOS 14.4.1 (23E224)
- **Processor/Chip**: Apple M2 (8-core CPU)
- **Clock Speed**: Up to 3.49 GHz
- **RAM**: 8 GB
- **Storage**: 245.11 GB Macintosh HD
- **Python Version**: 3.12.0
- **Virtual Environment**: Yes (`venv`)
- **Major Dependencies**: `timeit`, `matplotlib`
- **Device Power Status**: Plugged in
- **Background Processes**: Minimal activity, no significant CPU load during benchmarking.

# Quicksort Performance Analysis

## Overview
I simulated the performance characteristics of the non-random pivot version of the quicksort algorithm. The code in `quicksort_performance.py` generates a plot showing the best, average, and worst-case scenarios using hardcoded values to represent typical quicksort behavior.

## Mathematical Derivation of Average Runtime Complexity
### 1. Introduction
Quicksort is a divide-and-conquer algorithm that sorts an array by partitioning it into smaller subarrays. For the non-random pivot version, a fixed element (such as the first or last element) is chosen as the pivot.

### 2. Understanding the Partitioning Process
In quicksort:
1. The array is partitioned into two subarrays around the pivot.
2. The partitioning operation runs in linear time, i.e., **O(n)**.
3. After partitioning, the pivot element is in its correct position, and the process is recursively applied to the subarrays.

### 3. Average Case Analysis
I derived the average-case time complexity by considering the recursive nature of quicksort. Here’s how it breaks down:

1. **Recursive Relation:** 
   The average runtime `T(n)` can be expressed as:
T(n) = n + (1/n) * [T(0) + T(1) + T(2) + ... + T(n-1)]

- The term `n` represents the time for the partitioning operation.
- The summation represents the average runtime over all possible ways of splitting the array.

2. **Simplifying the Equation:**
The fixed pivot splits the array into two roughly equal parts on average, the recurrence simplifies to:
T(n) = n + 2 * T(n / 2)


3. **Solving the Recurrence:**
Using the recursion tree method, each level of the tree contributes approximately `n` to the total runtime. Since there are about `log2(n)` levels, the total runtime simplifies to:
T(n) = O(n log n)

### 4. Conclusion
From this derivation, the average-case time complexity of the non-random pivot version of quicksort is **O(n log n)**. However, the worst case, where the pivot results in extremely unbalanced partitions (e.g., an already sorted array), can degrade to **O(n^2)**.
