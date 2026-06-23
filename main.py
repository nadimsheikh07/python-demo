rows = 5

for i in range(rows):
    print("*" * i)

for i in range(rows):
    space = " " * (rows - i - 1)
    star = "*" * (2 * i + 1)
    print(space, star)
