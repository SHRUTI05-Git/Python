class Student:
    def __init__(self, name, age, roll):
        self.name = name          # public
        self._age = age           # protected
        self.__roll = roll        # private

    def display(self):
        print(f"Name: {self.name}, Age: {self._age}, Roll: {self.__roll}")

# Create object
s = Student("Shruti", 21, 101)
s.display()

# Accessing
print(s.name)       # public
print(s._age)       # works, but treated as protected
# print(s.__roll)   # Error (private)
print(s._Student__roll)  # Access private using name mangling
