# Example 1: Simple while loop
i = 1
while i <= 5:
    print(i)  # Prints 1, 2, 3, 4, 5
    i += 1

# Example 2: Using string in while loop
text = "Hello"
count = 0
while count < len(text):
    print(text[count])  # Prints each character in "Hello"
    count += 1

# Example 3: Boolean variable controlling while
running = True
steps = 0
while running:
    print("Step:", steps)
    steps += 1
    if steps == 3:
        running = False  # Stop the loop after 3 steps
