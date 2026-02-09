# Parent and child classes

class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass


d = Dog()
d.speak()

