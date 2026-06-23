def counter():
    # Initialize the attribute if it doesn't exist yet
    if not hasattr(counter, "state"):
        counter.state = 0

    counter.state += 1
    return counter.state


# Example Usage:
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3

print("----------------")


def create_counter():
    state = 0  # Enclosed variable (persists in memory)

    def incrementer():
        nonlocal state  # Critical: allows modification of outer scope variable
        state += 1
        return state

    return incrementer


# Example Usage:
my_counter = create_counter()
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3

print("----------------")


def generator_counter():
    state = 0
    while True:
        state += 1
        yield state  # Pauses execution and returns the current value


# Example Usage:
my_gen = generator_counter()
print(next(my_gen))  # Output: 1
print(next(my_gen))  # Output: 2
print(next(my_gen))  # Output: 3
