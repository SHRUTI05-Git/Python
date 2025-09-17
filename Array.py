import array as arr
a = arr.array('i',[1,2,3])
print("The new created array is: ",end=" ")
for i in range (0,3):
    print(a[i],end=" ")


b=arr.array('i',[10,20,30,40,50])
print("\nOriginal Array:", b.tolist())

print("\nTraversing the array:")
for i in b:
    print(i, end=" ")

print("\n\nElement at index 2:", b[2])

#  Insert element
b.insert(2, 25)   
print("After inserting 25 at index 2:", b.tolist())

#  Append element
b.append(60)
print("After appending 60:", b.tolist())

# Update element
b[1] = 15
print("After updating index 1 with 15:", b.tolist())

# Delete element by value
b.remove(40)
print("After removing 40:", b.tolist())

#  Delete element by index
del b[3]
print("After deleting element at index 3:", b.tolist())

#  Search element
element = 30
if element in b:
    print(f"{element} found at index:", b.index(element))
else:
    print(f"{element} not found in array")

#  Length of array
print("Length of array:", len(b))