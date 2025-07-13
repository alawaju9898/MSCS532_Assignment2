import time
import random
import sys

from memory_profiler import memory_usage

# Quick Sort Algorithm
def quick_sort(arr):
    """Quick Sort using Divide-and-Conquer."""
    if len(arr) <= 1:
        return arr  # Base case: an array of 0 or 1 element is already sorted
    pivot = arr[len(arr) // 2]  # Choose a pivot element (middle element)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort subarrays


# Merge Sort Algorithm
def merge_sort(arr):
    """Merge Sort using Divide-and-Conquer."""
    if len(arr) <= 1:
        return arr  # Base case: an array of 0 or 1 element is already sorted
    mid = len(arr) // 2  # Find the midpoint
    left = merge_sort(arr[:mid])  # Recursively sort the left half
    right = merge_sort(arr[mid:])  # Recursively sort the right half
    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Add remaining elements from left
    result.extend(right[j:])  # Add remaining elements from right
    return result


# Performance Comparison
def analyze_algorithm(algorithm, data):
    """Analyze execution time and memory usage of a sorting algorithm."""
    start_time = time.time()
    start_memory = memory_usage()[0]
    sorted_data = algorithm(data.copy())
    end_memory = memory_usage()[0]
    execution_time = time.time() - start_time
    memory_used = end_memory - start_memory
    return execution_time, memory_used
