class Car:
    def __init__(self):
      self.make=input("enter car make")
      self.model=input("enter car model")
      self.year=int(input("enter car year"))

car=Car()
c1=Car()
print(car.make)
print(car.model)
print(car.year)
print(c1.make)
print(c1.model)
print(c1.year)