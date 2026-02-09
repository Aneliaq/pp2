# __init__ constructor

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} ({self.year})"


car = Car("Toyota", 2020)
print(car.info())

