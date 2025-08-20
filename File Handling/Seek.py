f=open("Sample 3.txt","w+")
f.write("Hello this is my first line")
f.seek(6)
print(f.read())
f.seek(11)
f.write("ABCD")

print(f.tell())