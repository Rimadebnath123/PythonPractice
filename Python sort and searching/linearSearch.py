def linear_search(arr, target):
    # Loop through each element in the array
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example usage
# arr = [5, 3, 7, 1, 9, 2]
# target = 7

# Take input from user
arr_input = input("Enter the elements of the array separated by spaces: ")
arr = list(map(int, arr_input.split()))
target = int(input("Enter the number you want to search for: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
