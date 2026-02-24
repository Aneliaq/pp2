import math

# 1. Convert degree to radian
degree = 15
radian = math.radians(degree)
print(radian)

# 2. Calculate the area of a trapezoid
height = 5
base1 = 5
base2 = 6
trapezoid_area = 0.5 * (base1 + base2) * height
print(trapezoid_area)

# 3. Calculate the area of a regular polygon
num_sides = 4
side_length = 25
# Area = (n * s^2) / (4 * tan(pi / n))
polygon_area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print(polygon_area)

# 4. Calculate the area of a parallelogram
base = 5
height_parallelogram = 6
parallelogram_area = base * height_parallelogram
print(parallelogram_area)

