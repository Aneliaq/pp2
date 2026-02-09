# Method overriding

class Bird:
    def fly(self):
        print("Flying")


class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly")


p = Penguin()
p.fly()

