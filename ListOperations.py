fruits = ["apple", "banana", "mango", "watermalon"]
print("Original list:", fruits)

print("First fruit:", fruits[0])

print("First two fruits:", fruits[:2])

fruits[1] = "cherry"
print("After modifying second fruit:", fruits)

fruits.append("grapes")
print("After appending:", fruits)

fruits.insert(2, "strawberry")
print("After inserting at index 2:", fruits)

fruits.remove("mango")
print("After removing 'mango':", fruits)

del fruits[0]
print("After deleting first element:", fruits)

last_fruit = fruits.pop()
print("Popped fruit:", last_fruit)
print("After popping:", fruits)

index = fruits.index("strawberry")
print("Index of 'strawberry':", index)

count = fruits.count("watermalon")
print("Count of 'watermalon':", count)

fruits.sort()
print("Sorted list (ascending):", fruits)

fruits.sort(reverse=True)
print("Sorted list (descending):", fruits)

fruits.reverse()
print("Reversed list:", fruits)

fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)

#Extending a list with another
more_fruits = ["dragon fruit", "guava"]
fruits.extend(more_fruits)
print("After extending with more fruits:", fruits)

fruits.clear()
print("After clearing the list:", fruits)
