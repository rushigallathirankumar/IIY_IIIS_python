class Animal:
     def make_sound(self):
         return "Some generic animal sound"
class Dog(Animal):
     def make_sound(self):
         return "boo! boo!"
class Cat(Animal):
     def make_sound(self):
         return "meow!"
class Bird(Animal):
     def make_sound(self):
         return "chup! chup!"
     def animal_sound(animal):
         print(animal,make_sound())
if __name__=="__main__":
   animals= [Dog(),Cat(),Bird()]
   for a in animals:
    animal_sound(a)
