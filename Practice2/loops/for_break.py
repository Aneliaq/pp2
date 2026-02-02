# Example 1: Stop loop when a condition is met
for i in range(10):
    if i == 5:
        break  # Exit the loop
    print(i)  # Prints 0,1,2,3,4

# Example 2: Stop when found a specific item
colors = ["red", "green", "blue"]
for color in colors:
    if color == "green":
        break
    print(color)  # Prints "red"
