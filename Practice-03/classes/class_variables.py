# Class vs instance variables

class Student:
    school_name = "Green School"   # class variable

    def __init__(self, name):
        self.name = name           # instance variable


s1 = Student("Alex")
s2 = Student("Kate")

print(s1.school_name)
print(s2.name)

