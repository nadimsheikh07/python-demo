x = 10


def fun():
    global x
    x = 20
    print(x)


fun()
print(x)


def outer_func():
    y = "hello"  # Enclosing scope

    def inner_func():
        nonlocal y
        y = "world"  # Modifies outer_func's variable

    inner_func()
    print(y)  # Output: world


outer_func()
