names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate example
for index, name in enumerate(names):
    print(index, name)

# zip example
for name, score in zip(names, scores):
    print(name, score)

# sorted example
numbers = [5, 2, 9, 1]
print("Sorted:", sorted(numbers))

# type conversion
num_str = "123"
print(int(num_str))
print(float(num_str))
