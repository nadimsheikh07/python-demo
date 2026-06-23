def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculates the middle index safely to avoid potential overflow
        mid = low + (high - low) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target was not present in the list
    return -1


# Example Usage:
numbers = [2, 3, 4, 10, 40]  # Must be sorted!
target_value = 10

result = binary_search(sorted(numbers), target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
