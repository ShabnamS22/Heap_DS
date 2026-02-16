"""
heapsort.py

Implements HeapSort using a max-heap.
Time Complexity: O(n log n)
Space Complexity: O(1)
"""

def heapify(arr, n, i):
    """
    Maintains max heap property for subtree rooted at index i
    
    parameters:
    arr : list the array representing the heap
    n: int size of heap
    i: int index of current root
    Time complexity: O(log n)
    """
    largest = i        #Initialize largest as root
    left = 2 * i + 1   #left child 
    right = 2 * i + 2  #right child

    # if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # if right child exists and is greater than current larest 
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    # if largest is not root         
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)   # recursively heapify


def heap_sort(arr):
    """
    Main function to perform hHeapSort
    
    Steps:
    1. Build max heap
    2. Extract elements one by one 
    Time Complexity: O(n log n)
    """
    n = len(arr)

    # Build max heap
    # start from last non leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # move root to end
        heapify(arr, i, 0)                # call heapify on reduced heap

    return arr

# for testing
if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6, 7]
    print("Original array:", sample)
    print("Sorted array:", heap_sort(sample))
