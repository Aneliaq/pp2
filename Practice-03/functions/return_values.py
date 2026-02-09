# Returning multiple values

def min_max(numbers):
    """Return minimum and maximum values from list"""
    return min(numbers), max(numbers)


nums = [3, 7, 2, 9]
small, big = min_max(nums)
print(small, big)

