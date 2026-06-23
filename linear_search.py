def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


nums = [40, 10, 3, 2, 4]  # Does not need to be sorted!
target_val = 10

result = linear_search(nums, target_val)
print(result)  # Output: 1
