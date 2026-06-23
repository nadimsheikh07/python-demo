import copy

# A nested list
original = [[1, 2], [3, 4]]

# Create both copies
shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modify the nested list inside the shallow copy
shallow[0][0] = 99

print(original)  # Output: [[99, 2], [3, 4]] -> (Original changed!)
print(shallow)  # Output: [[99, 2], [3, 4]]

# Modify the nested list inside the deep copy
deep[1][0] = 88

print(original)  # Output: [[99, 2], [3, 4]] -> (Original safe!)
print(deep)  # Output: [[99, 2], [88, 4]]
