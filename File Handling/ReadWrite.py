# Create a new file
# f = open("sample.txt", "x")  
# print("File created successfully")
# f.close()

# Write to a file
f = open("sample.txt", "w")   
f.write("Hello, this is the first line.\n")
f.write("This is the second line.\n")
f.close()

#  Append to a file
f = open("sample.txt", "a")
f.write("This line is appended.\n")
f.close()

#  Read the file
f = open("sample.txt", "r") 
print("Reading the whole file:")
print(f.read())   # read entire file
f.close()

with open("sample 2.txt", "w") as f:
    f.write("This line is 'with'")

with open("sample 2.txt", "a") as f:
    f.write("\nThis line is append 'with'")

with open("sample 2.txt", "r") as f:
    print("This line is read",f.read())
