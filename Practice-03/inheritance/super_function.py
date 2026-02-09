# Using super()

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


s = Student("Tom", 10)
print(s.name, s.grade)

