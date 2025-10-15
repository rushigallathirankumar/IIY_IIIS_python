class Animal:
     def __init__(self,name):
         self.name=name
     def speak(self):
         return f"{self.name}makes a sound."
     def eat(self):
         return f"{self.name}is eating."
class Dog(Animal):
     def speak(self):
         return f"{self.name}says:bow! bow!"
class Cat(Animal):
     def speak(self):
         return f"{self.name}says:meow! meow!"
if __name__=="__main__":
   dog = Dog("Buddy")
   cat = Cat("whikers")
   print(dog.speak())
   print(cat.speak())





