class Car:
    # Class variable to store the total object count
    object_count = 0

    def __init__(self, brand):
        self.brand = brand
        # Increment the counter every time a new object is made
        Car.object_count += 1

    def __del__(self):
        # Decrement the counter when an object gets deleted
        Car.object_count -= 1


# Create class objects
car1 = Car("Toyota")
car2 = Car("Honda")
car3 = Car("Ford")

# Print the final count
print(f"Total objects created: {Car.object_count}")
# Output: Total objects created: 3
