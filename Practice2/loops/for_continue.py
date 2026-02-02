# Example 1: Skip even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints 1, 3, 5

# Example 2: Skip specific item
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)  # Prints "apple" and "cherry"
