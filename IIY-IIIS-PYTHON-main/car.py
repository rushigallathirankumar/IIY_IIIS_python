class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self)
        return f"{self.make} {self.model} {self.year}"

    def stop(self):
        print(f"{self.year} {self.make} {self.model} Stopping")

my_car = Car("Ford", "Mustang", 1999)
c1 = Car("Benze", "Camry", 2020)

print(my_car)
my_car.stop()  