#Base class
class Animal:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print("This is an animal..")

# Derived class
class Dog(Animal):
    def getName(self):
        print(f"The name of the dog is {self.name}")

d = Dog("Hira")

d.display()

d.getName()