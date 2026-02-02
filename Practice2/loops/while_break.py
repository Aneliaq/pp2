# Example 1: Break when condition is met
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break  # Stop the loop when i > 5

# Example 2: Break with user input simulation
count = 0
while True:
    count += 1
    print("Count:", count)
    if count == 3:
        break  # Exit loop at 3
