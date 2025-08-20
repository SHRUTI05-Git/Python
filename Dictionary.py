student = {
    "name": "Johny",
    "age": 21,
    "grade": "A",
    "courses": ["Math", "Science"]
}

print("Original Dictionary:", student)

print("Name:", student["name"])
print("Age:", student.get("age"))  

student["university"] = "DYP"
print("After Adding University:", student)

student["grade"] = "A+"
print("After updating grade value:",student)

student.pop("age")
print("After Removing Age:", student)

print("\nAll Keys:", student.keys())

print("All Values:", student.values())

student_copy = student.copy()
print("Copied Dictionary:", student_copy)

student.clear()
print("After Clearing Dictionary:", student)