# sorted() with lambda key

students = [
    ("Tom", 85),
    ("Anna", 92),
    ("Bob", 78)
]

sorted_students = sorted(students, key=lambda s: s[1])

print(sorted_students)

