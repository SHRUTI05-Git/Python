
# Open source file in read mode
source = open("source.txt", "r")

# Open destination file in write mode
destination = open("destination.txt", "w")

# Read content from source
content = source.read()

# Write content to destination
destination.write(content)

print("File copied successfully!")

# Close both files
source.close()
destination.close()
