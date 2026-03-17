from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map example
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter example
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# reduce example
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum:", sum_all)
