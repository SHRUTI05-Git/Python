# students = []
# grades = []

# def add_student(name, grade):
#     students.append(name)
#     grades.append(grade)
#     print(f"{name} added with grade {grade}.")

# def update_grade(name, new_grade):
#     if name in students:
#         index = students.index(name)
#         grades[index] = new_grade
#         print(f"{name}'s grade updated to {new_grade}.")
#     else:
#         print(f"{name} not found.")

# def remove_student(name):
#     if name in students:
#         index = students.index(name)
#         students.pop(index)
#         grades.pop(index)
#         print(f"{name} removed from the list.")
#     else:
#         print(f"{name} not found.")

# def average_grade():
#     if grades:
#         avg = sum(grades) / len(grades)
#         print(f"Average grade: {avg:.2f}")
#     else:
#         print("No grades available.")

# def highest_and_lowest():
#     if grades:
#         highest = max(grades)
#         lowest = min(grades)
#         print(f"Highest grade: {highest}")
#         print(f"Lowest grade: {lowest}")
#     else:
#         print("No grades available.")

# add_student("Alice", 85)
# add_student("Bob", 92)
# add_student("Charlie", 78)

# update_grade("Alice", 88)
# remove_student("Charlie")

# average_grade()
# highest_and_lowest()

students = []
grades = []

# Add students
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    grade = float(input(f"Enter grade of {name}: "))
    students.append(name)
    grades.append(grade)

# Update a grade
name = input("Enter the name of the student to update: ")
if name in students:
    new_grade = float(input(f"Enter new grade for {name}: "))
    grades[students.index(name)] = new_grade
else:
    print("Student not found.")

# Remove a student
name = input("Enter the name of the student to remove: ")
if name in students:
    index = students.index(name)
    students.pop(index)
    grades.pop(index)
else:
    print("Student not found.")

# Average grade
if grades:
    avg = sum(grades) / len(grades)
    print("Average grade:", avg)
    print("Highest grade:", max(grades))
    print("Lowest grade:", min(grades))
else:
    print("No grades available.")
