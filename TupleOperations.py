numbers = (10, 20, 30, 20, 40)
print("Original number tuple:", numbers)

print("First element:", numbers[0])

print("First three elements:", numbers[:3])

print("Count of 20:", numbers.count(20))

print("Index of 30:", numbers.index(30))

print("Iterating through numbers:")
for num in numbers:
    print(num)

print("Is 40 in the tuple?", 40 in numbers)

print("Length:", len(numbers))

more_numbers = (50, 60)
combined_numbers = numbers + more_numbers
print("Concatenated tuple:", combined_numbers)

repeated_numbers = (1, 2) * 3
print("Repeated tuple:", repeated_numbers)

#Convert list to tuple
num_list = [70, 80, 90]
tuple_from_list = tuple(num_list)
print("Tuple from list:", tuple_from_list)

# Nested tuple
nested_tuple = ((1, 2), (3, 4))
print("Nested tuple:", nested_tuple)
print("Accessing nested element [1][1]:", nested_tuple[1][1])


