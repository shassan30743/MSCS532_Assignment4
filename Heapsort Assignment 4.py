# Heapsort implementation
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right child exists and is greater than the current largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Mergesort implementation
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Priority Queue and Task Class
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            max_task = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            max_task = self.heap.pop()
        else:
            max_task = None
        return max_task

    def increase_priority(self, index, new_priority):
        if self.heap[index].priority < new_priority:
            self.heap[index].priority = new_priority
            self._heapify_up(index)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0

# Performance comparison for sorting algorithms
import time
import numpy as np

def compare_sorting_algorithms():
    arr_sizes = [1000, 5000, 10000]
    results = {}

    for size in arr_sizes:
        arr = np.random.randint(0, 10000, size).tolist()
        
        start_time = time.time()
        heapsort(arr.copy())
        heap_time = time.time() - start_time
        
        start_time = time.time()
        quicksort(arr.copy())
        quick_time = time.time() - start_time
        
        start_time = time.time()
        mergesort(arr.copy())
        merge_time = time.time() - start_time
        
        results[size] = {'Heapsort': heap_time, 'Quicksort': quick_time, 'Merge Sort': merge_time}

    for size, times in results.items():
        print(f"\nArray Size: {size}")
        for algo, time_taken in times.items():
            print(f"{algo}: {time_taken:.6f} seconds")

# Example usage of Priority Queue
def test_priority_queue():
    pq = PriorityQueue()
    pq.insert(Task(1, 3, '10:00', '11:00'))
    pq.insert(Task(2, 5, '10:05', '10:30'))
    pq.insert(Task(3, 1, '09:50', '10:45'))

    print("Priority Queue Contents (max-priority first):")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")

# Running the comparison
if __name__ == "__main__":
    print("Sorting Algorithms Performance Comparison:")
    compare_sorting_algorithms()

    print("\nTesting Priority Queue:")
    test_priority_queue()
