#create class
class Student:
    # Constructor 
    def __init__(self, name, age):
        self.name = name   
        self.age = age
        print(f"Constructor called for {self.name}")    

    # display student details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    # Destructor
    def __del__(self):
        print(f"Destructor called for {self.name}")



# Create objects 
student1 = Student("Shruti", 20)
student2 = Student("Snehal", 21)

student1.display_info()
student2.display_info()

# Delete object
del student2
print("program ended")