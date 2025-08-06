str= "HELLO"
print(str)
print(type(str))
print(str*4)
print(str.lower())
print(str[1])
str1="world"
print(str + str1)

s="hello World!"

#print original string
print("Original string:", repr(s))

#length of string
print("Length: ",len(s))

#convert to uppercase
print("Uppercase: ",s.upper())

#convert to lowercase
print("Lowercase: ",s.lower())

#capatilize first letter
print("Capatilize: ", s.capitalize())

print("Replace 'World' with 'Python':", s.replace("World", "Python"))

print("Find position of 'World':", s.find("World"))

s1="Banana"
print("Count of 'a' in 'banana':", s1.count("a"))

