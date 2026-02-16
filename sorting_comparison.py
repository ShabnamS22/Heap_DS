"""
sorting_comparison.py

Compares HeapSort, QuickSort, and MergeSort
on different input types.
"""

import random
import time
from heapsort import heap_sort


# ---------------- QUICK SORT ----------------
def quick_sort(arr):
    """
    Recursive Quicksort
    
    Averae case: O(n log n)
    worst case: O(n^2)
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    """
    Recursive MergeSort
    
    Time complexity: O(n log n)
    space complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):     # merge two sorted lines
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------------- TESTING ----------------
def test_sorting_algorithm(sort_function, data):        # Measures execution time of sorting function
    start = time.time()
    sort_function(data.copy())
    end = time.time()
    return end - start


if __name__ == "__main__":
    sizes = [1000, 5000, 10000]

    for size in sizes:
        random_data = [random.randint(0, 100000) for _ in range(size)]

        print(f"\nData Size: {size}")

        print("HeapSort:", test_sorting_algorithm(heap_sort, random_data))
        print("QuickSort:", test_sorting_algorithm(quick_sort, random_data))
        print("MergeSort:", test_sorting_algorithm(merge_sort, random_data))
