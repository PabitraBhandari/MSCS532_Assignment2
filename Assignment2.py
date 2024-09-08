## Name: Pabitra Bhandari
## Subject : Algorithms and Data Structures
## Assignment : Analyze and implement the divide-and-conquer algorithms (Assignment-2)
## Date: 09/8/2024

import random
import timeit
import tracemalloc

# Quick Sort Algorithm
def quicksort(array):
    if len(array) <= 1:  # Base case: single element or empty list
        return array
    else:
        # Pick pivot, partition around it
        pivot = array[len(array) // 2]
        less_than_pivot = [e for e in array if e < pivot]
        equal_to_pivot = [e for e in array if e == pivot]
        greater_than_pivot = [e for e in array if e > pivot]
        
        return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

# Merge Sort Algorithm
def mergesort(array):
    if len(array) <= 1:  # Base case: if array is one element, it's already sorted
        return array
    
    mid_index = len(array) // 2  # Find the middle index
    L = array[:mid_index]
    R = array[mid_index:]

    # Recursively divide and merge the two halves
    mergesort(L)
    mergesort(R)

    i = j = k = 0  # i for left, j for right, k for merged array
    
    # Merge the sorted halves into the main array
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1

# Function to calculate time and memory usage
def evaluate_algorithm(algorithm, dataset):
    tracemalloc.start()  # Begin tracking memory usage
    start_time = timeit.default_timer()  # Record start time

    algorithm(dataset.copy())  # Execute the algorithm on a copy of the dataset

    end_time = timeit.default_timer()  # Record end time
    current_mem, peak_mem = tracemalloc.get_traced_memory()  # Get memory stats
    tracemalloc.stop()  # Stop tracking memory

    return {
        'time_taken': end_time - start_time,
        'peak_memory_mb': peak_mem / (1024 * 1024)  # Convert to MB
    }

# Define test cases
sorted_data = list(range(10000))  # Data sorted in ascending order
reverse_data = sorted_data[::-1]  # Data sorted in descending order
random_data = random.sample(range(10000), 10000)  # Data shuffled randomly

# Store datasets for easy iteration
test_cases = {
    "Sorted": sorted_data,
    "Reverse Sorted": reverse_data,
    "Random": random_data
}

# General function to report algorithm performance
def report_performance(algorithm_name, algorithm_func):
    print(f"\n{algorithm_name} Performance")
    print("=" * (len(algorithm_name) + 12))
    
    for case_name, case_data in test_cases.items():
        results = evaluate_algorithm(algorithm_func, case_data)
        print(f"{case_name} Dataset:")
        print(f"  Time: {results['time_taken']:.6f} seconds")
        print(f"  Peak Memory: {results['peak_memory_mb']:.6f} MB\n")

# Run and report performance for Quick Sort and Merge Sort
report_performance("Quick Sort", quicksort)
report_performance("Merge Sort", mergesort)