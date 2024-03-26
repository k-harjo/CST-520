import timeit
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr_search = [3, 5, 7, 11, 13, 17, 19]  
target = 11

arr_sort = [random.randint(1, 100) for _ in range(10)]

time_bubble = timeit.timeit('bubble_sort(arr_sort.copy())', globals=globals(), number=1000)
time_quick = timeit.timeit('quick_sort(arr_sort.copy())', globals=globals(), number=1000)
time_linear = timeit.timeit(lambda: linear_search(arr_search, target), number=1000)
time_binary = timeit.timeit(lambda: binary_search(arr_search, target), number=1000)

print(f"Bubble Sort time: {time_bubble:.6f}s")
print(f"QuickSort time: {time_quick:.6f}s")
print(f"Linear Search time: {time_linear:.6f}s")
print(f"Binary Search time: {time_binary:.6f}s")
