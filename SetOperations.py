numbers = {1, 2, 3, 4, 5}
more_numbers = {4, 5, 6, 7}
print("Original set (numbers):", numbers)
print("Another set (more_numbers):", more_numbers)

numbers.add(6)
print("After adding 6:", numbers)

numbers.update([7, 8])
print("After updating with [7, 8]:", numbers)

numbers.remove(2)
print("After removing 2:", numbers)

numbers.discard(100)  
print("After discarding 100 :", numbers)

popped_item = numbers.pop()
print("Popped item:", popped_item)
print("After popping:", numbers)

temp_set = {1, 2, 3}
temp_set.clear()
print("After clearing temp_set:", temp_set)

union_result = numbers.union(more_numbers)
print("Union of sets:", union_result)

intersection_result = numbers.intersection(more_numbers)
print("Intersection of sets:", intersection_result)

# Set Difference (elements in numbers but not in more_numbers)
difference_result = numbers.difference(more_numbers)
print("Difference (numbers - more_numbers):", difference_result)

# Symmetric Difference (elements in either but not both)
sym_diff_result = numbers.symmetric_difference(more_numbers)
print("Symmetric Difference:", sym_diff_result)

# Subset check
subset_test = {4, 5}
print("Is {4, 5} a subset of more_numbers?:", subset_test.issubset(more_numbers))

# Superset check
print("Is more_numbers a superset of {4, 5}?:", more_numbers.issuperset(subset_test))

#  Disjoint check
disjoint_test = {10, 11}
print("Are numbers and {10, 11} disjoint?:", numbers.isdisjoint(disjoint_test))

# Converting list to set 
dup_list = [1, 2, 2, 3, 3, 3]
unique_set = set(dup_list)
print("Set from list with duplicates:", unique_set)
