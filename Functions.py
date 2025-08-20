# 1. Basic function
def greet():
    print("Hello! Welcome to Python functions.")

greet()

# 2. Function with parameters
def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

add_numbers(10, 5)

# 3. Function with return value
def multiply(x, y):
    return x * y

product = multiply(4, 5)
print("Product:", product)

# 4. Function with default argument
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()
welcome("DYP")

# Lambda Function
# Lambda function to add two numbers
add = lambda x, y: x + y
print("Sum:", add(5, 3))

# Lambda function to square a number
square = lambda n: n * n
print("Square:", square(6))

