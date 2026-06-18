rows = 10
for i in range(1, rows + 1):
    # Calculate the spaces needed for centering
    spaces = " " * (rows - i)
    # Generate odd numbers of blocks (1, 3, 5, 7...)
    blocks = "*" * (2 * i - 1)
    print(spaces + blocks)


for i in range(rows):
    print("*" * i)
