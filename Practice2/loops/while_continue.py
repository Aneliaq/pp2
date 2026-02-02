# Example 1: Skip even numbers
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints 1, 3, 5

# Example 2: Skip specific value
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip 3
    print(i)  # Prints 1, 2, 4, 5

