"""
priority_queue.py

Description:
Implements a Priority Queue using a binary min-heap.
Used for task scheduling simulations.

Time Complexity:
- insert: O(log n)
- extract_min: O(log n)
- decrease_key: O(log n)
- is_empty: O(1)
"""


class Task:
    """
    Represents a task in the scheduler.
    """

    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        """
        Defines comparison for min-heap.
        Lower priority value means higher importance.
        """
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"


class PriorityQueue:
    """
    Binary Min-Heap implementation.
    """

    def __init__(self):
        self.heap = []

    def is_empty(self):
        """
        Returns True if heap is empty.
        Time Complexity: O(1)
        """
        return len(self.heap) == 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, task):
        """
        Inserts new task into heap.
        Time Complexity: O(log n)
        """
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """
        Removes and returns highest priority task.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def decrease_key(self, index, new_priority):
        """
        Decreases priority and restores heap.
        Time Complexity: O(log n)
        """
        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def _heapify_up(self, i):
        """
        Moves element upward to restore heap property.
        """
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = \
                self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _heapify_down(self, i):
        """
        Moves element downward to restore heap property.
        """
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = \
                self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)


# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.insert(Task(1, 3, 0, 10))
    pq.insert(Task(2, 1, 1, 5))
    pq.insert(Task(3, 2, 2, 8))

    while not pq.is_empty():
        print("Processing:", pq.extract_min())
