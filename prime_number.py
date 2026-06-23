def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check factors up to the square root
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Testing numbers using f-strings
for num in range(10):
    status = "is prime" if is_prime(num) else "is NOT prime"
    print(f"The number {num} {status}.")
