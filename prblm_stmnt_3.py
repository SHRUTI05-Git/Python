
print("Simple Grade System")

names = []
grades = []
while True:
    print("\nWhat do you want to do?")
    print("1 - Add student")
    print("2 - Show all students") 
    print("3 - Find average grade")
    print("4 - Find highest grade")
    print("5 - Find lowest grade")
    print("6 - Sort students by grade")
    print("7 - Count total students")

    choice = input("Pick 1, 2, 3, 4, 5, 6, or 7: ")

    if choice == "1":
        print("\n--- Add Student ---")
        name = input("Student name: ")
        grade = float(input("Student grade: "))
        
        names.append(name)
        grades.append(grade)
        
        print(name, "added with grade", grade)

    elif choice == "2":
        print("\n--- All Students ---")
        if len(names) == 0:
            print("No students yet!")
        else:
            for i in range(len(names)):
                print(names[i], "-", grades[i])

    elif choice == "3":
        print("\n--- Average Grade ---")
        if len(grades) == 0:
            print("No students yet!")
        else:
            average = sum(grades) / len(grades)
            print("Average grade is:", average)

    elif choice == "4":
        print("\n--- Highest Grade ---")
        if len(grades) == 0:
            print("No students yet!")
        else:
            highest = max(grades)
            position = grades.index(highest)
            best_student = names[position]
            
            print("Highest grade:", highest)
            print("Student:", best_student)

    elif choice == "5":
        print("\n--- Lowest Grade ---")
        if len(grades) == 0:
            print("No students yet!")
        else:
            lowest = min(grades)
            position = grades.index(lowest)
            lowest_student = names[position]
            
            print("Lowest grade:", lowest)
            print("Student:", lowest_student)

    elif choice == "6":
        print("\n--- Students Sorted by Grade ---")
        if len(grades) == 0:
            print("No students yet!")
        else:
            positions = list(range(len(grades)))
            sorted_positions = sorted(positions, key=lambda i: grades[i])
            
            print("Students from lowest to highest grade:")
            for i in sorted_positions:
                print(names[i], "-", grades[i])

    elif choice == "7":
        print("\n--- Total Students ---")
        total = len(names)
        print("Total number of students:", total)
        
        if total > 0:
            print("All student names:", names)
            print("All grades:", grades)

        else:
         print("That's not a valid choice!")

