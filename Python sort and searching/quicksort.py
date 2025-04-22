def quicksort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot (here, we use the last element)
    pivot = arr[-1]

    # Create two sublists: one with elements less than the pivot, and one with greater or equal
    smaller = []
    greater = []

    for x in arr[:-1]:  # Skip the pivot itself
        if x < pivot:
            smaller.append(x)
        else:
            greater.append(x)

    # Recursively sort the sublists and combine with the pivot in between
    return quicksort(smaller) + [pivot] + quicksort(greater)

# Example
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)

# quicksort([7]) → [7]

# quicksort([4, 7]) → [] + [4] + [7] → [4, 7]

# quicksort([7, 4, 1]) → [] + [1] + [4, 7] → [1, 4, 7]

# quicksort([1, 7, 4, 1]) → [] + [1] + [1, 4, 7] → [1, 1, 4, 7]

# quicksort([1, 7, 4, 1, 10, 9]) → [1, 1, 4, 7] + [9] + [10] → [1, 1, 4, 7, 9, 10]

# Final answer: [] + [-2] + [1, 1, 4, 7, 9, 10] → [-2, 1, 1, 4, 7, 9, 10]

