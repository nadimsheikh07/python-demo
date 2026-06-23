n = 10
try:
    res = n / 0  # Raises ZeroDivisionError

except ZeroDivisionError:
    print("Can't be divided by zero!")

finally:
    print("Execution completed.")
