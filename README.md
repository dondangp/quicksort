# Quicksort Benchmark 


# Quicksort Performance Analysis

## Overview
In this project, I simulated the performance characteristics of the non-random pivot version of the quicksort algorithm. The code in `quicksort_performance.py` generates a plot showing the best, average, and worst-case scenarios using hardcoded values to represent typical quicksort behavior.

## Mathematical Derivation of Average Runtime Complexity
### 1. Introduction
Quicksort is a divide-and-conquer algorithm that sorts an array by partitioning it into smaller subarrays. For the non-random pivot version, a fixed element (such as the first or last element) is chosen as the pivot.

### 2. Understanding the Partitioning Process
In quicksort:
1. The array is partitioned into two subarrays around the pivot.
2. The partitioning operation runs in linear time, i.e., O(n).
3. After partitioning, the pivot element is in its correct position, and the process is recursively applied to the subarrays.

### 3. Average Case Analysis
I derived the average-case time complexity by considering the recursive nature of quicksort. Here’s how it breaks down:

1. **Recursive Relation:** 
   The average runtime `T(n)` can be expressed as:
   \[
   T(n) = n + \frac{1}{n} \sum_{k=0}^{n-1} (T(k) + T(n - k - 1))
   \]
   - `n` represents the time for the partitioning operation.
   - The summation represents the average runtime over all possible splits of the array.

2. **Simplifying the Equation:**
   Assuming that the pivot splits the array into two equal parts on average, the recurrence simplifies to:
   \[
   T(n) = n + 2T\left(\frac{n}{2}\right)
   \]

3. **Solving the Recurrence:**
   Using the recursion tree method, each level of the tree contributes `n` to the total runtime. Since there are approximately `log_2(n)` levels, the total runtime is:
   \[
   T(n) = n \log_2(n)
   \]

### 4. Conclusion
From this derivation, the average-case time complexity of the non-random pivot version of quicksort is **O(n log n)**. However, I noted that the worst case, where the pivot results in extremely unbalanced partitions (e.g., an already sorted array), can degrade to **O(n²)**.

### 4. Conclusion
From this derivation, the average-case time complexity of the non-random pivot version of quicksort is **O(n log n)**. However, the worst case, where the pivot results in extremely unbalanced partitions (e.g., an already sorted array), can degrade to **O(n^2)**.


