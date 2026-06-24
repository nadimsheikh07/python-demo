l = ["a", "B", "2", 3, 1, "3.a", 1.0]


def try_float(val):
    try:
        return float(val)
    except ValueError:
        return 0


sum = 0
for i in l:
    sum += try_float(i)
print(sum)
